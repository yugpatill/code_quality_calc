# 3) Repository structure

```
.
├── pyproject.toml                 # Tooling + packaging metadata
├── pytest.ini                     # Pytest configuration
├── requirements.txt               # (Optional) runtime dependencies
├── requirements-dev.txt           # Developer toolchain
├── Makefile                       # Common quality targets
├── .pre-commit-config.yaml        # Fast local checks before commit
├── .editorconfig                  # Editor‑agnostic formatting rules
├── .github/workflows/quality.yml  # CI pipeline
├── .vscode/                       # Editor tasks, settings, launches
│   ├── tasks.json
│   ├── settings.json
│   └── launch.json
├── src/
│   ├── __init__.py
│   ├── main.py                    # CLI entry
│   └── operations/__init__.py     # Arithmetic functions
├── tests/
│   ├── __init__.py
│   ├── test_operations.py
│   └── test_operations_param.py
└── docs/                          # This textbook
```

Design choices:
- src/ layout: prevents accidental imports and mirrors installable packages.
- Single source of truth for config in `pyproject.toml` where possible.
- Tests live in `tests/` and target `src/`.
- VS Code tasks encapsulate common commands using the venv.

---

Next: [Formatting, linting, and style](./04-tooling.md)
