# 9) VS Code configuration and tasks

## Settings
- File: `.vscode/settings.json`
- Select interpreter: `.venv/bin/python`
- Pytest enabled; format on save via Black; organize imports; Coverage Gutters reads `coverage.xml`.

## Tasks (Command Palette → Run Task)
- venv: create
- venv: pip upgrade
- install: dev tools
- fmt (Black + isort)
- lint (Flake8 + Pylint on Git‑tracked files)
- coverage (pytest with coverage)
- typecheck (mypy)
- security (make security)
- pre‑commit: all‑files
- quality: all (runs fmt → lint → typecheck → coverage → security)

## Debugging
- File: `.vscode/launch.json` (debugpy)
- Examples:
  - Debug calc CLI (add)
  - Debug calc CLI (divide‑by‑zero)
  - Pytest: Debug tests (prompts for -k filter)

---

Next: [Security and dependency health](./10-security.md)
