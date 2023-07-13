import rdflib
from datetime import datetime
from bricksrc.namespaces import BRICK, SKOS, SH, XSD, RDFS, DCTERMS, RDF, SDO, OWL

DEMO = rdflib.Namespace("urn:demo_extension#")

ontology_definition = {
    "namespace": DEMO,
    DCTERMS.creator: [
        {
            RDF.type: SDO.Person,
            SDO.email: rdflib.Literal("gtfierro@mines.edu"),
            SDO.name: rdflib.Literal("Gabe Fierro"),
        },
    ],
    DCTERMS.issued: rdflib.Literal("2016-11-16"),
    DCTERMS.modified: rdflib.Literal(datetime.now().strftime("%Y-%m-%d")),
    DCTERMS.publisher: {
        RDF.type: SDO.Individual,
        SDO.legalName: rdflib.Literal("Gabe Fierro"),
        SDO.sameAs: rdflib.URIRef("https://gtf.fyi"),
    },
    OWL.versionInfo: rdflib.Literal("0.0.1"),
    RDFS.label: rdflib.Literal("Demo Extension"),
    DCTERMS.publisher: {
        RDF.type: SDO.Organization,
        SDO.legalName: rdflib.Literal("Not a real org"),
        SDO.sameAs: rdflib.Literal("http://my fake organization website.org"),
    },
    "imports": {
        "shacl": "http://www.w3.org/ns/shacl#",
    },
    "decls": [
        {
            SH.namespace: rdflib.Literal(str(RDF), datatype=XSD.anyURI),
            SH.prefix: rdflib.Literal("rdf"),
        },
        {
            SH.namespace: rdflib.Literal(str(RDFS), datatype=XSD.anyURI),
            SH.prefix: rdflib.Literal("rdfs"),
        },
        {
            SH.namespace: rdflib.Literal(str(BRICK), datatype=XSD.anyURI),
            SH.prefix: rdflib.Literal("brick"),
        },
        {
            SH.namespace: rdflib.Literal(str(OWL), datatype=XSD.anyURI),
            SH.prefix: rdflib.Literal("owl"),
        },
        {
            SH.namespace: rdflib.Literal(str(SH), datatype=XSD.anyURI),
            SH.prefix: rdflib.Literal("sh"),
        },
        {
            SH.namespace: rdflib.Literal(str(DEMO), datatype=XSD.anyURI),
            SH.prefix: rdflib.Literal("demo"),
        },
    ],
}

class_parent = BRICK.Equipment
classes = {
    DEMO["Sensor_Platform"]: {},
    DEMO["PurpleAir_Weather_Station"]: {
        "parents": [BRICK.Weather_Station],
    },
}


entity_properties = {
    DEMO.manufacturer: {
        SKOS.definition: rdflib.Literal("the manufacturer"),
        SH.datatype: XSD.string,
        RDFS.label: rdflib.Literal("manufacturer"),
        "property_of": BRICK.Equipment,
    },
    DEMO.version: {
        SKOS.definition: rdflib.Literal("a MAJOR.MINOR.PATCH versiion number"),
        SH.node: DEMO.VersionShape,
        RDFS.label: rdflib.Literal("version"),
        "property_of": BRICK.Equipment,
    },
}

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
