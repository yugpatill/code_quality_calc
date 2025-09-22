# 11) Everyday workflows

## Local development loop
- Activate venv, install dev tools
- Write a test → implement code → run tests
- Run “quality: all” in VS Code or:
  ```zsh
  black . && isort .
  flake8 $(git ls-files '*.py' | tr '\n' ' ')
  pylint -j 0 $(git ls-files '*.py' | tr '\n' ' ')
  mypy src
  pytest --cov=src --cov-report=term-missing
  make security
  ```

## Git hygiene
- Small commits with clear messages
- Open a PR early; CI must pass before merge
- Use branches per feature/fix

---

Next: [Troubleshooting](./12-troubleshooting.md)
