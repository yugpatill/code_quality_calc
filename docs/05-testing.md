# 5) Testing and coverage

We use pytest with coverage and enforce 100% for `src/`.

- Config: `pytest.ini`
  - `addopts = --cov=src --pylint --cov-report=term-missing --cov-fail-under=100 -q -ra`
  - `testpaths = tests`

## Run tests
```zsh
pytest -q
```

## Coverage report
```zsh
pytest --cov=src --cov-report=term-missing --cov-report=xml
```
- Writes `coverage.xml` for the Coverage Gutters VS Code extension.

## Writing tests
- Name files `test_*.py`, functions `test_*`.
- Use `pytest.raises` for exceptions.
- Parametrize with `@pytest.mark.parametrize`.

---

Next: [Static typing with mypy](./06-typing.md)
