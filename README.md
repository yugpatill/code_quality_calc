![CI](https://github.com/kaw393939/code_quality_calc/actions/workflows/quality.yml/badge.svg?branch=main)

# Basic Calculator — Professional Python Project Template

This repo is a tiny calculator used to teach professional Python practices: clean structure, tests with coverage, linting/formatting, typing, security checks, CI, and VS Code workflows.

Looking for the full student guide? Read the textbook in [docs](docs/index.md):

- Start here: docs/index.md
- Or jump to: Setup (docs/02-setup.md), Testing (docs/05-testing.md), VS Code (docs/09-vscode.md), CI (docs/08-ci.md)

## Quickstart (macOS + zsh)

```zsh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

Run the quality suite:

```zsh
pytest --cov=src --cov-report=term-missing -q
flake8 $(git ls-files '*.py' | tr '\n' ' ')
pylint -j 0 $(git ls-files '*.py' | tr '\n' ' ')
mypy src
make security
```

## CLI usage

Install in editable mode to use the `calc` command:

```zsh
. .venv/bin/activate
pip install -e .
calc add 2 3
```

Or run without installing:

```zsh
python -m src.main add 2 3
```

## What’s inside

- `src/` — calculator code and CLI
- `tests/` — pytest suite with 100% coverage on `src/`
- `pyproject.toml` — tool configs (Black, isort, Flake8, Pylint, mypy) and console script
- `.vscode/` — tasks, settings, and debug configs
- `.github/workflows/quality.yml` — CI for format/lint/typecheck/security
- `docs/` — the full student textbook for this project

For details, see the textbook: `docs/index.md`.
