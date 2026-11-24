#!/usr/bin/env python3
"""Python re-implementation of RealEstateCore's Tools/DTDL2SHACL (DTDL v2 -> SHACL).

Mirrors the translation in rec/Tools/DTDL2SHACL/Program.cs:

* Interface            -> rdfs:Class + sh:NodeShape (label, comment, rdfs:subClassOf)
* Property (primitive) -> sh:property [ sh:datatype xsd:X ; sh:maxCount 1 ]
* Property (Enum)      -> sh:property [ sh:in (...) ]
* Property (Map/Object/Array) -> sh:property [ sh:node <GeneratedShape> ] + shape
* Relationship         -> sh:property [ sh:nodeKind sh:IRI ; sh:class target ; min/maxCount ]
* Component            -> sh:property [ sh:nodeKind sh:IRI ; sh:maxCount 1 ; sh:class schema ]
                          and types the schema shape as dtmi:dtdl:class:Component

Only content *defined in* an interface is emitted on that interface (inherited
content is reached through rdfs:subClassOf), like the C# tool.

Unlike the C# tool this does not use the Azure DigitalTwins parser, so it does not
validate the DTDL; it only reads the JSON.

Usage:
    python tools/dtdl2shacl.py -i rec/Source/DTDLv2 \
        -n rec/Source/SHACL/DtmiNamespaceMappings.csv -o out.ttl
    # compare against the checked-in Turtle:
    python tools/dtdl2shacl.py -i rec/Source/DTDLv2 \
        -n rec/Source/SHACL/DtmiNamespaceMappings.csv \
        --compare rec/Source/SHACL/RealEstateCore/rec.ttl
    # only what that Turtle lacks (used by the Makefile):
    ... --supplement-for rec/Source/SHACL/RealEstateCore/rec.ttl -o out.ttl
"""

import argparse
import csv
import json
import sys
from pathlib import Path

from rdflib import RDF, RDFS, XSD, BNode, Graph, Literal, Namespace, URIRef

SH = Namespace("http://www.w3.org/ns/shacl#")
DTDL_COMPONENT = URIRef("dtmi:dtdl:class:Component")

PRIMITIVES = {
    "boolean": XSD.boolean,
    "date": XSD.date,
    "dateTime": XSD.dateTime,
    "double": XSD.double,
    "duration": XSD.duration,
    "float": XSD.float,
    "integer": XSD.integer,
    "long": XSD.long,
    "string": XSD.string,
    # NB: the C# tool maps DTDateTimeInfo to xsd:time (apparent typo); we use dateTime.
    "time": XSD.time,
}


def versionless(dtmi: str) -> str:
    return dtmi.split(";")[0]


def version(dtmi: str) -> str:
    return dtmi.split(";")[1] if ";" in dtmi else "1"


def types_of(node: dict) -> list:
    t = node.get("@type", [])
    return t if isinstance(t, list) else [t]


