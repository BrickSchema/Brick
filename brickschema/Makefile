.PHONY: test docs

test:
	pytest -s -vvvv tests/

docs:
	mkdocs build -d built-docs
	pdoc3 --html -o built-docs --force brickschema
