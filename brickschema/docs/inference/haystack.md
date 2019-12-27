# Haystack Inference

Examples for how to infer Brick models from existing Haystack modesl.
Requires a JSON export of a Haystack model

## Inferring a Brick Model from a Haystack Model

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
