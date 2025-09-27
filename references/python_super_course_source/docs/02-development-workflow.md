# Development Workflow

This guide covers best practices for writing and organizing your Python code.

## Project Structure

A well-organized Python project typically follows this structure:

```
project_name/
├── README.md
├── requirements.txt
├── .gitignore
├── .github/
│   └── workflows/
│       └── main.yml
├── src/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   └── test_module2.py
└── docs/
    └── ...
```

## Code Organization

### Modules and Packages

- **Modules**: Single Python files (`.py`)
- **Packages**: Directories containing multiple modules and an `__init__.py` file

### Imports

Use the following import conventions:

```python
# Standard library imports
import os
import sys

# Third-party imports
import numpy as np
import pandas as pd

# Local application imports
from src.module1 import some_function
```

## Git Workflow

### Basic Git Commands

```bash
# Check status of your files
git status

# Add files to staging
git add filename.py

# Commit changes
git commit -m "Description of changes"

# Push to remote repository
git push origin main
```

### Branching Strategy

```bash
# Create a new branch
git checkout -b feature/new-feature

# Work on your changes, then commit and push
git add .
git commit -m "Implement new feature"
git push origin feature/new-feature

# Create a pull request on GitHub to merge into main
```

## Code Documentation

### Docstrings

Use docstrings to document your functions and classes:

```python
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers (list): A list of integers or floats
        
    Returns:
        float: The average of the numbers
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)
```

## Next Steps

Learn how to ensure your code works as expected with [Testing with pytest](03-testing.md).
