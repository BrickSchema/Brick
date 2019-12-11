# Brick Ontology Python package


## Inferring a Brick Model from a Haystack Model

First, export your Haystack model as JSON; we are using the public reference model `carytown.json`.
Then you can use this package as follows:

```python
import json
from brickschema.inference import HaystackInferenceSession
haysess = HaystackInferenceSession()
model = json.load(open('carytown.json'))
model = haysess.infer_model(model, "http://project-haystack.org/carytown#")
print(len(model))

points = model.query("""SELECT ?point ?type WHERE { 
    ?point rdf:type/rdfs:subClassOf* brick:Point .
    ?point rdf:type ?type
}""")
print(points)
```