class Translator:
    def __init__(self, mappings, lang_tags=False):
        # mappings: list of (dtmi_base, uri_base, prefix), first match wins
        self.mappings = mappings
        self.g = Graph()
        for _, uri_base, prefix in mappings:
            self.g.bind(prefix, Namespace(uri_base))
        self.g.bind("sh", SH)
        self.g.bind("xsd", XSD)
        self.lang_tags = lang_tags

    # -- identifiers -------------------------------------------------------
    def shacl_id(self, dtmi: str, local: str | None = None) -> URIRef:
        vl = versionless(dtmi)
        explicit = local is not None
        if local is None:
            local = vl.split(":")[-1]
            if vl.startswith("dtmi:dtdl:"):  # reserved DTMIs have '_'-padded names
                local = local.strip("_")
        for base, uri_base, _ in self.mappings:
            if base in vl:
                return URIRef(uri_base + local)
        # fall back to the DTMI itself (C# tool appends the shape name for 2-arg form)
        return URIRef(dtmi + local) if explicit else URIRef(dtmi)

    # -- literals ----------------------------------------------------------
    def add_text(self, subj, pred, node, key):
        val = node.get(key)
        if isinstance(val, str):
            val = {None: val}
        for lang, text in sorted((val or {}).items(), key=str):
            self.g.add(
                (subj, pred, Literal(text, lang=lang if self.lang_tags else None))
            )

    # -- translation -------------------------------------------------------
    def interface(self, iface: dict):
        iid = iface["@id"]
        node = self.shacl_id(iid)
        self.node_shape(node)
        self.add_text(node, RDFS.label, iface, "displayName")
        self.add_text(node, RDFS.comment, iface, "description")
        parents = iface.get("extends", [])
        for parent in [parents] if isinstance(parents, (str, dict)) else parents:
            pid = parent if isinstance(parent, str) else parent["@id"]
            self.g.add((node, RDFS.subClassOf, self.shacl_id(pid)))

        for content in iface.get("contents", []):
            kinds = types_of(content)
            name = content["name"]
            cid = content.get("@id") or versionless(iid) + ":" + name + ";" + version(
                iid
            )
            if "Property" in kinds:
                self.property(node, cid, content)
            elif "Relationship" in kinds:
                self.relationship(node, cid, content)
            elif "Component" in kinds:
                self.component(node, cid, content)

    def node_shape(self, node):
        self.g.add((node, RDF.type, RDFS.Class))
        self.g.add((node, RDF.type, SH.NodeShape))

    def property_shape(self, owner, path):
        ps = BNode()
        self.g.add((owner, SH.property, ps))
        self.g.add((ps, RDF.type, SH.PropertyShape))
        self.g.add((ps, SH.path, path))
        return ps

    def names(self, ps, content):
        self.add_text(ps, SH.name, content, "displayName")
        self.add_text(ps, SH.description, content, "description")

    def property(self, owner, cid, content):
        ps = self.property_shape(owner, self.shacl_id(cid))
        self.names(ps, content)
        self.build_property_shape(ps, content["schema"], content["name"], cid)

    def relationship(self, owner, cid, content):
        ps = self.property_shape(owner, self.shacl_id(cid))
        self.g.add((ps, SH.nodeKind, SH.IRI))
        if content.get("target"):
            self.g.add((ps, SH["class"], self.shacl_id(content["target"])))
        self.names(ps, content)
        if "minMultiplicity" in content:
            self.g.add((ps, SH.minCount, Literal(content["minMultiplicity"])))
        if "maxMultiplicity" in content:
            self.g.add((ps, SH.maxCount, Literal(content["maxMultiplicity"])))

    def component(self, owner, cid, content):
        ps = self.property_shape(owner, self.shacl_id(cid))
        self.g.add((ps, SH.nodeKind, SH.IRI))
        self.g.add((ps, SH.maxCount, Literal(1)))
        schema = self.shacl_id(content["schema"])
        self.g.add((ps, SH["class"], schema))
        self.g.add((schema, RDF.type, DTDL_COMPONENT))
        self.names(ps, content)

    def build_property_shape(self, ps, schema, name, owner_id):
        if isinstance(schema, str):
            self.g.add((ps, SH.datatype, PRIMITIVES[schema]))
            self.g.add((ps, SH.maxCount, Literal(1)))
            return
        kind = schema["@type"]
        if kind == "Enum":
            as_int = schema.get("valueSchema") != "string"
            for ev in schema["enumValues"]:
                v = ev["enumValue"]
                self.g.add((ps, SH["in"], Literal(int(v) if as_int else str(v))))
            return
        # Map / Object / Array -> a generated, reusable NodeShape
        shape_name = (name[:1].upper() + name[1:] if name else "") + "Shape"
        shape_id = self.shacl_id(owner_id, shape_name)
        if (shape_id, RDF.type, SH.NodeShape) not in self.g:
            self.complex_shape(shape_id, schema, shape_name, owner_id)
        self.g.add((ps, SH.node, shape_id))

    def complex_shape(self, shape_id, schema, shape_name, owner_id):
        self.node_shape(shape_id)
        self.add_text(shape_id, RDFS.label, schema, "displayName")
        self.add_text(shape_id, RDFS.comment, schema, "description")
        kind = schema["@type"]
        if kind == "Array":
            first = self.property_shape(shape_id, RDF.first)
            el = schema["elementSchema"]
            if isinstance(el, dict) and el["@type"] in ("Map", "Object", "Array"):
                self.build_property_shape(
                    first, el, shape_name.replace("Shape", "Entry"), owner_id
                )
                self.g.add((first, SH.maxCount, Literal(1)))
            else:
                self.build_property_shape(first, el, "", owner_id)
            rest = self.property_shape(shape_id, RDF.rest)
            self.g.add((rest, SH.maxCount, Literal(1)))
            self.g.add((rest, SH["in"], shape_id))
            self.g.add((rest, SH["in"], RDF.nil))
        elif kind == "Object":
            for field in schema["fields"]:
                path = self.shacl_id(owner_id, field["name"])
                fs = self.property_shape(shape_id, path)
                self.build_property_shape(fs, field["schema"], field["name"], owner_id)
        elif kind == "Map":
            key, value = schema["mapKey"], schema["mapValue"]
            ks = self.property_shape(shape_id, self.shacl_id(owner_id, key["name"]))
            self.g.add((ks, SH.datatype, XSD.string))
            self.g.add((ks, SH.maxCount, Literal(1)))
            vs = self.property_shape(shape_id, self.shacl_id(owner_id, value["name"]))
            self.build_property_shape(vs, value["schema"], value["name"], owner_id)
        else:
            raise ValueError(f"cannot translate schema of type {kind}")


