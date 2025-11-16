# Contributing to Brick

Thank you for helping improve Brick. This document captures how we collaborate today, how to set up a working environment, and what we expect when you submit changes. Suggestions to improve these guidelines are always welcome via Pull Request (PR).

## Reporting Bugs and Issues in Brick

If you have a question about Brick or its related tools, it is recommended to make a post in the [Brick User Forum](https://groups.google.com/forum/#!forum/brickschema) or under the [Brick GitHub Issue Tracker](https://github.com/BrickSchema/Brick/issues). If you have a question about the website, please file the question either in the User Forum or on the [Brick Website Issue Tracker](https://github.com/BrickSchema/Brick/issues).

Please conduct a brief search to see if someone has asked your question already; if they have, feel free to jump into the conversation. Otherwise, please file a new issue or make a new post on the forum.

Bug reports are most helpful when they fully explain the problem and include as many details as possible.
Some suggestions:

- **Use a clear and descriptive title** for the issue that identifies the problem
- **Include as many details as possible** about the problem, including any relevant Brick/SPARQL queries, RDF triples, segments of Turtle files, Python code, etc
- **Describe the observed and expected behavior**: for example, what query did you run, what were the results, and what did you expect the results to be? What definition exists and what definition would you expect?
 - **Describe the exact steps to reproducing the problem** where it is appropriate: did you execute a query and

- Make sure you are using the most recent version of the Brick repository/ontology

## Proposing Changes to Brick

The content, structure and extent of Brick is determined by its community, so suggestions for how to improve Brick are always welcome and will be taken under consideration.
Proposed changes to Brick are tracked on the [Brick GitHub Issue Tracker](https://github.com/BrickSchema/Brick/issues).

Effective proposals should fully explain the motivation and scope of the proposed changes, and should have at least an initial impression of the nature of the implementation.
The more detail, the better!

## Submitting Changes to Brick

Changes to Brick are performed through [Pull Requests](https://github.com/BrickSchema/Brick/pulls).
It is recommended that you become familiar with how to [fork a repository](https://help.github.com/en/articles/fork-a-repo) and [create a pull request](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork).

# Development Workflow Overview

1. Fork `BrickSchema/Brick` and clone your fork.
2. Initialize submodules (for example RealEstateCore):
   ```bash
   git submodule update --init --recursive
   ```
3. Work with Python 3.11 or newer (the repo enforces `requires-python = ">= 3.11"` in `pyproject.toml`).
4. Use a virtual environment managed by **uv** (recommended) or standard `pip`. Both approaches install dependencies straight from `pyproject.toml`, so you do not need `requirements.txt`.
5. Run tests locally before opening a PR.

## Environment Setup

### Using uv (recommended)

1. Install uv by following https://docs.astral.sh/uv/ (macOS/Linux installer: `curl -LsSf https://astral.sh/uv/install.sh | sh`).
2. Ensure Python 3.11 is available (uv can install it with `uv python install 3.11`).
3. Sync dependencies directly from `pyproject.toml`/`uv.lock` (uv will create a managed `.venv` automatically):
   ```bash
   uv sync
   ```
4. Install pre-commit hooks without activating the venv by prefixing commands with `uv run`:
   ```bash
   uv run pre-commit install
   ```
5. When dependencies change, refresh the environment with `uv sync` so it stays aligned with the lockfile. You can run any project command through `uv run …` (for example `uv run python generate_brick.py`).

### Using pip (alternative)

These steps assume you are **not** using uv anywhere in your toolchain.

1. Verify Python 3.11 is available (for example `python3.11 --version`).
2. Create and activate a virtual environment:
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```
3. Install Brick in editable mode so you can iterate quickly:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -e .
   python -m pip install pre-commit
   pre-commit install
   ```

## Dependency Management (`pyproject.toml`)

`pyproject.toml` is the single source of truth for runtime and development requirements. When you need a new library:
- add it under `[project.dependencies]` (or the relevant optional extra) with an appropriate version range
- if the dependency is only for tooling/tests, consider creating an extra such as `.[dev]`
- run `uv lock` to refresh `uv.lock` so CI stays reproducible
- rerun `uv sync` (uv workflow) or `pip install -e .` (pip workflow) to pick up the new dependency
- mention the change in your PR description so reviewers know why it is needed

## Formatting, Linting, and Hooks

We use [`pre-commit`](https://pre-commit.com/) to run formatters and linters (Black, flake8, etc.) before every commit. After installing hooks (`pre-commit install` in your activated environment) you can manually check everything with `pre-commit run --all-files`. Commits should be free of formatting issues before you open a PR.

## Generating Artifacts and Running Tests

1. Regenerate ontology outputs whenever you touch ontological source files:
   ```bash
   python generate_brick.py
   ```
   or, if you prefer uv, `uv run python generate_brick.py`.
2. Run the pytest suite from the repository root so `Brick.ttl` and related artifacts are up to date:
   ```bash
   uv run pytest
   # or, after activating your pip environment:
   pytest
   ```
3. Tests live in `tests/` and may be parallelized thanks to `pytest-xdist`; keep them deterministic.
4. Please add or update tests whenever you change ontology behavior or Python utilities.

## Submitting Pull Requests

- Keep PRs focused; smaller changes are easier to review.
- Ensure `git status` is clean, tests pass, and hooks succeed before pushing.
- Fill out the PR template with context, testing evidence, and any migration notes.
- Respond promptly to review comments; collaborative discussion is encouraged.

## Extending the Ontology Programmatically

The Brick class hierarchy lives inside `bricksrc/`. Each file contains nested dictionaries describing a slice of the hierarchy. Follow these placement guidelines:
- Point subclasses (`Command`, `Sensor`, `Setpoint`, `Status`) belong in their respective `bricksrc/<class>.py` files.
- `Equipment` definitions go in `bricksrc/equipment.py`.
- `Location`, `Parameter`, `Quantity`, and `Substance` classes go in their similarly named modules.

Definitions use the following structure:

```python
{
    "Sensor": {
        "tags": [TAG.Sensor],
        "subclasses": {
            "Air_Grains_Sensor": {
                "tags": [TAG.Sensor, TAG.Air, TAG.Grains],
                "substances": [[BRICK.measures, BRICK.Air], [BRICK.measures, BRICK.Grains]],
                "subclasses": {
                    "Outside_Air_Grains_Sensor": {
                        "tags": [TAG.Outside, TAG.Air, TAG.Grains, TAG.Sensor],
                    },
                    "Return_Air_Grains_Sensor": {
                        "tags": [TAG.Return, TAG.Air, TAG.Grains, TAG.Sensor],
                    },
                },
            }
        }
    }
}
```

Guidelines:
- Class names are Camel_Case strings with `_` separators.
- `tags` combine Brick tag constants; an entity that has all tags will be inferred as the class.
- Use `parents` to share ancestry without duplicating structures.
- `substances` entries look like `[BRICK.measures, BRICK.<Substance>]` and must match definitions in `bricksrc/substances.py`.

To add textual descriptions, edit `bricksrc/definitions.csv` and insert a row with the full Brick URI, a human-readable definition (quote it if it contains commas), and an optional citation. Keep the file alphabetized.

## Need Help?

When in doubt:
- start a discussion in the Brick User Forum
- tag relevant maintainers in an issue or PR
- open a draft PR early so maintainers can guide the direction
