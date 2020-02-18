.PHONY: format

Brick.ttl: bricksrc/*.py generate_brick.py
	python generate_brick.py

format:
	black generate_brick.py
	black bricksrc/
	black tests/
	black tools/

test: Brick.ttl
	pytest -s -vvvv tests

quantity-test: Brick.ttl
	pytest -s -vvvv tests/test_quantities.py

inference-test: Brick.ttl
	pytest -s -vvvv tests/test_inference.py

hierarchy-test: Brick.ttl
	pytest -s -vvvv tests/test_hierarchy_inference.py

measures-test: Brick.ttl
	pytest -s -vvvv tests/test_measures_inference.py
