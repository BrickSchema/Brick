# Brick Ontology Python package

## Installation

The `brickschema` package requires Python >= 3.6. It can be installed with `pip`:

```
pip install brickschema
```

## Haystack Inference

Requires a JSON export of a Haystack model
First, export your Haystack model as JSON; we are using the public reference model `carytown.json`.
Then you can use this package as follows:

```python
import json
from brickschema.inference import HaystackInferenceSession
haysess = HaystackInferenceSession("http://project-haystack.org/carytown#")
model = json.load(open('carytown.json'))
model = haysess.infer_model(model)
print(len(model))

points = model.query("""SELECT ?point ?type WHERE {
    ?point rdf:type/rdfs:subClassOf* brick:Point .
    ?point rdf:type ?type
}""")
print(points)
```

## SQL ORM

```python
from brickschema.graph import Graph
from brickschema.namespaces import BRICK
from brickschema.orm import SQLORM, Location, Equipment, Point

# loads in default Brick ontology
g = Graph(load_brick=True)
# load in our model
g.load_file("test.ttl")
# put the ORM in a SQLite database file called "brick_test.db"
orm = SQLORM(g, connection_string="sqlite:///brick_test.db")

# get the points for each equipment
for equip in orm.session.query(Equipment):
    print(f"Equpiment {equip.name} is a {equip.type} with {len(equip.points)} points")
    for point in equip.points:
        print(f"    Point {point.name} has type {point.type}")
# filter for a given name or type
hvac_zones = orm.session.query(Location)\
                        .filter(Location.type==BRICK.HVAC_Zone)\
                        .all()
print(f"Model has {len(hvac_zones)} HVAC Zones")
```
