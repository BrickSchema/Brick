# Brick → bSDD export

```bash
make Brick.ttl
python tools/bsdd/generate_bsdd.py
pytest tests/test_bsdd_export.py
```

The exporter creates one bSDD JSON dictionary from `Brick+imports.ttl`.

| Brick source | bSDD output |
| --- | --- |
| live Brick class | Class (`Code`, `Name`, `Definition`, parent) |
| quantity or `brick:hasQuantity` target | numeric Property (`Units`, `Dimension`) |
| `brick:EntityProperty` SHACL value shape | scalar Property |
| multi-field EntityProperty shape | `Complex` Property with `ConnectedPropertyCodes` |
| `brick:hasQuantity`, `brick:hasSubstance`, SHACL class property | `ClassProperty` |

Complex children use `parent.field` codes, such as `coordinates.latitude`.
Imported vocabularies and deprecated Brick terms are not published.

`mappings/units.csv` maps QUDT unit IRIs to bSDD unit codes. The export is
offline and deterministic. IFC alignment and other publication-quality checks
deliberately do not alter the mapping.

Property codes are case-insensitive in bSDD. A collision stops the export; add
an explicit mapping decision rather than silently merging distinct Brick terms.
