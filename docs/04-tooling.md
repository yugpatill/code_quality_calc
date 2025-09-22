# 4) Formatting, linting, and style

Quality tools help you keep a consistent, readable codebase.

## Black (formatter)
- Config: `[tool.black]` in `pyproject.toml` (line length 100)
- Run: VS Code task “fmt” or `black .`

## isort (imports)
- Config: `[tool.isort]` profile "black"
- Run: `isort .` (included in “fmt” task)

## Flake8 (style linter)
- Config: `[tool.flake8]` in `pyproject.toml`
- Excludes `.venv`, `build`, etc.
- Run only on project files via Git: `flake8 $(git ls-files '*.py' | tr '\n' ' ')`

## Pylint (code linter)
- Config: `[tool.pylint]` in `pyproject.toml`
- Run: `pylint -j 0 $(git ls-files '*.py' | tr '\n' ' ')`

## Pre‑commit (fast local checks)
- Config: `.pre-commit-config.yaml`
- Install hooks: `pre-commit install`
- Run all: `pre-commit run --all-files`

---

Next: [Testing and coverage](./05-testing.md)
