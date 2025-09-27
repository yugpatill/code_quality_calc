# Assignment 2: Code Quality with Pylint

## Learning Objectives
- Understand the importance of code quality and style guidelines
- Learn about PEP 8, Python's style guide
- Install and configure pylint
- Identify and fix common code quality issues
- Integrate pylint into your development workflow
- Apply code quality standards to your calculator project

## Background

Writing clean, readable code is essential for collaboration and maintenance. Python has a style guide called PEP 8 that provides conventions for Python code. Pylint is a static code analysis tool that checks if your code follows these conventions and helps identify potential errors.

### Historical Context

Code quality tools have a long history in software development:
- In 1978, Stephen Johnson created "lint" for C programming, the first static analyzer
- PEP 8 was introduced in 2001 to standardize Python code style
- Pylint was created in 2003 to automate PEP 8 compliance checking
- Modern development teams consider linting an essential part of the development workflow

## Prerequisites
- Python >= 3.10 installed
- Virtual environment knowledge (from Assignment 1)
- Basic Python programming skills
- Calculator project from Assignment 1

## Time to Complete
Expect to spend approximately 2-3 hours on this assignment.

## Part 1: Setting Up Pylint for Your Calculator Project

### Task 1.1: Prepare Your Environment

1. Navigate to your calculator project directory:
   ```bash
   cd python_calculator
   ```

2. Ensure your virtual environment is activated:
   ```bash
   # On Windows with WSL2, macOS, or Linux:
   source venv/bin/activate
   
   # On Windows Command Prompt:
   venv\Scripts\activate
   
   # On Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   ```

3. If you haven't already installed pylint, install it now:
   ```bash
   pip install pylint
   ```

### Task 1.2: First Analysis of Your Calculator Code

1. Run pylint on your existing calculator operations file:
   ```bash
   pylint src/calculator/operations.py
   ```

2. Take note of the score and the issues pylint found.

3. Create a text file named `pylint_issues.txt` and document:
   - What was your initial score?
   - What types of issues were found?
   - Which issues do you think are most important to fix?

## Part 2: Understanding PEP 8 and Pylint Messages

### Task 2.1: Learn About PEP 8

Read the key sections of PEP 8, focusing on:
- Indentation (4 spaces per level)
- Maximum line length (79 characters)
- Imports (should be on separate lines, grouped properly)
- Whitespace in expressions and statements
- Comments and docstrings
- Naming conventions

### Task 2.2: Understanding Pylint Messages

Pylint message categories:
- **C**: Convention - programming standard violation
- **R**: Refactor - bad code smell
- **W**: Warning - Python specific problems
- **E**: Error - likely bugs
- **F**: Fatal - error preventing further processing

Common messages include:
- C0111: Missing docstring
- C0103: Invalid name
- C0303: Trailing whitespace
- E1101: Instance has no 'x' member
- R0201: Method could be a function

## Part 3: Improving Your Calculator Code

### Task 3.1: Fixing Convention Issues

1. Improve the docstrings in your `operations.py` file:
   ```python
   """
   Basic arithmetic operations for the calculator.
   
   This module provides elementary math functions for the calculator application.
   """

   def add(a, b):
       """
       Add two numbers and return the result.
       
       Args:
           a: First number
           b: Second number
           
       Returns:
           The sum of a and b
       """
       return a + b
   
   def subtract(a, b):
       """
       Subtract b from a and return the result.
       
       Args:
           a: Number to subtract from
           b: Number to subtract
           
       Returns:
           The difference (a - b)
       """
       return a - b
   ```

2. Run pylint again to see the improvement:
   ```bash
   pylint src/calculator/operations.py
   ```

### Task 3.2: Creating a Pylint Configuration

1. Generate a default pylint configuration file:
   ```bash
   pylint --generate-rcfile > .pylintrc
   ```

2. Edit `.pylintrc` to customize settings:
   - Increase maximum line length to 100
   - Add your name to the copyright holder
   - Adjust the docstring template if desired

3. Run pylint with your configuration:
   ```bash
   pylint --rcfile=.pylintrc src/calculator/operations.py
   ```

## Part 4: Extending Your Calculator with Quality in Mind

### Task 4.1: Adding New Operations with Good Code Quality

1. Add multiplication and division functions to `operations.py`, ensuring they meet PEP 8 standards:
   ```python
   def multiply(a, b):
       """
       Multiply two numbers and return the result.
       
       Args:
           a: First number
           b: Second number
           
       Returns:
           The product of a and b
       """
       return a * b
   
   def divide(a, b):
       """
       Divide a by b and return the result.
       
       Args:
           a: Numerator
           b: Denominator
           
       Returns:
           The quotient a/b
           
       Raises:
           ZeroDivisionError: If b is 0
       """
       if b == 0:
           raise ZeroDivisionError("Cannot divide by zero")
       return a / b
   ```

