.PHONY: format

Brick.ttl: bricksrc/*.py bricksrc/*.ttl bricksrc/definitions.csv generate_brick.py support/*.ttl validation.ttl
	mkdir -p extensions
	python tools/sort_definitions.py bricksrc/definitions.csv
	python generate_brick.py
	python handle_extensions.py

clean:
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
