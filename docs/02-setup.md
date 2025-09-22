# 2) Setup and first run (macOS + zsh)

This project uses a local virtual environment `.venv` and pinned developer tools.

## Create and activate the environment

```zsh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
```

## Install developer tools

```zsh
pip install -r requirements-dev.txt
```

This installs Black, isort, Flake8, Pylint, pytest (+cov, +pylint plugin), mypy, Bandit, pip‑audit, and pre‑commit.

## Verify everything

- Run tests with coverage: VS Code task “coverage” or:
  ```zsh
  pytest --cov=src --cov-report=term-missing
  ```
- Lint project files:
  ```zsh
  flake8 $(git ls-files '*.py' | tr '\n' ' ')
  pylint -j 0 $(git ls-files '*.py' | tr '\n' ' ')
  ```
- Type check:
  ```zsh
  mypy src
  ```

If these pass, you’re ready.

---

Next: [Repository structure](./03-structure.md)
