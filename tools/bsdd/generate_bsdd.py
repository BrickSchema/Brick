#!/usr/bin/env python3
"""Generate the Brick bSDD import document.

The mapping itself lives in :mod:`mapping`; this file only supplies dictionary
metadata, orchestrates the three mappings, and writes JSON.
"""

import argparse
import json
import sys
from pathlib import Path

from rdflib import URIRef

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(REPO_ROOT))

from bricksrc.version import BRICK_FULL_VERSION, BRICK_VERSION
from brick_graph import DCTERMS, load_graph, load_unit_map
from mapping import (
    DICTIONARY_URI,
    attach_class_properties,
    export_classes,
    export_entity_properties,
    export_quantities,
    export_substance_property,
    load_ifc_map,
    unique_properties,
)

DEFAULT_SOURCE = REPO_ROOT / "Brick+imports.ttl"


def build_dictionary(graph):
    """Assemble bSDD's Classes, Properties, and ClassProperties collections."""
    classes = export_classes(graph, load_ifc_map())
    unit_map = load_unit_map()
    properties = unique_properties(
        export_quantities(graph, unit_map)
        + export_entity_properties(graph, unit_map)
        + [export_substance_property(graph)]
    )
    attach_class_properties(graph, classes, properties)
    document = {
        "ModelVersion": "2.0",
        "OrganizationCode": "brick",
        "DictionaryCode": "brick",
        "DictionaryName": "Brick Schema",
        "DictionaryVersion": BRICK_FULL_VERSION,
        "LanguageIsoCode": "en-GB",
        "LanguageOnly": False,
        "UseOwnUri": True,
        "DictionaryUri": DICTIONARY_URI,
        "License": "BSD-3-Clause",
        "LicenseUrl": "https://github.com/BrickSchema/Brick/blob/master/LICENSE",
        "ChangeRequestEmailAddress": "info@brickschema.org",
        "MoreInfoUrl": "https://brickschema.org",
        "QualityAssuranceProcedure": "Brick Consortium open review process",
        "QualityAssuranceProcedureUrl": "https://github.com/BrickSchema/Brick/blob/master/CONTRIBUTING.md",
        "Status": "Preview",
        "Classes": classes,
        "Properties": sorted(properties.values(), key=lambda entry: entry["Code"]),
    }
    ontology = URIRef(f"https://brickschema.org/schema/{BRICK_VERSION}/Brick")
    if modified := next(iter(graph.objects(ontology, DCTERMS.modified)), None):
        document["ReleaseDate"] = str(modified)
    return document


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Export Brick as a bSDD dictionary.")
    parser.add_argument("--source", default=str(DEFAULT_SOURCE))
    parser.add_argument("--output", default="bsdd/brick-bsdd.json")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    source = Path(args.source)
    if not source.exists():
        raise SystemExit(
            f"Source ontology not found: {source}. Run `make Brick.ttl` first."
        )
    document = build_dictionary(load_graph(source))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        f"Wrote {output}: {len(document['Classes'])} classes, "
        f"{len(document['Properties'])} properties"
    )


if __name__ == "__main__":
    main()
