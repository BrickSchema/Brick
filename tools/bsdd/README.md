# Brick → bSDD export

Generates the JSON import file that publishes Brick as a dictionary in the
[buildingSMART Data Dictionary](https://technical.buildingsmart.org/services/bsdd/).

bSDD accepts a dictionary only as a single JSON document — content cannot be
uploaded in parts — so the whole dictionary is derived from the built ontology
on every run, and never hand-edited.

## Usage

```bash
make Brick.ttl                                   # Brick+imports.ttl must exist
python tools/bsdd/generate_bsdd.py               # writes bsdd/brick-bsdd.json + bsdd/report.md
pytest tests/test_bsdd_export.py                 # validates the result
```

| Option | Effect |
|---|---|
| `--output PATH` | Where to write the JSON (default `bsdd/brick-bsdd.json`). |
| `--report PATH` | Where to write the Markdown report (default `report.md` beside the output). |
| `--uri-style {canonical,versioned}` | Whether `OwnedUri` carries the Brick version. |
| `--organization-code CODE` | bSDD organisation. Use `DEMO` for test uploads. |
| `--include-deprecated` | Also export the 186 deprecated terms, with their mitigation messages. |
| `--refresh-units` | Rebuild `mappings/units.csv` from the bSDD unit API, then exit. |
| `--source PATH` | Ontology to read (default `Brick+imports.ttl`). |

Read `bsdd/report.md` after every run. It records what was dropped, merged or
left incomplete, including defects it found in Brick itself.

## What maps to what

`Brick+imports.ttl` is the source, not `Brick.ttl`: REC classes arrive through
`owl:imports` declared as `rdfs:Class`, and Brick's own `brick:Location` subtree
is entirely deprecated in favour of them. Reading `Brick.ttl` alone would produce
a dictionary with no rooms or spaces at all.

### Classes

1,274 live Brick classes plus the 126-class REC location closure
(`rec:Space`, `rec:Architecture`, `rec:Collection`, `rec:Building` and their
subclasses). REC's other branches are excluded: `*Observation` duplicates Brick
Points, and `Asset`/`Agent`/furniture fall outside a building-metadata dictionary.

| Brick | bSDD |
|---|---|
| IRI local name | `Code` |
| `rdfs:label`@en | `Name` |
| `skos:definition`, else `rdfs:comment` | `Definition` |
| primary `rdfs:subClassOf` | `ParentClassCode` |
| remaining named superclasses | `ClassRelations` → `IsChildOf` |
| `owl:equivalentClass` | `Synonyms` + `ClassRelations` → `IsEqualTo` |
| `brick:deprecationMitigationMessage` | `DeprecationExplanation` |
| `brick:isReplacedBy` | `ReplacingObjectCodes` |
| `mappings/ifc.csv` | `RelatedIfcEntityNamesList` |

bSDD permits a single `ParentClassCode`, but 226 classes have more than one named
superclass. The deepest parent stays in the tree — it is the most specific — and
the rest become `IsChildOf` relations, so no edge is lost. The report lists every
such resolution.

Per-class `Status` is deliberately never set: the bSDD guidelines say status
inherits from the dictionary.

REC classes receive Brick dictionary-owned URIs under `#class/rec/` because
`UseOwnUri` requires every owned URI to begin with `DictionaryUri`. Each carries
a `HasReference` relation back to its authoritative `https://w3id.org/rec#...`
identifier.

### Properties

- **Entity properties** (51) — constraints come from the SHACL value shape reached
  via `sh:path` → `sh:node`, which constrains `brick:value` and `brick:hasUnit`.
  `sh:in` on the value becomes `AllowedValues` (the EV connector and charger
  types, `currentFlowType`, `buildingPrimaryFunction`, …); `sh:or bsh:NumericValue`
  becomes `Real`; `sh:datatype` maps directly.
- **Quantities** (`brick:Quantity` plus the QUDT quantity kinds Points reference)
  — `qudt:applicableUnit` becomes `Units`, and QUDT's dimension vector converts to
  bSDD's `Dimension`.
- **Substance** — one enumerated property whose 96 `AllowedValues` are the Brick
  substance concepts, ordered by a walk of `skos:broader` so related substances
  stay adjacent.

Classes link to properties through `ClassProperty`: `brick:hasQuantity` (what a
Point measures), `brick:hasSubstance` (what it observes, as a `PredefinedValue`),
and SHACL property shapes for entity properties.

Every property receives a dictionary-owned URI under `#property/`. This separate
namespace avoids collisions with classes such as `brick:Substance` and gives
merged properties one stable identifier even when they derive from multiple RDF
terms.

### Substances are not materials

A substance in Brick is **what is observed, not what something is made of** —
`brick:Substance` is `rdfs:subClassOf sosa:FeatureOfInterest`. `ClassType:
Material` and the `HasMaterial` relation both mean composition, so neither is ever
emitted; `tests/test_bsdd_export.py::test_no_material_semantics` guards this.

The RDF rules it out independently: the 96 substances are *instances* of
`brick:Substance` organised by `skos:broader`, not classes, so they could not be
emitted as classes even if the semantics fit.

### Relationships that are not exported

bSDD's `ClassRelation` vocabulary is closed, and most Brick relationships have no
equivalent in it. `feeds`, `hasPoint`, `hasLocation`, `controls`, `isMeteredBy` and
the rest are dropped rather than forced into `HasReference`, which REL-03 reserves
for genuinely referential links. The report lists them so the omission is explicit.

## Mapping files

- **`mappings/units.csv`** — `qudt_uri, bsdd_code, source`. Built by joining Brick's
  QUDT units against the bSDD unit API, which publishes a `qudtUri` for many of its
  entries. Coverage is partial (118 of 671), so rows marked `source=manual` are
  curated by hand and survive `--refresh-units`. Units bSDD does not know are
  omitted from the output and listed in the report; file them as
  [bSDD issues](https://github.com/buildingSMART/bSDD/issues) to have them added.
- **`mappings/ifc.csv`** — `code, ifc_entities, note`. Curated by hand: Brick has no
  IFC alignment to derive this from. Only concrete IFC entities, never abstract
  ones (CLS-01). 93 curated rows, reaching 711 classes by inheritance; extend it
  incrementally. Entity names are checked against `reference/ifc-4.3-classes.csv`
  and anything unrecognised is listed in the report.

### IFC entities are inherited

A curated row applies to the class's subclasses and equivalents too. `Fan` is
curated as `IfcFan`, and every Brick fan is an IfcFan, so all thirteen
descendants carry it without a row of their own. This is what takes CLS-01
coverage from 93 curated rows to 711 classes; the report lists how many classes
each curated row reaches.

Two details make it safe. A class with its own row always keeps it, so `Coil`
stays `IfcCoil` instead of taking `IfcHeatExchanger` from its parent — that is
how a subclass overrides a parent whose entity is only approximately right. And
`owl:equivalentClass` is followed as well as `rdfs:subClassOf`, because Brick's
abbreviations (`AHU`, `VAV`, `HX`) are equivalent to their spelled-out forms but
sit under a generic parent, so subclass inheritance alone would never reach them.

No Brick class currently inherits conflicting entities through its multiple
parents. If one ever does, the entity from the deepest origin wins — the most
specific claim, matching how `ParentClassCode` resolves multiple inheritance —
and the report names the class.

Points are the natural limit. IFC models physical products, not telemetry, so
setpoints, commands and statuses inherit nothing; sensors are the exception,
since `IfcSensor` is a real device. Of the 689 classes still without an entity,
552 are Points.

## Reference data

`reference/ifc-4.3-classes.csv` is the vocabulary `mappings/ifc.csv` has to draw
from — every class in buildingSMART's own IFC 4.3 dictionary
(`https://identifier.buildingsmart.org/uri/buildingsmart/ifc/4.3`, released
2024-01-11, the ISO 16739-1:2024 schema), with full definitions. An entity name
absent from it will not resolve when Brick is published alongside IFC in bSDD.

Rebuild it with `python tools/bsdd/fetch_ifc_dictionary.py`. The run takes a few
minutes: bSDD's bulk listing truncates every definition at 101 characters, so the
730 long ones are re-fetched one class at a time.

| Column | |
|---|---|
| `code` | IFC entity name, e.g. `IfcChiller` |
| `name` | bSDD display name, e.g. `Chiller` |
| `class_type` | `Class`; `GroupOfProperties` only with `--include-property-sets` |
| `parent_code` | IFC supertype, or the base entity for a predefined type |
| `predefined_type` | set only on predefined-type rows |
| `definition` | IFC documentation text, verbatim (`[[…]]` cross-references included) |

1,418 rows: 239 base entities and 1,179 predefined types. IFC's predefined types
are published as classes in their own right (`IfcChillerAIRCOOLED`), and Brick's
equipment classes frequently align with one of those rather than with the bare
entity — but `RelatedIfcEntityNamesList` takes **entity names only**, so a
predefined type belongs in the `note` column, as the existing rows do it.

The 239 base entities include IFC's abstract supertypes (`IfcElement`,
`IfcProduct`, `IfcDistributionFlowElement`, `IfcFlowController`, `IfcRoot`, …),
so the file does not settle CLS-01's "concrete entities only" rule on its own —
bSDD carries no abstract flag. Checking that automatically needs the `ABSTRACT
SUPERTYPE` declarations from the IFC 4.3 EXPRESS schema.

## Uploading

1. **Register the organisation.** Every dictionary publishes on behalf of a
   registered bSDD organisation, and bSI reviews each request by hand. Until
   Brick's own code exists, run test uploads under bSI's `DEMO` organisation:
   `--organization-code DEMO`.
2. Go to the [bSDD management portal](https://manage.bsdd.buildingsmart.org/) and
   upload with **"Validate only?"** checked. Fix anything it reports.
3. Upload again as a **"Test upload"** — that content is deleted automatically
   after two months and cannot be activated, so it is safe. A detailed import
   report arrives by email within about 15 minutes.

**Do not activate.** Activation is irreversible: the content receives an immutable
URI and can never be deleted, only marked `Inactive`. The generator always emits
`Status: Preview`; activation is a deliberate manual step.

One question the bSDD documentation does not answer, to settle with a
validate-only upload:

- whether bSDD accepts the same `OwnedUri` reappearing in a later dictionary
  version. If it demands uniqueness, make `--uri-style versioned` the default.

## Known gaps

Two verification items cannot be closed from this script:

- **CLS-01** — `RelatedIfcEntityNamesList` is empty for 689 of 1,400 classes, of
  which 552 are Points that have no IFC counterpart by design. The 110 unmapped
  equipment classes are the real remaining surface, and most name things IFC
  lacks outright (fan-coil variants, condensing units, plenums, CRAC/CRAH);
  extend `mappings/ifc.csv`, drawing names from `reference/ifc-4.3-classes.csv`.
- **GEN-01** — 463 classes ship without a definition (354 Brick, 109 REC). Fix
  these upstream in `bricksrc/definitions.csv` and in REC.

`GEN-12` expects an own URI to resolve to a page carrying the term's name and
definition. `https://brickschema.org/schema/Brick#X` currently serves the whole
ontology as `application/octet-stream`, while
`https://ontology.brickschema.org/brick/X.html` returns real HTML — closing this
properly means content negotiation on `brickschema.org`.

## Attribution

The REC location terms come from [RealEstateCore](https://www.realestatecore.io/),
which is BSD-3-Clause licensed (see `rec/LICENSE`, Copyright (c) 2022
RealEstateCore Consortium). Redistribution is permitted with that notice. Give the
RealEstateCore Consortium notice before publishing: the bSDD guidelines discourage
republishing another dictionary's content, and REC may prefer to publish its own.
