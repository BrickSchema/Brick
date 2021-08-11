.PHONY: format

Brick.ttl: bricksrc/*.py bricksrc/*.ttl bricksrc/definitions.csv generate_brick.py
	mkdir -p extensions
	python generate_brick.py
	cd shacl && python generate_shacl.py

shacl/BrickShape.ttl: bricksrc/*.py generate_brick.py shacl/generate_shacl.py
	cd shacl && python generate_shacl.py

format:
	black generate_brick.py
	black shacl/
	black bricksrc/
	black tests/
	black tools/

test: Brick.ttl shacl/BrickShape.ttl
	pytest -s -vvvv -m 'not slow' tests
	cd tests/integration && bash run_integration_tests.sh

quantity-test: Brick.ttl
	pytest -s -vvvv tests/test_quantities.py

inference-test: Brick.ttl
	pytest -s -vvvv tests/test_inference.py

hierarchy-test: Brick.ttl
	pytest -s -vvvv tests/test_hierarchy_inference.py

measures-test: Brick.ttl
	pytest -s -vvvv tests/test_measures_inference.py