def load_interfaces(root: Path):
    files = [root] if root.is_file() else sorted(root.rglob("*.json"))
    for f in files:
        data = json.loads(f.read_text(encoding="utf-8-sig"))
        for item in data if isinstance(data, list) else [data]:
            if "Interface" in types_of(item):
                yield item


def read_mappings(path: Path, extra):
    out = []
    with open(path, newline="", encoding="utf-8-sig") as fp:
        rows = csv.reader(fp, delimiter=";")
        next(rows)  # header
        out += [(r[0], r[1], r[2]) for r in rows if r]
    for spec in extra:
        base, uri, prefix = spec.split(",")
        out.append((base, uri, prefix))
    return out


def compare(
    generated: Graph, existing_path: Path, prefix_uri: str, max_diffs: int = 25
):
    """Report differences between generated and existing shapes for the given namespace."""
    existing = Graph()
    existing.parse(existing_path)

    def shapes(g):
        out = {}
        for cls in set(g.subjects(RDF.type, SH.NodeShape)):
            if not str(cls).startswith(prefix_uri):
                continue
            props = set()
            for ps in g.objects(cls, SH.property):
                sig = frozenset(
                    (str(p), str(o))
                    for p, o in g.predicate_objects(ps)
                    if p != RDF.type and not isinstance(o, BNode)
                )
                props.add(sig)
            meta = frozenset(
                (str(p), str(o))
                for p, o in g.predicate_objects(cls)
                if p in (RDFS.subClassOf, RDFS.label, RDFS.comment)
                and not isinstance(o, BNode)
            )
            out[cls] = (meta, props)
        return out

    gen, old = shapes(generated), shapes(existing)
    only_gen = sorted(set(gen) - set(old))
    only_old = sorted(set(old) - set(gen))
    print(f"classes: generated={len(gen)} existing={len(old)}")
    print(f"\nin DTDL but not in Turtle: {len(only_gen)}")
    for c in only_gen:
        print("  ", c)
    print(f"\nin Turtle but not in DTDL: {len(only_old)}")
    for c in only_old:
        print("  ", c)

    def short(u):
        u = str(u)
        for ns in (
            "http://www.w3.org/ns/shacl#",
            "http://www.w3.org/2001/XMLSchema#",
            "http://www.w3.org/2000/01/rdf-schema#",
            prefix_uri,
            "https://brickschema.org/schema/Brick#",
        ):
            u = u.replace(ns, "")
        return u

    def render(sig):
        d = {short(k): short(v) for k, v in sig}
        path = d.pop("path", "?")
        return path + " " + " ".join(f"{k}={v}" for k, v in sorted(d.items()))

    changed = 0
    for c in sorted(set(gen) & set(old)):
        gm, gp = gen[c]
        om, op = old[c]
        if gm == om and gp == op:
            continue
        changed += 1
        if changed > max_diffs:
            continue
        print(f"\nDIFF {short(c)}")
        for x in sorted(gm - om):
            print("  + dtdl   ", short(x[0]), "=", short(x[1])[:90])
        for x in sorted(om - gm):
            print("  - turtle ", short(x[0]), "=", short(x[1])[:90])
        for x in sorted(map(render, gp - op)):
            print("  + dtdl   shape", x[:160])
        for x in sorted(map(render, op - gp)):
            print("  - turtle shape", x[:160])
    print(f"\nclasses with differences: {changed}")
    return bool(only_gen or only_old or changed)


