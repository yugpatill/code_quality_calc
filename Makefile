.PHONY: fmt lint typecheck test security qa ci

fmt:
	. .venv/bin/activate && black . && isort .

lint:
	. .venv/bin/activate && flake8 $(shell git ls-files '*.py' | tr '\n' ' ') && pylint -j 0 $(shell git ls-files '*.py' | tr '\n' ' ')

typecheck:
	. .venv/bin/activate && mypy src

test:
	. .venv/bin/activate && pytest

security:
	. .venv/bin/activate && bandit -q -r src -x tests
	. .venv/bin/activate && pip-audit -r requirements.txt || true

qa: fmt lint typecheck test security

ci:
	. .venv/bin/activate && black --check . && isort --check-only . && flake8 $(shell git ls-files '*.py' | tr '\n' ' ') && pylint -j 0 $(shell git ls-files '*.py' | tr '\n' ' ') && mypy src && pytest && bandit -q -r src -x tests
