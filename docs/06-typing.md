# 6) Static typing with mypy

Static typing catches bugs early and documents intent.

- Config: `[tool.mypy]` in `pyproject.toml` (targets Python 3.11, excludes tests)
- Key flags: `disallow_untyped_defs = true`, `no_implicit_optional = true`

## Run type checks
```zsh
mypy src
```

Tip: Add types to function signatures and return values. Prefer `float` math in CLI.

---

Next: [CLI and packaging](./07-cli.md)