def supplement(generated: Graph, existing_path: Path, prefix_uri: str) -> Graph:
    """Return only what the DTDL defines in `prefix_uri` that `existing_path` lacks:
    whole new classes/shapes, plus property shapes whose sh:path is new on an existing class.
    Nothing already in the existing Turtle is re-asserted or altered (labels, constraints, ...).
    """
    existing = Graph()
    existing.parse(existing_path)
    out = Graph()
    for prefix, ns in generated.namespaces():
        out.bind(prefix, ns)

    def copy_tree(
        subj,
    ):  # a subject's triples, recursing into blank-node property shapes
        for p, o in generated.predicate_objects(subj):
            out.add((subj, p, o))
            if isinstance(o, BNode):
                copy_tree(o)

    for cls in sorted(set(generated.subjects(RDF.type, SH.NodeShape))):
        if not str(cls).startswith(prefix_uri):
            continue
        if (cls, RDF.type, SH.NodeShape) not in existing:
            copy_tree(cls)
            continue
        known = {
            existing.value(ps, SH.path) for ps in existing.objects(cls, SH.property)
        }
        for ps in generated.objects(cls, SH.property):
            if generated.value(ps, SH.path) not in known:
                out.add((cls, SH.property, ps))
                copy_tree(ps)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "-i", "--input", required=True, type=Path, help="DTDL root dir or file"
    )
    ap.add_argument(
        "-n",
        "--namespace-mappings",
        required=True,
        type=Path,
        help="CSV (';'-separated) with DTMI;URI;Prefix",
    )
    ap.add_argument(
        "-o", "--output", type=Path, help="output Turtle file (default: stdout)"
    )
    ap.add_argument(
        "--map",
        action="append",
        default=[],
        metavar="DTMI,URI,PREFIX",
        help="extra namespace mapping, e.g. "
        "dtmi:org:brickschema:schema:Brick:,https://brickschema.org/schema/Brick#,brick",
    )
    ap.add_argument(
        "--lang-tags",
        action="store_true",
        help="keep language tags on labels/comments (default: plain literals, as in rec.ttl)",
    )
    ap.add_argument(
        "--supplement-for",
        type=Path,
        metavar="TTL",
        help="write only the REC terms/property shapes missing from this existing Turtle",
    )
    ap.add_argument(
        "--max-diffs",
        type=int,
        default=25,
        help="max per-class diffs printed by --compare",
    )
    ap.add_argument(
        "--compare",
        type=Path,
        metavar="TTL",
        help="diff REC-namespace shapes against an existing Turtle file instead of writing output",
    )
    args = ap.parse_args(argv)

    tr = Translator(
        read_mappings(args.namespace_mappings, args.map), lang_tags=args.lang_tags
    )
    count = 0
    for iface in load_interfaces(args.input):
        tr.interface(iface)
        count += 1
    print(f"translated {count} interfaces, {len(tr.g)} triples", file=sys.stderr)

    rec_uri = next(u for _, u, prefix in tr.mappings if prefix == "rec")
    if args.compare:
        return 1 if compare(tr.g, args.compare, rec_uri, args.max_diffs) else 0
    graph = tr.g
    if args.supplement_for:
        graph = supplement(tr.g, args.supplement_for, rec_uri)
        print(f"supplement: {len(graph)} triples", file=sys.stderr)
    out = graph.serialize(format="turtle")
    if args.output:
        args.output.write_text(out, encoding="utf-8")
    else:
        sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
