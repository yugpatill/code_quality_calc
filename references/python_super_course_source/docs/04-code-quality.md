# Code Quality: Formatting and Linting

This guide explains how to maintain high code quality with a consistent formatter and linter. We recommend:
- Black for opinionated, automatic code formatting
- isort for import sorting
- pylint for linting (or flake8 as an alternative)

## Setup

Install tools in your virtual environment:

```bash
pip install black isort pylint
```

## Running Black (formatter)

```bash
# Format the entire project
black .

# Check formatting without changing files (CI friendly)
black --check .
```

## Running isort (imports)

```bash
# Sort imports in all files
isort .

# Check without modifying (CI)
isort --check-only .
```

## Running pylint (linter)

```bash
# Check a single file
pylint filename.py

# Check multiple files
pylint file1.py file2.py

# Check all Python files in a directory
pylint your_package_name/
```

## Understanding pylint Output

pylint generates a report with:
- A score out of 10
- Messages categorized by type (error, warning, convention, refactor)
- Line numbers and descriptions of issues

Example output:
```
************* Module example
example.py:10:0: C0303: Trailing whitespace (trailing-whitespace)
example.py:15:0: C0111: Missing function docstring (missing-docstring)
```

## Common pylint Messages

- **C0111**: Missing docstring
- **C0103**: Invalid name (doesn't conform to naming convention)
- **W0612**: Unused variable
- **E1101**: Instance has no 'attribute' member
- **R0201**: Method could be a function
- **R0903**: Too few public methods

## Configuring tools

Create configuration files to customize behavior:

```bash
# Generate a default pylint configuration
pylint --generate-rcfile > .pylintrc

# Create a basic pyproject.toml for Black and isort
cat > pyproject.toml << 'EOF'
[tool.black]
line-length = 100
target-version = ["py310"]

[tool.isort]
profile = "black"
line_length = 100
force_sort_within_sections = true
combine_as_imports = true
known_first_party = ["your_package_name"]
EOF
```

Common pylint configurations:
```ini
[MASTER]
# Maximum line length
max-line-length=100

[MESSAGES CONTROL]
# Disable specific checks
disable=C0111,C0103

[REPORTS]
# Output format
output-format=text
```

## Integrating with Your Editor

Most code editors support pylint integration:

- **VS Code**: Install the Python extension
- **PyCharm**: Enable pylint in settings
- **Sublime Text**: Install SublimeLinter-pylint

## Pre-commit integration (optional)

Automate formatting and linting before each commit:

```bash
pip install pre-commit
cat > .pre-commit-config.yaml << 'EOF'
repos:
	- repo: https://github.com/psf/black
		rev: 24.8.0
		hooks:
			- id: black
	- repo: https://github.com/pycqa/isort
		rev: 5.13.2
		hooks:
			- id: isort
	- repo: https://github.com/pycqa/pylint
		rev: v3.2.6
		hooks:
			- id: pylint
				additional_dependencies: []
EOF
pre-commit install
```

## Next Steps

Learn how to automate testing and linting with [GitHub Actions](05-github-actions.md).
