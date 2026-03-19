from rdflib import Literal
from .namespaces import A, OWL, RDFS, BRICK, VCARD, QUDT, SDO, RDF, BSH, XSD, REC, SH
from .env import env

"""
Defining Brick relationships
"""
relationships = {
    "isReplacedBy": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.label: Literal("Is replaced by", lang="en"),
        "range": BRICK.Entity,
        "domain": BRICK.Entity,
    },
    "hasSubstance": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.label: Literal("Has Substance", lang="en"),
        "range": BRICK.Substance,
        "domain": [BRICK.Point, BRICK.Meter],
    },
    "hasQuantity": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.label: Literal("Has Quantity", lang="en"),
        RDFS.subPropertyOf: QUDT.hasQuantityKind,
        "range": [BRICK.Quantity, QUDT.QuantityKind],
        "domain": BRICK.Point,
    },
    "value": {
        RDFS.subPropertyOf: QUDT.value,
        RDFS.label: Literal("Value", lang="en"),
        A: [RDF.Property],
        "range": RDFS.Resource,
        "domain": RDFS.Resource,
    },
    "latitude": {
        RDFS.subPropertyOf: SDO.latitude,
        RDFS.label: Literal("Latitude", lang="en"),
        "domain": BRICK.Entity,
        "datatype": BSH.NumericValue,
    },
    "longitude": {
        RDFS.subPropertyOf: SDO.longitude,
        RDFS.label: Literal("Longitude", lang="en"),
        "domain": BRICK.Entity,
        "datatype": BSH.NumericValue,
    },
    "timestamp": {
        RDFS.label: Literal("Timestamp", lang="en"),
        A: [RDF.Property],
        "domain": BRICK.Entity,
        "datatype": XSD.dateTime,
    },
    "hasQUDTReference": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        RDFS.label: Literal("Has QUDT reference", lang="en"),
        "domain": BRICK.Quantity,
        "range": QUDT.QuantityKind,
    },
    "isLocationOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasLocation"],
        "domain": [BRICK.Location, REC.Architecture],
        "range": BRICK.Entity,
        RDFS.label: Literal("Is location of", lang="en"),
    },
    "hasLocation": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isLocationOf"],
        "domain": BRICK.Entity,
        "range":[BRICK.Location, REC.Architecture],
        RDFS.label: Literal("Has location", lang="en"),
    },
    "hasInputSubstance": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "range": BRICK.Substance,
        "domain": BRICK.Equipment,
        RDFS.label: Literal("Has input substance", lang="en"),
    },
    "hasOutputSubstance": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "range": BRICK.Substance,
        "domain": BRICK.Equipment,
        RDFS.label: Literal("Has output substance", lang="en"),
    },
    "feeds": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isFedBy"],
        RDFS.label: Literal("Feeds", lang="en"),
    },
    "isFedBy": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["feeds"],
        RDFS.label: Literal("Is fed by", lang="en"),
    },
    "hasPoint": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isPointOf"],
        "range": BRICK.Point,
        "domain": [BRICK.Equipment, BRICK.Location, REC.Architecture],
        RDFS.label: Literal("Has point", lang="en"),
    },
    "isPointOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasPoint"],
        "domain": BRICK.Point,
        "range": [
            BRICK.Equipment,
            BRICK.Location,
            REC.Architecture
        ],
        RDFS.label: Literal("Is point of", lang="en"),
    },
    "hasPart": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isPartOf"],
        RDFS.label: Literal("Has part", lang="en"),
    },
    "isPartOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasPart"],
        RDFS.label: Literal("Is part of", lang="en"),
    },
    "hasTag": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isTagOf"],
        "range": BRICK.Tag,
        "domain": OWL.Class,
        RDFS.label: Literal("Has tag", lang="en"),
    },
    "isTagOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "domain": BRICK.Tag,
        "range": [BRICK.Entity, BRICK.Measurable],
        RDFS.label: Literal("Is tag of", lang="en"),
    },
    "hasAssociatedTag": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isAssociatedWith"],
        "domain": OWL.Class,
        "range": BRICK.Tag,
        RDFS.label: Literal("Has associated tag", lang="en"),
    },
    "isAssociatedWith": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hasAssociatedTag"],
        "domain": BRICK.Tag,
        "range": OWL.Class,
        RDFS.label: Literal("Is associated with", lang="en"),
    },
    "hasAddress": {
        RDFS.subPropertyOf: VCARD.hasAddress,
        "domain": BRICK.Building,
        "range": VCARD.Address,
        RDFS.label: Literal("Has address", lang="en"),
    },
    "hasUnit": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "range": QUDT.Unit,
        "domain": BRICK.Point,
        RDFS.label: Literal("Has unit", lang="en"),
    },
    "controls": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isControlledBy"],
        "range": BRICK.Equipment,
        "domain": BRICK.Controller,
        RDFS.label: Literal("Controls", lang="en"),
    },
    "isControlledBy": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["controls"],
        "range": BRICK.Controller,
        "domain": BRICK.Equipment,
        RDFS.label: Literal("Is controlled by", lang="en"),
    },
    "hosts": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["isHostedBy"],
        "range": BRICK.Point,
        "domain": BRICK.ICT_Equipment,
        RDFS.label: Literal("Hosts point", lang="en"),
    },
    "isHostedBy": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK["hosts"],
        "range": BRICK.ICT_Equipment,
        "domain": BRICK.Point,
        RDFS.label: Literal("Is hosted by", lang="en"),
    },
    "meters": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK.isMeteredBy,
        "domain": BRICK.Meter,
        # this is a special property that implements the 'range' as a SHACL shape
        "range": [BRICK.Equipment, BRICK.Location, BRICK.Collection, REC.Architecture],
        RDFS.label: Literal("meters", lang="en"),
    },
    "isMeteredBy": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK.meters,
        # this is a special property that implements the 'domain' as a SHACL shape
        "domain": [BRICK.Equipment, BRICK.Location, BRICK.Collection, REC.Architecture],
        "range": BRICK.Meter,
        RDFS.label: Literal("is metered by", lang="en"),
    },
    "hasSubMeter": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK.isSubMeterOf,
        "range": BRICK.Meter,
        "domain": BRICK.Meter,
        RDFS.label: Literal("has sub-meter", lang="en"),
    },
    "isSubMeterOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        OWL.inverseOf: BRICK.hasSubMeter,
        "range": BRICK.Meter,
        "domain": BRICK.Meter,
        RDFS.label: Literal("is sub-meter of", lang="en"),
    },
    "hasAmbientTemperature": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
    },
    "aliasOf": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "range": BRICK.Entity,
        "domain": BRICK.Entity,
    },
    "deprecation": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "range": [BSH.DeprecationRule],
    },
    "deprecationMitigationMessage": {
        A: [OWL.DatatypeProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "range": XSD.string,
    },
    "deprecatedInVersion": {
        A: [OWL.DatatypeProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "range": XSD.string,
    },
    "deprecationMitigationRule": {
        A: [OWL.ObjectProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
        "range": [SH.PropertyShape],
    },
    "aggregationFunction": {
        A: [OWL.DatatypeProperty, OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
    },
    "ambientTemperatureOfMeasurement": {
        A: [OWL.AsymmetricProperty, OWL.IrreflexiveProperty],
    },
}

# add REC relationships by mining them from the REC ontology
rec = env.get_graph("https://w3id.org/rec")
# for all objects of sh:path, read out the sh:nodeKind and sh:datatype
query = """SELECT ?path ?nodeKind ?datatype WHERE {
    ?p sh:path ?path .
    OPTIONAL { ?p sh:nodeKind ?nodeKind }
    OPTIONAL { ?p sh:datatype ?datatype }
}"""
for row in rec.query(query):
    if row["path"] not in relationships:
        relationships[row["path"]] = {}
    if row["datatype"]:
        relationships[row["path"]][A] = [OWL.DatatypeProperty]
    if row["nodeKind"]:
        relationships[row["path"]][A] = [
            OWL.ObjectProperty,
            OWL.AsymmetricProperty,
            OWL.IrreflexiveProperty,
        ]
