# 7) CLI and packaging

We provide a console script `calc` and a Python module entry `src.main:main`.

- Packaging metadata: `[build-system]` and `[project]` in `pyproject.toml`
- Console entry point:
  ```toml
  [project.scripts]
  calc = "src.main:main"
  ```
- Explicit packages to include:
  ```toml
  [tool.setuptools]
  packages = ["src", "src.operations"]
  ```

## Install and use the CLI
```zsh
. .venv/bin/activate
pip install -e .
calc add 2 3
```

## Run without installing
```zsh
python -m src.main add 2 3
```

---

Next: [Continuous Integration](./08-ci.md)
