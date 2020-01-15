Brick.ttl: bricksrc/*.py generate_brick.py
	python generate_brick.py

test: Brick.ttl
	pytest -s -vvvv tests

quantity-test: Brick.ttl
	pytest -s -vvvv tests/test_quantities.py
	$(shell python get_unsatisfiable.py output.ttl | sort > unsat)
