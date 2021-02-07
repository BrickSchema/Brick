"""Defines the timeseries reference model"""

from .namespaces import BRICK, A, OWL, SKOS, SH, XSD
from rdflib import Literal, BNode


def define_timeseries_model(G):
    """
    Adds the timeseries model definitions to the graph G
    """
    G.add((BRICK.TimeseriesReference, A, OWL.Class))
    G.add((BRICK.TimeseriesReference, A, SH.NodeShape))
    G.add(
        (
            BRICK.TimeseriesReference,
            SKOS.definition,
            Literal(
                "Metadata describing where and how the data for a Brick Point is stored"
            ),
        )
    )

    idprop = BNode()
    G.add((idprop, A, SH.PropertyShape))
    G.add((idprop, SH.path, BRICK.hasTimeseriesId))
    G.add((idprop, SH.minCount, Literal(1)))
    G.add((idprop, SH.maxCount, Literal(1)))
    G.add((idprop, SH.datatype, XSD.string))

    storedprop = BNode()
    G.add((storedprop, A, SH.PropertyShape))
    G.add((storedprop, SH.path, BRICK.storedAt))
    G.add((idprop, SH.maxCount, Literal(1)))
    # G.add((storedprop, SH.datatype, XSD.string))

    G.add((BRICK.TimeseriesReference, SH.property, idprop))
    G.add((BRICK.TimeseriesReference, SH.property, storedprop))
