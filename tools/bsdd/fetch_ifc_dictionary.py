#!/usr/bin/env python3
"""
Download the buildingSMART IFC dictionary from bSDD into
``reference/ifc-4.3-classes.csv``.

The file is the authoritative vocabulary for ``RelatedIfcEntityNamesList`` in
``mappings/ifc.csv``: an entity name bSDD's own IFC dictionary does not carry
will not resolve when Brick is published alongside it. Definitions come with
it so the Brick -> IFC alignment can be argued from IFC's wording rather than
from entity names alone.

bSDD's bulk class listing truncates every definition at 101 characters, so the
long ones are re-fetched one class at a time; that is the slow part of a run
(~750 requests, a few minutes, rate-limited).

    python tools/bsdd/fetch_ifc_dictionary.py
"""

import argparse
import csv
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

DICTIONARY_URI = "https://identifier.buildingsmart.org/uri/buildingsmart/ifc/4.3"
CLASSES_API = "https://api.bsdd.buildingsmart.org/api/Dictionary/v1/Classes"
CLASS_API = "https://api.bsdd.buildingsmart.org/api/Class/v1"

REFERENCE_DIR = Path(__file__).resolve().parent / "reference"
OUTPUT = REFERENCE_DIR / "ifc-4.3-classes.csv"

PAGE = 1000
WORKERS = 6
# The bulk listing caps descriptionPart here; anything this long is a prefix
# of the real definition and has to be fetched again per class.
TRUNCATED_AT = 101


def get_json(url, attempts=6):
    """GET with backoff. bSDD answers 429 under even mild concurrency."""
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(url, timeout=60) as response:
                return json.load(response)
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == attempts - 1:
                raise
            retryable = getattr(exc, "code", None) in (429, 500, 502, 503, 504)
            time.sleep((3 if retryable else 1) * (attempt + 1))
    raise AssertionError("unreachable")


def fetch_listing():
    """Every class in the dictionary, paged."""
    rows, offset = [], 0
    while True:
        query = urllib.parse.urlencode(
            {"Uri": DICTIONARY_URI, "Limit": PAGE, "Offset": offset}
        )
        page = get_json(f"{CLASSES_API}?{query}")
        rows.extend(page["classes"])
        offset += page["classesCount"]
        print(f"  {offset}/{page['classesTotalCount']}", flush=True)
        if offset >= page["classesTotalCount"] or not page["classesCount"]:
            return rows, page


def fetch_definition(uri):
    query = urllib.parse.urlencode({"Uri": uri})
    return get_json(f"{CLASS_API}?{query}").get("definition") or ""


def predefined_type(code, parent_code):
    """
    IFC predefined types are published as their own bSDD classes, named by
    concatenation: IfcChiller + AIRCOOLED -> IfcChillerAIRCOOLED. Recovering
    the suffix marks which rows are a specialisation of an entity rather than
    an entity in their own right -- Brick's equipment classes usually align
    with the former.
    """
    if parent_code and code.startswith(parent_code) and code != parent_code:
        return code[len(parent_code) :]
    return ""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument(
        "--include-property-sets",
        action="store_true",
        help="Also emit Pset_/Qto_ rows (classType GroupOfProperties). Their "
        "definitions stay truncated; only entity definitions are re-fetched.",
    )
    args = parser.parse_args()

    print(f"listing {DICTIONARY_URI}")
    listing, meta = fetch_listing()

    wanted = (
        ("Class", "GroupOfProperties") if args.include_property_sets else ("Class",)
    )
    rows = [r for r in listing if r["classType"] in wanted]

    truncated = [
        r
        for r in rows
        if r["classType"] == "Class"
        and len(r.get("descriptionPart", "")) >= TRUNCATED_AT
    ]
    print(f"re-fetching {len(truncated)} truncated definitions")

    def resolve(row):
        return row["code"], fetch_definition(row["uri"])

    full = {}
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        for done, (code, definition) in enumerate(pool.map(resolve, truncated), 1):
            full[code] = definition
            if done % 100 == 0:
                print(f"  {done}/{len(truncated)}", flush=True)

    # A handful of predefined-type rows carry no definition at all, only bSDD's
    # boilerplate note about being a specialisation. Keep the truncated text.
    empty = [c for c, d in full.items() if not d]
    if empty:
        print(f"{len(empty)} classes have no definition in bSDD: {', '.join(empty)}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "code",
                "name",
                "class_type",
                "parent_code",
                "predefined_type",
                "definition",
            ]
        )
        for row in sorted(rows, key=lambda r: r["code"]):
            parent = row.get("parentClassCode", "") or ""
            definition = full.get(row["code"]) or row.get("descriptionPart", "") or ""
            writer.writerow(
                [
                    row["code"],
                    row.get("name", ""),
                    row["classType"],
                    parent,
                    predefined_type(row["code"], parent),
                    " ".join(definition.split()),
                ]
            )

    entities = sum(1 for r in rows if r["classType"] == "Class")
    print(
        f"wrote {args.output} -- {len(rows)} rows ({entities} classes) from "
        f"IFC {meta.get('version')} ({meta.get('status')}, "
        f"released {str(meta.get('releaseDate'))[:10]})"
    )


if __name__ == "__main__":
    main()
