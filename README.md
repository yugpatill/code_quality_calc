# Basic Calculator — Professional Python Project Template

This repository demonstrates professional programming practices using a very small Python project (a basic calculator). It’s intentionally simple so the focus is on process and quality: structure, testing, linting, and workflow. It’s perfect for graduate students in Computer Science and related programs learning how to deliver production-quality code—even for tiny projects.

## Learning goals
- Understand a clean Python project layout (`src/` + `tests/`)
- Use virtual environments for reproducibility
- Write unit tests with pytest and name them clearly
- Lint code with pylint and interpret feedback
- Document decisions in `README.md` and track metadata in `pyproject.toml`
- Practice disciplined Git workflows and iterate with confidence

## What’s in this repo

```
.
├── .gitignore           # Ignore venv, caches, OS/editor files
├── .pylintrc            # Linting rules (pylint)
├── pyproject.toml       # Project metadata + build system
├── pytest.ini           # Test discovery and options
├── requirements.txt     # Developer dependencies (pytest, pylint)
├── src/
│   ├── __init__.py      # Marks src as a package, enables src.main import
│   └── main.py          # Calculator functions (currently: addition)
├── tests/
│   └── test_sanity.py   # Example unit test covering addition
├── venv/                # Local virtual environment (ignored by Git)
└── README.md            # You are here
```

Notes:
- `src/` layout: Keeping code under `src/` prevents accidental imports from the working directory and mirrors how your package would be used when installed. Pytest runs with the repository root on `sys.path`, so `import src.main` works because `src/` has an `__init__.py`.
- `pyproject.toml`: Declares metadata and build-system. We’re using `setuptools`. Once the package grows, you can configure packaging (e.g., `tool.setuptools.package-dir`).
- `.pylintrc`: Configured to focus feedback on what matters early (line length, basic design warnings) without overwhelming you with docstring requirements.

## The calculator (initial scope)

Current API (in `src/main.py`):

```python
def addition(a, b):
    return a + b
```

Contract:
- Inputs: numbers (int or float)
- Output: number (sum)
- Error modes: Python will raise `TypeError` if unsupported types are added.

Extension ideas (recommended TDD order):
1) subtraction(a, b)
2) multiplication(a, b)
3) division(a, b) with divide-by-zero handling
4) power(a, b), sqrt(a)
5) input validation and type hints throughout

Each new function should be accompanied by tests that define expected behavior before the implementation.

## Setup (macOS, zsh)

1) Create and activate a virtual environment in `venv`:

```zsh
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

2) Install developer dependencies:

```zsh
pip install -r requirements.txt
```

3) (Optional) Install the project in editable mode once you turn `src/` into an installable package:

```zsh
pip install -e .
```

## Running tests

```zsh
pytest
```

Pytest configuration highlights (`pytest.ini`):
- `testpaths = tests` ensures tests live under `tests/`
- `python_files = test_*.py *_test.py` keeps test filenames consistent
- `-ra -q` gives concise output while still showing summary of skipped/xfailed

Tips:
- Run a subset: `pytest -k addition`
- Stop on first failure: `pytest -x`
- Show print statements: `pytest -s`

Coverage (optional but encouraged):

```zsh
pip install pytest-cov
pytest --cov=src --cov-report=term-missing
```

## Linting with pylint

Run pylint from the project root:

```zsh
pylint .
```

Configuration highlights (`.pylintrc`):
- `max-line-length = 100` for readability without wrapping too aggressively
- Some docstring warnings disabled early to keep signal-to-noise high in small demos
- `ignore=venv` avoids scanning the virtual environment

As the project matures, re-enable stricter rules and add docstrings systematically.

## Professional workflow suggestions

- Use feature branches and small, focused commits. Prefer meaningful messages, e.g.,
  - "Add subtraction() with tests"
  - "Refactor calculator API; add type hints"
- Open pull requests early for feedback. Include test results and a short description of the change.
- Keep CI green: tests must pass and lints should be clean before merging.
- Write tests first (TDD): define behavior via tests, then implement.
- Prefer pure functions with clear inputs/outputs; avoid hidden state.

Optional next steps you can add to this repository:
- Continuous Integration (GitHub Actions) to run `pytest` and `pylint` on every push
- Type checking with `mypy` and style with `ruff` or `black`
- A `Makefile` or simple task runner (e.g., `tox`, `nox`) to standardize commands
- A `LICENSE` file and a proper project name in `pyproject.toml`

## Troubleshooting

- "ModuleNotFoundError: No module named 'src'": ensure you run commands from the repository root and that `src/__init__.py` exists (it does). If you install the package (`pip install -e .`) and move to a different working directory, import via your package name instead.
- Using the wrong Python: verify you’re inside the virtual environment. `which python` should point to `.../venv/bin/python`.
- Lint noise: start with the current `.pylintrc`. Tighten rules once code stabilizes.

## Why this structure matters

Real-world engineering is about more than code that "works". This template reinforces:
- Reproducibility: isolated dependencies in `venv/`
- Testability: fast unit tests under `tests/`
- Maintainability: consistent style and early feedback from linters
- Portability: metadata in `pyproject.toml` for packaging and tooling
- Clarity: a README that explains how to build, test, and extend

If you’re new to professional Python, study the configuration files—they encode many best practices you’ll reuse in larger systems.

