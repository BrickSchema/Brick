from rdflib import Graph, Literal, BNode, URIRef
import sys

sys.path.append("..")
from bricksrc.namespaces import RDF, RDFS, BRICK, BSH, SH, SKOS  # noqa: E402
from bricksrc.namespaces import bind_prefixes  # noqa: E402
from bricksrc.properties import properties as property_definitions  # noqa: E402

G = Graph()
bind_prefixes(G)
A = RDF.type

domainShapeDict = {}
rangeShapeDict = {}
subpropertyDict = {}

# Add base Entity shapes
G.parse("BrickEntityShapeBase.ttl", format="turtle")


def bn(item):
    """
    Returns a shortened string version of the rdflib Node for use
    in generating new BNodes
    """
    if isinstance(item, URIRef):
        return item.split("#")[-1]
    return item


# Make shape for expectedDomain property
def addDomainShape(propertyName, expectedType):
    domainShapeDict[propertyName] = expectedType
    shapename = f"{propertyName}DomainShape"
    G.add((BSH[shapename], A, SH.NodeShape))
    G.add((BSH[shapename], SH.targetSubjectsOf, BRICK[propertyName]))
    G.add((BSH[shapename], SH["class"], expectedType))
    G.add(
        (
            BSH[shapename],
            SH["message"],
            Literal(f"Property {propertyName} has subject with incorrect type"),
        )
    )


# Make shape for expectedRange property
def addRangeShape(propertyName, expectedType):
    rangeShapeDict[propertyName] = expectedType
    sh_prop = BNode(f"RangeShape_{bn(propertyName)}")
    shapename = f"{propertyName}RangeShape"
    G.add((BSH[shapename], SH["property"], sh_prop))
    G.add((BSH[shapename], A, SH.NodeShape))
    G.add((sh_prop, SH["path"], BRICK[propertyName]))
    G.add((sh_prop, SH["class"], expectedType))
    G.add((BSH[shapename], SH.targetSubjectsOf, BRICK[propertyName]))
    G.add(
        (
            sh_prop,
            SH["message"],
            Literal(f"Property {propertyName} has object with incorrect type"),
        )
    )


def addPropertyShapes(propertyName, defn):
    for pred, obj in defn.items():
        # We are only concerned with properties that have RDFS.domain or .range
        # predicate.  The temporary replacements for those predicates are
        # brick:expectedDomain and :expectedRange.  See properties.py for
        # explanation.

        if pred == RDFS.domain:
            addDomainShape(propertyName, obj)

        if pred == RDFS.range:
            addRangeShape(propertyName, obj)

        # subproperties are considered after "domain" and "range" are counted for
        if pred == "subproperties":
            for subprop, desc in obj.items():
                addPropertyShapes(subprop, desc)


for name, defn in property_definitions.items():
    addPropertyShapes(name, defn)

# serialize to output
with open("BrickShape.ttl", "w") as fp:
    fp.write(G.serialize(format="turtle").rstrip())
    fp.write("\n")
