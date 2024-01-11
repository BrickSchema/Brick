import rdflib
from datetime import datetime
from bricksrc.namespaces import BRICK, SKOS, SH, XSD, RDFS, DCTERMS, RDF, SDO, OWL

# define the namespace to hold all of our terms, classes, properties, etc
DEMO = rdflib.Namespace("urn:demo_extension#")

# this is the ontology metadata dictionary. It MUST be named 'ontology_definition'
ontology_definition = {
    # required 'namespace' key for ontology declaration
    "namespace": DEMO,
    # optional list of creators (individuals)
    DCTERMS.creator: [
        {
            RDF.type: SDO.Person,
            SDO.email: rdflib.Literal("gtfierro@mines.edu"),
            SDO.name: rdflib.Literal("Gabe Fierro"),
        },
    ],
    # first date of release of extension/ontology
    DCTERMS.issued: rdflib.Literal("2023-07-13"),
    # keep this to ensure the 'modified' date matches when this was last ran
    DCTERMS.modified: rdflib.Literal(datetime.now().strftime("%Y-%m-%d")),
    # a version number for the ontology
    OWL.versionInfo: rdflib.Literal("0.0.1"),
    # a human-readable label for the extension/ontology
    RDFS.label: rdflib.Literal("Demo Extension"),
    # metadata on the publisher of the extension/ontology
    DCTERMS.publisher: {
        # see schema.org for other types, e.g. Consortium or Person
        RDF.type: SDO.Organization,
        SDO.legalName: rdflib.Literal("Not a real org"),
        SDO.sameAs: rdflib.Literal("http://my fake organization website.org"),
    },
    # key-value pairs of prefix to URI of ontology being imported. This will
    # add owl:imports statements to the generated extension
    "imports": {
        "shacl": "http://www.w3.org/ns/shacl#",
    },
    # namespace declarations for any SHACL rules
    "decls": {
        "rdf": RDF,
        "rdfs": RDFS,
        "brick": BRICK,
        "owl": OWL,
        "sh": SH,
        "demo": DEMO,
    },
}

# optional
# the *first* level of this dictionary should have Brick (or otherwise existing)
# classes as keys, and class definition dictionaries as values. Anything further
# nested can follow the normal class dictionary construction.
# This dictionary MUST be named 'classes'
classes = {
    BRICK.Equipment: {
        DEMO["Sensor_Platform"]: {},
        DEMO["PurpleAir_Weather_Station"]: {
            "parents": [BRICK.Weather_Station],
        },
    },
}


# optional
# this dictionary MUST be named 'entity_properties'
entity_properties = {
    DEMO.manufacturer: {
        SKOS.definition: rdflib.Literal("the manufacturer"),
        SH.datatype: XSD.string,
        RDFS.label: rdflib.Literal("manufacturer"),
        "property_of": BRICK.Equipment,
    },
    DEMO.version: {
        SKOS.definition: rdflib.Literal("a MAJOR.MINOR.PATCH version number"),
        SH.node: DEMO.VersionShape,
        RDFS.label: rdflib.Literal("version"),
        "property_of": BRICK.Equipment,
    },
}

# optional
# this dictionary MUST be named 'property_value_shapes'
property_value_shapes = {
    DEMO.VersionShape: {
        "properties": {
            DEMO.versionMajor: {
                SKOS.definition: rdflib.Literal("Major version"),
                "datatype": XSD.integer,
            },
            DEMO.versionMinor: {
                SKOS.definition: rdflib.Literal("Minor version"),
                "datatype": XSD.integer,
            },
            DEMO.versionPatch: {
                SKOS.definition: rdflib.Literal("Patch version"),
                "datatype": XSD.integer,
            },
        },
    },
}
