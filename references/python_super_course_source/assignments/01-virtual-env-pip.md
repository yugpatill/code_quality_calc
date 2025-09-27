# Assignment 1: Virtual Environments and Package Management

## Learning Objectives
- Understand the purpose of virtual environments
- Create and activate Python virtual environments
- Install and manage packages with pip
- Manage package versions and dependencies
- Create and use requirements.txt files
- Set up the basic structure for a Python calculator project

## Background

When developing Python applications, you'll often need specific versions of libraries. Using virtual environments allows you to create isolated spaces for your projects, avoiding conflicts between different projects' dependencies.

### Historical Context

Before virtual environments existed, Python developers faced significant challenges:

- **System-wide packages**: All packages were installed globally, causing version conflicts between projects
- **Dependency hell**: Different projects requiring different versions of the same package
- **Limited isolation**: No way to create project-specific environments

The `virtualenv` tool was created in 2007 by Ian Bicking to solve these problems. Later, Python 3.3+ integrated this functionality directly as the `venv` module, making environment isolation a standard practice.

## Prerequisites
- Completion of Assignment 0: Professional Development Environment Setup
- Python >= 3.10 installed and configured
- VS Code with Python extensions installed
- Git properly configured
- Terminal/Command Prompt access and basic familiarity

## Time to Complete
Expect to spend approximately 2-3 hours on this assignment.

## Part 1: Creating Your First Virtual Environment

### Task 1.1: Create a Virtual Environment for Our Calculator Project

1. Create a new directory for the calculator project:
   ```bash
   # All platforms
   mkdir python_calculator
   cd python_calculator
   ```

2. Create a virtual environment:
   ```bash
   # On Windows with WSL2, macOS, or Linux:
   python3 -m venv venv
   
   # On Windows (PowerShell or Command Prompt):
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   # On Windows with WSL2, macOS, or Linux:
   source venv/bin/activate
   
   # On Windows Command Prompt:
   venv\Scripts\activate
   
   # On Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   ```

4. Verify activation:
   ```bash
   # The command prompt should now show (venv) at the beginning
   
   # Check Python location (On Windows with WSL2, macOS, or Linux):
   which python
   
   # Check Python location (On Windows Command Prompt):
   where python
   
   # Check Python location (On Windows PowerShell):
   Get-Command python | Format-List
   ```

### Task 1.2: Deactivate and Reactivate

1. Deactivate the virtual environment:
   ```bash
   # All platforms
   deactivate
   ```

2. Observe that the `(venv)` prefix is gone.

3. Reactivate the virtual environment:
   ```bash
   # On Windows with WSL2, macOS, or Linux:
   source venv/bin/activate
   
   # On Windows Command Prompt:
   venv\Scripts\activate
   
   # On Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   ```

### VS Code Integration

If you're using VS Code:

1. Open your project folder in VS Code:
   ```bash
   # All platforms
   code .
   ```

2. When prompted to select a Python interpreter, choose the one in your virtual environment:
   - It should be labeled as `./venv/bin/python` (WSL2, macOS, Linux)
   - Or `.\venv\Scripts\python.exe` (Windows)

## Part 2: Package Management for the Calculator Project

### Task 2.1: Installing Required Packages

1. Ensure your virtual environment is activated.

2. Install pytest for testing:
   ```bash
   # All platforms
   pip install pytest
   ```

3. Install pylint for code quality:
   ```bash
   # All platforms
   pip install pylint
   ```

4. List installed packages:
   ```bash
   # All platforms
   pip list
   ```

### Task 2.2: Setting Up the Calculator Project Structure

1. Create the following directory structure:
   ```
   python_calculator/
   ├── src/
   │   └── calculator/
   │       ├── __init__.py
   │       └── operations.py
   ├── tests/
   │   ├── __init__.py
   │   └── test_operations.py
   └── venv/
   ```

   You can do this with these commands:
   ```bash
   mkdir -p src/calculator tests
   touch src/calculator/__init__.py
   touch src/calculator/operations.py
   touch tests/__init__.py
   touch tests/test_operations.py
   ```

2. Create a simple implementation in `src/calculator/operations.py`:
   ```python
   """Basic arithmetic operations for the calculator."""

   def add(a, b):
       """Add two numbers and return the result."""
       return a + b
   
   def subtract(a, b):
       """Subtract b from a and return the result."""
       return a - b
   ```

3. Create a simple test in `tests/test_operations.py`:
   ```python
   """Tests for calculator operations."""
   
   from calculator.operations import add, subtract

   def test_add():
       """Test the add function."""
       assert add(1, 2) == 3
       assert add(-1, 1) == 0
       assert add(0, 0) == 0
   
   def test_subtract():
       """Test the subtract function."""
       assert subtract(3, 2) == 1
       assert subtract(2, 3) == -1
       assert subtract(0, 0) == 0
   ```

4. Run the test to verify your setup:
   ```bash
   # Navigate to the root of your project
   cd python_calculator
   
   # Run pytest
   python -m pytest
   ```

   If you get an import error, create a `setup.py` file:
   ```python
   from setuptools import setup, find_packages

   setup(
       name="calculator",
       version="0.1",
       packages=find_packages(where="src"),
       package_dir={"": "src"},
   )
   ```

   Then install your package in development mode:
   ```bash
   pip install -e .
   ```

## Part 3: Managing Dependencies for the Calculator Project

### Task 3.1: Creating a requirements.txt File

