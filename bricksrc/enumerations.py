from rdflib import Literal
from .namespaces import RDFS

enumeration_definitions = {
    "TriggerDirection": {
        RDFS.comment: Literal(
            "Enumerates the direction a measured value crosses a threshold to trigger an action.",
            lang="en",
        ),
        "subclasses": {
            "TriggerDirection-Rising": {
                RDFS.comment: Literal(
                    "The threshold is triggered when the measured value rises above it.",
                    lang="en",
                ),
                "subclasses": {
                    "TriggerDirection-Cooling": {
                        RDFS.comment: Literal(
                            "A rising trigger associated with cooling: cooling begins when "
                            "the measured value rises above the threshold.",
                            lang="en",
                        ),
                    },
                },
            },
            "TriggerDirection-Falling": {
                RDFS.comment: Literal(
                    "The threshold is triggered when the measured value falls below it.",
                    lang="en",
                ),
                "subclasses": {
                    "TriggerDirection-Heating": {
                        RDFS.comment: Literal(
                            "A falling trigger associated with heating: heating begins when "
                            "the measured value falls below the threshold.",
                            lang="en",
                        ),
                    },
                },
            },
        },
    },
}
