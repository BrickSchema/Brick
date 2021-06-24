from flask import Flask, request
from flask_jsonpify import jsonify
import json
from brickschema.namespaces import A
import brickschema
from rdflib import Namespace, URIRef
import re

from logging.config import dictConfig

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

app = Flask(__name__)

metadata = {
    "name": "Brick <-> VBIS Inference",
    "defaultTypes": [
        {"id": "BrickClass", "name": "BrickClass"},
        {"id": "VBISTag", "name": "VBISTag"},
    ],
}

g = brickschema.Graph().load_file("Brick-VBIS-alignment.ttl")

VBIS = Namespace("https://brickschema.org/schema/Brick/alignments/vbis#")
INP = Namespace("urn:input#")


def make_graph():
    g = brickschema.Graph(load_brick_nightly=True)
    g.load_file("Brick-VBIS-alignment.ttl")
    g.bind("vbis", VBIS)
    g.bind("inp", INP)

    return g


def resolve_queries(queries):
    results = {}
    g = make_graph()
    if len(queries) == 0:
        return results
    for qid, q in queries.items():
        inp = q.get("query", "")
        if q.get("type") == "BrickClass":
            g.add((INP[inp], VBIS.hasTag, VBIS[inp]))
        elif q.get("type") == "VBISTag":
            g.add((INP[inp], A, URIRef(inp)))
            print(INP[inp])
        results[qid] = {}
    app.logger.info(f"Added {len(queries)} items")

    app.logger.info("Reasoning...")
    g.expand("shacl")

    app.logger.info("Retrieving results")
    for qid, q in queries.items():
        inp = q.get("query", "")
        my_results = []
        if q.get("type") == "BrickClass":
            res = g.query(f"SELECT ?type WHERE {{ <{INP[inp]}> a ?type }}")
            classes = [x[0] for x in res]
            for cl in g.get_most_specific_class(classes):
                my_results.append(
                    {
                        "id": q["query"],
                        "name": cl,
                        "score": 1.0,
                        "match": True,
                        "type": [{"id": "BrickClass", "name": "BrickClass"}],
                    }
                )
        elif q.get("type") == "VBISTag":
            res = g.query(
                f"SELECT ?tag WHERE {{ <{INP[inp]}> vbis:hasTag ?x . ?x rdfs:label ?tag }}"
            )
            for r in [str(x[0]) for x in res]:
                my_results.append(
                    {
                        "id": q["query"],
                        "name": r,
                        "score": 1.0,
                        "match": True,
                        "type": [{"id": "VBISTag", "name": "VBISTag"}],
                    }
                )
        results[qid]["result"] = my_results

    print(results)
    return results


def resolve(q):
    """
    q has fields:
    - query: string of the label that needs to be converted to a Brick type
    - type: optional list of 'types' (e.g. "PointClass" above)
    - limit: optional limit on # of returned candidates (default to 10)
    - properties: optional map of property idents to values
    - type_strict: [any, all, should] for strictness on the types returned
    """
    # limit = int(q.get('limit', 10))

    inp = q.get("query", "")

    results = []
    if q.get("type") == "BrickClass":
        # get brickclass from vbis tag
        print("input:", inp)
        g = make_graph()
        g.add((INP[inp], VBIS.hasTag, VBIS[inp]))
        g.expand("shacl")
        res = g.query(f"SELECT ?type WHERE {{ <{INP[inp]}> a ?type }}")
        classes = [x[0] for x in res]
        for cl in g.get_most_specific_class(classes):
            results.append(
                {
                    "id": q["query"],
                    "name": cl,
                    "score": 1.0,
                    "match": True,
                    "type": [{"id": "BrickClass", "name": "BrickClass"}],
                }
            )
        pass
    elif q.get("type") == "VBISTag":
        g = make_graph()
        g.add((INP[inp], A, inp))
        g.expand("shacl")
        pass

    # most_likely, leftover = inf.most_likely_tagsets(brick_tags, limit)
    # for ml in most_likely:
    #     res.append({
    #         'id': q['query'],
    #         'name': ml,
    #         'score': (len(brick_tags) - len(leftover)) / len(brick_tags),
    #         'match': len(leftover) == 0,
    #         'type': [{"id": "PointClass", "name": "PointClass"}],
    #     })
    # print('returning', res)
    return results


@app.route("/reconcile", methods=["POST", "GET"])
def reconcile():
    if request.method == "GET":
        queries = json.loads(request.args.get("queries", "[]"))
    else:
        queries = json.loads(request.form.get("queries", "[]"))
    if queries:
        return jsonify(resolve_queries(queries))
    return jsonify(metadata)


if __name__ == "__main__":
    app.run()
