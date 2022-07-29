import pytest
import rdflib
from rdflib.namespace import OWL, RDF, RDFS
from rdflib import Graph, URIRef
import json
import brickschema
import sys
from collections import defaultdict

sys.path.append("..")

from bricksrc.version import BRICK_VERSION  # noqa: E402
from bricksrc.namespaces import BRICK  # noqa: E402


def getDict(g, q):

    d = defaultdict(list)

    res = g.query(q)

    for row in res:
        c1 = row.c.toPython().replace("https://brickschema.org/schema/Brick#", "")
        if row.p:
            c2 = row.p.toPython().replace("https://brickschema.org/schema/Brick#", "")
            d[c1].append(c2)

    return d


def matchMinMax(d):
    ds = {}
    ds["MissingMatchingMin"] = []
    ds["MissingMatchingMax"] = []
    ds["AllGood"] = []
    dislist = []
    countmatch = 0
    countobutnotu = 0
    countubutnoto = 0
    for c in d:
        if "Min" in c:
            s = c.replace("Min", "Max")
            if s in d:
                # print('debug:',s,e[s])
                ds["AllGood"].append((s, c))
                countmatch += 1
                dislist.append(c)
            else:
                ds["MissingMatchingMax"].append(c)
                dislist.append(c)
                countobutnotu += 1
    for c in d:
        if "Max" in c:
            dis = c.replace("Max", "Min")
            if dis in dislist:
                pass
            else:
                ds["MissingMatchingMin"].append(c)
                countubutnoto += 1
    # print(json.dumps(ds,indent=4),file=open('tests/mm.json','w'))
    assert not ds[
        "MissingMatchingMin"
    ], "There are {0} classes that have Max but not Min".format(
        len(ds["MissingMatchingMin"])
    )
    assert not ds[
        "MissingMatchingMax"
    ], "There are {0} classes that have Min but not Max".format(
        len(ds["MissingMatchingMax"])
    )


def matchOccupiedUnoccupied(d):
    ds = {}
    ds["MissingMatchingOccupied"] = []
    ds["MissingMatchingUnoccupied"] = []
    ds["AllGood"] = []
    dislist = []
    countmatch = 0
    countobutnotu = 0
    countubutnoto = 0
    for c in d:
        if "Occupied" in c:
            s = c.replace("Occupied", "Unoccupied")
            if s in d:
                # print('debug:',s,e[s])
                ds["AllGood"].append((s, c))
                countmatch += 1
                dislist.append(c)
            else:
                ds["MissingMatchingUnoccupied"].append(c)
                dislist.append(c)
                countobutnotu += 1
    for c in d:
        if "Unoccupied" in c:
            dis = c.replace("Unoccupied", "Occupied")
            if dis in dislist:
                pass
            else:
                ds["MissingMatchingOccupied"].append(c)
                countubutnoto += 1

    # print(json.dumps(ds,indent=4),file=open('tests/uo.json','w'))
    assert not ds[
        "MissingMatchingOccupied"
    ], "There are {0} classes that have Unoccupied but not Occupied".format(
        len(ds["MissingMatchingOccupied"])
    )
    assert not ds[
        "MissingMatchingUnoccupied"
    ], "There are {0} classes that have Occupied but not Unoccupied".format(
        len(ds["MissingMatchingUnoccupied"])
    )


def matchSupplyDischarge(d, e):
    ds = {}
    ds["MissingMatchingDischarge"] = []
    ds["MissingMatchingSupply"] = []
    ds["NoEquivalenceDefined"] = {}
    ds["AllGood"] = {}
    dislist = []
    countmatch = 0
    countdbutnots = 0
    countsbutnotd = 0
    for c in d:
        if "Discharge" in c:
            s = c.replace("Discharge", "Supply")
            if s in d:
                if s in e:
                    # print('debug:',s,e[s])
                    if c in e[s]:
                        pass
                    else:
                        print("*ERROR* ", s, e[s])
                    ds["AllGood"][c] = s
                elif c in e:
                    if s in e[c]:
                        pass
                    else:
                        print("*ERROR* ", c, e[c])
                    ds["AllGood"][c] = s
                else:
                    ds["NoEquivalenceDefined"][c] = s
                countmatch += 1
                dislist.append(c)
            else:
                ds["MissingMatchingSupply"].append(c)
                dislist.append(c)
                countdbutnots += 1
    for c in d:
        if "Supply" in c:
            dis = c.replace("Supply", "Discharge")
            if dis in dislist:
                pass
            else:
                ds["MissingMatchingDischarge"].append(c)
                countsbutnotd += 1

    # print(json.dumps(ds,indent=4),file=open('tests/ds.json','w'))
    assert not ds[
        "MissingMatchingSupply"
    ], "There are {0} classes that have Discharge but not Supply".format(
        len(ds["MissingMatchingSupply"])
    )
    assert not ds[
        "MissingMatchingDischarge"
    ], "There are {0} classes that have Supply but not Discharge".format(
        len(ds["MissingMatchingDischarge"])
    )
    assert not ds[
        "NoEquivalenceDefined"
    ], "There are {0} classes that don't have Supply = Discharge defined".format(
        len(ds["NoEquivalenceDefined"])
    )


# maincode
def test_matching_classes():
    g = Graph()

    g.parse("Brick.ttl", format="turtle")
    # DeductiveClosure(OWLRL_Semantics).expand(g)

    d = getDict(
        g,
        """
       SELECT DISTINCT ?c ?p
       WHERE {
           ?c rdfs:subClassOf* brick:Class .
           ?c rdfs:subClassOf ?p .
           ?p rdfs:subClassOf* brick:Class .
           FILTER NOT EXISTS { ?c owl:deprecated true } .
           FILTER NOT EXISTS { ?p owl:deprecated true } .
       }
       """,
    )

    print("verifying min max classes...")
    matchMinMax(d)
    print("verifying occupied unoccupied classes...")
    matchOccupiedUnoccupied(d)

    deq = getDict(
        g,
        """
       SELECT DISTINCT ?c ?p
       WHERE {
           ?c rdfs:subClassOf* brick:Class .
           FILTER NOT EXISTS { ?c owl:deprecated true } .
           OPTIONAL {
           ?c owl:equivalentClass ?p .
           } .
       }
       """,
    )
    print("verifying supply discharge classes...")
    matchSupplyDischarge(d, deq)
