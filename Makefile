.PHONY: format

# TEMPORARY: REC's checked-in SHACL Turtle (rec/Source/SHACL/RealEstateCore/rec.ttl) lags
# its DTDL source. Until REC regenerates that Turtle, we run a Python port of
# REC's DTDL2SHACL and merge in only the terms the Turtle is missing. Remove this rule, the
# prerequisite below and tools/dtdl2shacl.py once REC's Turtle catches up.
REC_DTDL_SUPPLEMENT = bricksrc/rec-dtdl-supplement.ttl
REC_DTDL_SOURCES = $(shell find rec/Source/DTDLv2 -name '*.json' 2>/dev/null)

$(REC_DTDL_SUPPLEMENT): tools/dtdl2shacl.py rec/Source/SHACL/DtmiNamespaceMappings.csv rec/Source/SHACL/RealEstateCore/rec.ttl $(REC_DTDL_SOURCES)
	python tools/dtdl2shacl.py -i rec/Source/DTDLv2 \
		-n rec/Source/SHACL/DtmiNamespaceMappings.csv \
		--map "dtmi:org:brickschema:schema:Brick:,https://brickschema.org/schema/Brick#,brick" \
		--supplement-for rec/Source/SHACL/RealEstateCore/rec.ttl \
		-o $@

Brick.ttl: bricksrc/*.py bricksrc/*.ttl bricksrc/definitions.csv generate_brick.py support/*.ttl validation.ttl $(REC_DTDL_SUPPLEMENT)
	mkdir -p extensions
	python tools/sort_definitions.py bricksrc/definitions.csv
	python generate_brick.py
	python handle_extensions.py

clean:
	rm -f $(REC_DTDL_SUPPLEMENT)
	rm -r Brick.ttl Brick+extensions.ttl imports/ .ontoenv

format:
	black generate_brick.py
	black handle_extensions.py
	black bricksrc/
	black tests/
	black tools/

test: Brick.ttl
	pytest -s -vvvv  -n auto tests

quantity-test: Brick.ttl
	pytest -s -vvvv tests/test_quantities.py

inference-test: Brick.ttl
	pytest -s -vvvv tests/test_inference.py

hierarchy-test: Brick.ttl
	pytest -s -vvvv tests/test_hierarchy_inference.py

measures-test: Brick.ttl
	pytest -s -vvvv tests/test_measures_inference.py

matches-test: Brick.ttl
	pytest -s -vvvv tests/test_matching_classes.py
