# Project 1 (Python)

A minimal Python project scaffold with testing and linting.

## Prerequisites
- Python 3.10+ installed
- Git (optional)

## Setup (macOS, zsh)

Create and activate a virtual environment in `venv`:

```zsh
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

Install dependencies:

```zsh
pip install -r requirements.txt
```

(Optional) Install the project in editable mode if you later add a package:

```zsh
pip install -e .
```

## Run tests

```zsh
pytest
```

- Useful options:
  - `pytest -q` for quiet output
  - `pytest -k pattern` to run tests matching a substring

## Lint with pylint

```zsh
pylint .
```

- Lint only your package (recommended once you add a `src/` package):

```zsh
pylint src
```

## Project structure

- `README.md` — this file
- `pyproject.toml` — project metadata (optional to start)
- `pytest.ini` — pytest configuration
- `.pylintrc` — pylint configuration
- `requirements.txt` — dev dependencies (pytest, pylint)
- `tests/` — test suite

## Tips
- Keep virtual env untracked (already in `.gitignore`).
- Add your application code under `src/your_package/` and add `src` to `pyproject.toml` when ready.