1. Generate a requirements.txt file:
   ```bash
   # All platforms
   pip freeze > requirements.txt
   ```

2. Examine the contents of requirements.txt:
   ```bash
   # On Windows with WSL2, macOS, or Linux:
   cat requirements.txt
   
   # On Windows Command Prompt:
   type requirements.txt
   
   # On Windows PowerShell:
   Get-Content requirements.txt
   ```

### Task 3.2: Using requirements.txt in a New Environment

1. Deactivate and delete your virtual environment:
   ```bash
   # All platforms
   deactivate
   
   # On Windows with WSL2, macOS, or Linux:
   rm -rf venv
   
   # On Windows Command Prompt:
   rmdir /s /q venv
   
   # On Windows PowerShell:
   Remove-Item -Recurse -Force venv
   ```

2. Create a new virtual environment:
   ```bash
   # On Windows with WSL2, macOS, or Linux:
   python3 -m venv new_venv
   
   # On Windows (PowerShell or Command Prompt):
   python -m venv new_venv
   ```

3. Activate the new environment:
   ```bash
   # On Windows with WSL2, macOS, or Linux:
   source new_venv/bin/activate
   
   # On Windows Command Prompt:
   new_venv\Scripts\activate
   
   # On Windows PowerShell:
   .\new_venv\Scripts\Activate.ps1
   ```

4. Install dependencies from requirements.txt:
   ```bash
   # All platforms
   pip install -r requirements.txt
   ```

5. Verify that all packages were installed:
   ```bash
   # All platforms
   pip list
   ```

6. Run the tests again to verify everything works:
   ```bash
   python -m pytest
   ```

## Part 4: Advanced Package Management

### Task 4.1: Understanding Version Specifiers

1. Edit your requirements.txt file to use version specifiers:
   ```
   pytest>=7.0.0,<8.0.0
   pylint>=2.15.0,<3.0.0
   ```

2. Reinstall with the updated requirements:
   ```bash
   # All platforms
   pip install -r requirements.txt
   ```

3. Research and document the meaning of these version specifiers:
   - `==`: Exact version
   - `>=`: Greater than or equal to
   - `<=`: Less than or equal to
   - `~=`: Compatible release
   - `!=`: Not equal to

### Task 4.2: Development vs. Production Dependencies

In professional projects, it's common to separate development dependencies from production dependencies:

1. Create a file named `requirements-dev.txt`:
   ```
   # Include production dependencies
   -r requirements.txt
   
   # Development-only dependencies
   pytest>=7.0.0,<8.0.0
   pylint>=2.15.0,<3.0.0
   black>=22.8.0,<23.0.0  # Code formatter
   ```

2. Create a minimal `requirements.txt` with only what the calculator needs to run:
   ```
   # No external dependencies for basic calculator functionality
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Common Pitfalls

- **Forgetting to activate the virtual environment**: Always check for the `(venv)` prefix in your terminal prompt
- **Installing packages globally**: If you don't see the prefix, you might be installing packages in your global Python
- **Path issues in import statements**: Make sure your project structure matches the import paths
- **Not including `__init__.py` files**: These are needed to make Python treat directories as packages
- **Running pytest from the wrong directory**: Run it from the project root, not from inside the tests directory

## Troubleshooting Common Issues

### Issue: "Command not found: python" or "Command not found: python3"

**Solution:**
- **Windows:** Make sure Python is added to your PATH during installation
- **macOS/Linux:** Use `python3` instead of `python`
- **All platforms:** Verify the installation with `python --version` or `python3 --version`

### Issue: "Error: Could not find a version that satisfies the requirement"

**Solution:**
- Check your internet connection
- Verify the package name is correct
- Try upgrading pip: `pip install --upgrade pip`

### Issue: Virtual environment not activating properly

**Solution:**
- Make sure you're using the correct activation command for your platform
- Check that the virtual environment was created successfully
- Try creating a new virtual environment

### Issue: "Permission denied" when installing packages

**Solution:**
- **macOS/Linux:** Use `pip install --user package_name` or use a virtual environment
- **Windows:** Run Command Prompt or PowerShell as administrator

## What Success Looks Like

By the end of this assignment, you should have:
- A working virtual environment
- A basic calculator project structure with addition and subtraction operations
- Working tests for these operations
- A requirements.txt file to manage dependencies
- Knowledge of how to manage package versions

## Self-Assessment Questions

Take a moment to answer these questions to check your understanding:

1. Why are virtual environments important for Python development?
2. What is the difference between `pip install package` and `pip install -r requirements.txt`?
3. How would you specify that your project needs any version of pytest that is at least 7.0.0 but less than 8.0.0?
4. What happens if two projects on your computer need different versions of the same library?
5. What are the key differences in virtual environment usage between Windows, macOS, and Linux/WSL2?
6. How has Python package management evolved over time, and what problems did each evolution solve?

## Submission Requirements

Create a text file named `assignment1_answers.txt` with the following:

1. Screenshots or terminal output showing:
   - Virtual environment activation
   - Package installation
   - Running the calculator tests
   - Creating and using requirements.txt

2. Written answers to the self-assessment questions above.

## Additional Resources

- [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/)
- [pip User Guide](https://pip.pypa.io/en/stable/user_guide/)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/)
- [VS Code Python Environment Setup](https://code.visualstudio.com/docs/python/environments)
- [History of Python Packaging](https://blog.jaraco.com/a-history-of-python-packaging/)