2. Run pylint on the updated file:
   ```bash
   pylint --rcfile=.pylintrc src/calculator/operations.py
   ```

### Task 4.2: Creating a Calculator Class

1. Create a new file `src/calculator/calculator.py`:
   ```python
   """
   Calculator class implementation.
   
   This module provides a Calculator class that uses the operations module.
   """
   from calculator.operations import add, subtract, multiply, divide

   class Calculator:
       """
       A simple calculator class that provides basic arithmetic operations.
       
       This class uses the functions from the operations module to perform
       calculations and keeps track of calculation history.
       """
       
       def __init__(self):
           """Initialize a new Calculator with empty history."""
           self.history = []
       
       def add(self, a, b):
           """
           Add two numbers and store the operation in history.
           
           Args:
               a: First number
               b: Second number
               
           Returns:
               The sum of a and b
           """
           result = add(a, b)
           self.history.append(f"{a} + {b} = {result}")
           return result
       
       def subtract(self, a, b):
           """
           Subtract b from a and store the operation in history.
           
           Args:
               a: Number to subtract from
               b: Number to subtract
               
           Returns:
               The difference (a - b)
           """
           result = subtract(a, b)
           self.history.append(f"{a} - {b} = {result}")
           return result
       
       def multiply(self, a, b):
           """
           Multiply two numbers and store the operation in history.
           
           Args:
               a: First number
               b: Second number
               
           Returns:
               The product of a and b
           """
           result = multiply(a, b)
           self.history.append(f"{a} * {b} = {result}")
           return result
       
       def divide(self, a, b):
           """
           Divide a by b and store the operation in history.
           
           Args:
               a: Numerator
               b: Denominator
               
           Returns:
               The quotient a/b
               
           Raises:
               ZeroDivisionError: If b is 0
           """
           result = divide(a, b)
           self.history.append(f"{a} / {b} = {result}")
           return result
       
       def get_history(self):
           """
           Return the calculation history.
           
           Returns:
               A list of strings representing the calculation history
           """
           return self.history
   ```

2. Run pylint on the new file:
   ```bash
   pylint --rcfile=.pylintrc src/calculator/calculator.py
   ```

## Part 5: VS Code Integration

### Task 5.1: Configuring VS Code for Pylint

1. Open your project in VS Code.

2. Create a `.vscode/settings.json` file:
   ```json
   {
       "python.linting.enabled": true,
       "python.linting.pylintEnabled": true,
       "python.linting.pylintArgs": [
           "--rcfile=.pylintrc"
       ],
       "editor.formatOnSave": true,
       "python.formatting.provider": "black",
       "python.sortImports.args": ["--profile", "black"]
   }
   ```

3. Install Black and isort for formatting and import sorting:
   ```bash
    pip install black isort
   ```

4. Open a Python file and see linting in action in the editor.

## Common Pitfalls

- **Ignoring warnings**: Warnings often indicate real issues that should be fixed
- **Over-suppressing rules**: Use disable comments sparingly and with good reason
- **Inconsistent formatting**: Use a code formatter like Black to maintain consistency
- **Missing docstrings**: Always include docstrings for modules, classes, and functions
- **Focusing only on the score**: The specific issues are more important than the numeric score

## Troubleshooting

### Issue: "No module named 'calculator'"

**Solution:**
- Make sure you've installed your package in development mode:
  ```bash
  pip install -e .
  ```
- Check that your import statements match your directory structure

### Issue: VS Code not showing pylint errors

**Solution:**
- Check that the Python extension is installed
- Verify that the selected interpreter is from your virtual environment
- Make sure pylint is installed in your virtual environment

## What Success Looks Like

By the end of this assignment, you should have:
- A calculator project with high code quality (pylint score of 9.0+)
- Well-documented code with proper docstrings
- A custom pylint configuration
- VS Code integration for continuous code quality feedback
- A solid understanding of PEP 8 and Python coding standards

## Self-Assessment Questions

1. Why is code quality important in professional software development?
2. What are the key principles of PEP 8?
3. How does pylint help enforce coding standards?
4. What's the difference between style conventions and actual code errors?
5. How would you customize pylint for different types of projects?
6. How does maintaining good code quality help with team collaboration?

## Submission Requirements

Submit the following:

1. Your improved calculator code with high pylint scores
2. Your `.pylintrc` configuration file
3. A `pylint_issues.txt` file documenting the issues you found and fixed
4. A brief reflection (300-500 words) on how code quality practices benefit software development

## Additional Resources

- [PEP 8 Style Guide](https://pep8.org/)
- [Pylint User Manual](http://pylint.pycqa.org/en/latest/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Real Python: Linting Python Code](https://realpython.com/python-code-quality/)
- [Effective Python: 90 Specific Ways to Write Better Python](https://effectivepython.com/)
