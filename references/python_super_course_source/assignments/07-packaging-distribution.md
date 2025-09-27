````markdown
# Assignment 7: Python Packaging and Distribution

## Learning Objectives
- Master modern Python packaging with pyproject.toml
- Understand semantic versioning and dependency management
- Publish packages to PyPI and PyPI test environments
- Create distributable applications with entry points
- Implement proper package structure and metadata
- Apply packaging security and best practices

## Background

Python packaging has evolved significantly with modern tools like pyproject.toml, Poetry, and improved pip. This assignment teaches you to create professional, distributable Python packages that others can easily install and use.

### Modern Packaging Standards

This assignment follows PEP 517/518 standards for build system requirements and uses:
- **pyproject.toml**: Modern configuration format replacing setup.py
- **Semantic Versioning**: Version numbering that conveys meaning
- **Entry Points**: Creating command-line tools from your packages
- **Build Backends**: Using setuptools, poetry, or other build systems

Professional Python developers must know how to package and distribute their code effectively.

## Prerequisites
- Completed Assignments 1-6
- Calculator project with configuration management
- Understanding of virtual environments
- Basic knowledge of command-line interfaces

## Time to Complete
Expect to spend approximately 3-4 hours on this assignment.

## Part 1: Modern Package Structure

### Task 1.1: Restructure Project for Distribution

1. Create the modern package structure:
   ```
   calculator-package/
   ├── pyproject.toml
   ├── README.md
   ├── LICENSE
   ├── CHANGELOG.md
   ├── MANIFEST.in
   ├── src/
   │   └── calculator/
   │       ├── __init__.py
   │       ├── __main__.py
   │       ├── cli.py
   │       ├── calculator.py
   │       ├── operations.py
   │       ├── scientific.py
   │       ├── config.py
   │       ├── logging_config.py
   │       └── version.py
   ├── tests/
   ├── docs/
   ├── config/
   └── scripts/
   ```

2. Create `src/calculator/__init__.py`:
   ```python
   """
   Calculator Package
   
   A professional calculator library with support for basic and scientific operations,
   configuration management, and comprehensive logging.
   """
   from .calculator import Calculator
   from .operations import add, subtract, multiply, divide
   from .scientific import (
       square_root, power, sin, cos, tan, log, natural_log,
       factorial, degrees_to_radians, radians_to_degrees
   )
   from .config import config
   from .version import __version__
   
   __all__ = [
       'Calculator',
       'add', 'subtract', 'multiply', 'divide',
       'square_root', 'power', 'sin', 'cos', 'tan',
       'log', 'natural_log', 'factorial',
       'degrees_to_radians', 'radians_to_degrees',
       'config', '__version__'
   ]
   
   # Package metadata
   __author__ = "Your Name"
   __email__ = "your.email@example.com"
   __description__ = "A professional calculator library with advanced features"
   ```

3. Create `src/calculator/version.py`:
   ```python
   """Version information for the calculator package."""
   
   __version__ = "1.0.0"
   __version_info__ = tuple(map(int, __version__.split('.')))
   
   
   def get_version():
       """Return the version string."""
       return __version__
   
   
   def get_version_info():
       """Return the version as a tuple of integers."""
       return __version_info__
   ```

4. Create `src/calculator/__main__.py`:
   ```python
   """Main module for running calculator as a package."""
   from .cli import main
   
   if __name__ == '__main__':
       main()
   ```

### Task 1.2: Create Command-Line Interface

1. Create `src/calculator/cli.py`:
   ```python
   """Command-line interface for the calculator."""
   import sys
   import argparse
   from typing import List, Optional
   
   from .calculator import Calculator
   from .config import config
   from .logging_config import setup_logging
   from .version import __version__
   
   
   def create_parser() -> argparse.ArgumentParser:
       """Create and configure the argument parser."""
       parser = argparse.ArgumentParser(
           prog='calculator',
           description='A professional calculator with basic and scientific operations',
           epilog='Examples:\n'
                  '  calculator add 5 3\n'
                  '  calculator --interactive\n'
                  '  calculator --version',
           formatter_class=argparse.RawDescriptionHelpFormatter
       )
       
       # Version
       parser.add_argument(
           '--version', action='version',
           version=f'calculator {__version__}'
       )
       
       # Interactive mode
       parser.add_argument(
           '-i', '--interactive',
           action='store_true',
           help='Start interactive calculator mode'
       )
       
       # Configuration options
       parser.add_argument(
           '--precision',
           type=int,
           default=None,
           help='Number of decimal places for results'
       )
       
       parser.add_argument(
           '--log-level',
           choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
           default='INFO',
           help='Set logging level'
       )
       
       # Operation subcommands
       subparsers = parser.add_subparsers(
           dest='operation',
           help='Available operations'
       )
       
       # Basic operations
       add_parser = subparsers.add_parser('add', help='Add two numbers')
       add_parser.add_argument('a', type=float, help='First number')
       add_parser.add_argument('b', type=float, help='Second number')
       
       subtract_parser = subparsers.add_parser('subtract', help='Subtract two numbers')
       subtract_parser.add_argument('a', type=float, help='First number')
       subtract_parser.add_argument('b', type=float, help='Second number')
       
       multiply_parser = subparsers.add_parser('multiply', help='Multiply two numbers')
       multiply_parser.add_argument('a', type=float, help='First number')
       multiply_parser.add_argument('b', type=float, help='Second number')
       
       divide_parser = subparsers.add_parser('divide', help='Divide two numbers')
       divide_parser.add_argument('a', type=float, help='First number')
       divide_parser.add_argument('b', type=float, help='Second number')
       
       # Scientific operations
       sqrt_parser = subparsers.add_parser('sqrt', help='Square root of a number')
       sqrt_parser.add_argument('x', type=float, help='Number')
       
       power_parser = subparsers.add_parser('power', help='Raise number to power')
       power_parser.add_argument('base', type=float, help='Base number')
       power_parser.add_argument('exponent', type=float, help='Exponent')
       
       sin_parser = subparsers.add_parser('sin', help='Sine of angle in radians')
       sin_parser.add_argument('x', type=float, help='Angle in radians')
       
       cos_parser = subparsers.add_parser('cos', help='Cosine of angle in radians')
       cos_parser.add_argument('x', type=float, help='Angle in radians')
       
       tan_parser = subparsers.add_parser('tan', help='Tangent of angle in radians')
       tan_parser.add_argument('x', type=float, help='Angle in radians')
       
       return parser
   
   
   def interactive_mode(calc: Calculator) -> None:
       """Run calculator in interactive mode."""
       print(f"Calculator v{__version__} - Interactive Mode")
       print("Type 'help' for commands, 'quit' to exit")
       print("-" * 40)
       
       while True:
           try:
               user_input = input("calc> ").strip()
               
               if user_input.lower() in ['quit', 'exit', 'q']:
                   print("Goodbye!")
                   break
               
               if user_input.lower() == 'help':
                   print_help()
                   continue
               
               if user_input.lower() == 'history':
                   print_history(calc)
                   continue
               
               if user_input.lower() == 'clear':
                   calc.clear_history()
                   print("History cleared")
                   continue
               
               if user_input.lower() == 'stats':
                   print_stats(calc)
                   continue
               
               # Parse and execute command
               result = parse_interactive_command(calc, user_input)
               if result is not None:
                   print(f"Result: {result}")
           
           except KeyboardInterrupt:
               print("\nGoodbye!")
               break
           except Exception as e:
               print(f"Error: {e}")
   
   
   def print_help():
       """Print interactive mode help."""
       help_text = """
   Available commands:
   
   Basic Operations:
     add <a> <b>        - Add two numbers
     subtract <a> <b>   - Subtract b from a
     multiply <a> <b>   - Multiply two numbers
     divide <a> <b>     - Divide a by b
   
   Scientific Operations:
     sqrt <x>           - Square root of x
     power <base> <exp> - Raise base to power of exp
     sin <x>            - Sine of x (radians)
     cos <x>            - Cosine of x (radians)
     tan <x>            - Tangent of x (radians)
   
   Memory Operations:
     store <value>      - Store value in memory
     recall             - Recall value from memory
     clear_memory       - Clear memory
   
   Utility Commands:
     history            - Show calculation history
     clear              - Clear history
     stats              - Show calculator statistics
     help               - Show this help
     quit               - Exit calculator
   """
       print(help_text)
   
   
   def parse_interactive_command(calc: Calculator, command: str) -> Optional[float]:
       """Parse and execute an interactive command."""
       parts = command.split()
       if not parts:
           return None
       
       cmd = parts[0].lower()
       
       try:
           if cmd == 'add' and len(parts) == 3:
               return calc.add(float(parts[1]), float(parts[2]))
           elif cmd == 'subtract' and len(parts) == 3:
               return calc.subtract(float(parts[1]), float(parts[2]))
           elif cmd == 'multiply' and len(parts) == 3:
               return calc.multiply(float(parts[1]), float(parts[2]))
           elif cmd == 'divide' and len(parts) == 3:
               return calc.divide(float(parts[1]), float(parts[2]))
           elif cmd == 'sqrt' and len(parts) == 2:
               return calc.square_root(float(parts[1]))
           elif cmd == 'power' and len(parts) == 3:
               return calc.power(float(parts[1]), float(parts[2]))
           elif cmd == 'sin' and len(parts) == 2:
               from .scientific import sin
               return sin(float(parts[1]))
           elif cmd == 'cos' and len(parts) == 2:
               from .scientific import cos
               return cos(float(parts[1]))
           elif cmd == 'tan' and len(parts) == 2:
               from .scientific import tan
               return tan(float(parts[1]))
           elif cmd == 'store' and len(parts) == 2:
               calc.memory_store(float(parts[1]))
               print(f"Stored {parts[1]} in memory")
               return None
           elif cmd == 'recall' and len(parts) == 1:
               return calc.memory_recall()
           elif cmd == 'clear_memory' and len(parts) == 1:
               calc.memory_clear()
               print("Memory cleared")
               return None
           else:
               print(f"Unknown command or wrong number of arguments: {command}")
               print("Type 'help' for available commands")
               return None
       except ValueError as e:
           print(f"Invalid number format: {e}")
           return None
   
   
   def print_history(calc: Calculator):
       """Print calculation history."""
       history = calc.get_history()
       if not history:
           print("No history available")
           return
       
       print("Calculation History:")
       for i, entry in enumerate(history, 1):
           print(f"  {i}. {entry}")
   
   
   def print_stats(calc: Calculator):
       """Print calculator statistics."""
       stats = calc.get_stats()
       print("Calculator Statistics:")
       for key, value in stats.items():
           print(f"  {key}: {value}")
   
   
   def main(args: Optional[List[str]] = None) -> int:
       """Main entry point for the CLI."""
       parser = create_parser()
       parsed_args = parser.parse_args(args)
       
       # Setup logging
       setup_logging(level=parsed_args.log_level)
       
       # Override precision if specified
       if parsed_args.precision is not None:
           config.calculator.precision = parsed_args.precision
       
       # Initialize calculator
       calc = Calculator()
       
       # Interactive mode
       if parsed_args.interactive:
           interactive_mode(calc)
           return 0
       
       # Operation mode
       if not parsed_args.operation:
           parser.print_help()
           return 1
       
       try:
           # Execute the requested operation
           if parsed_args.operation == 'add':
               result = calc.add(parsed_args.a, parsed_args.b)
           elif parsed_args.operation == 'subtract':
               result = calc.subtract(parsed_args.a, parsed_args.b)
           elif parsed_args.operation == 'multiply':
               result = calc.multiply(parsed_args.a, parsed_args.b)
           elif parsed_args.operation == 'divide':
               result = calc.divide(parsed_args.a, parsed_args.b)
           elif parsed_args.operation == 'sqrt':
               result = calc.square_root(parsed_args.x)
           elif parsed_args.operation == 'power':
               result = calc.power(parsed_args.base, parsed_args.exponent)
           elif parsed_args.operation == 'sin':
               from .scientific import sin
               result = sin(parsed_args.x)
           elif parsed_args.operation == 'cos':
               from .scientific import cos
               result = cos(parsed_args.x)
           elif parsed_args.operation == 'tan':
               from .scientific import tan
               result = tan(parsed_args.x)
           else:
               print(f"Unknown operation: {parsed_args.operation}")
               return 1
           
           print(result)
           return 0
           
       except Exception as e:
           print(f"Error: {e}")
           return 1
   
   
   if __name__ == '__main__':
       sys.exit(main())
   ```

## Part 2: Creating pyproject.toml

### Task 2.1: Define Package Metadata

1. Create `pyproject.toml`:
   ```toml
   [build-system]
   requires = ["setuptools>=61.0", "wheel"]
   build-backend = "setuptools.build_meta"
   
   [project]
   name = "calculator-pro"
   version = "1.0.0"
   description = "A professional calculator library with advanced features"
   readme = "README.md"
   license = {file = "LICENSE"}
   authors = [
       {name = "Your Name", email = "your.email@example.com"}
   ]
   maintainers = [
       {name = "Your Name", email = "your.email@example.com"}
   ]
   keywords = ["calculator", "math", "scientific", "computation"]
   classifiers = [
       "Development Status :: 5 - Production/Stable",
       "Intended Audience :: Developers",
       "Intended Audience :: Education",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
       "Programming Language :: Python :: 3",
       "Programming Language :: Python :: 3.10",
       "Programming Language :: Python :: 3.11",
       "Programming Language :: Python :: 3.12",
       "Topic :: Scientific/Engineering :: Mathematics",
       "Topic :: Software Development :: Libraries :: Python Modules",
       "Topic :: Utilities",
   ]
   requires-python = ">=3.10"
   dependencies = [
       "pydantic[dotenv]>=1.10.0",
       "cryptography>=3.4.0",
   ]
   
   [project.optional-dependencies]
   dev = [
       "pytest>=7.0.0",
       "pytest-cov>=4.0.0",
       "pytest-benchmark>=4.0.0",
       "black>=22.0.0",
       "pylint>=2.15.0",
       "mypy>=1.0.0",
       "pre-commit>=3.0.0",
       "tox>=4.0.0",
   ]
   test = [
       "pytest>=7.0.0",
       "pytest-cov>=4.0.0",
       "pytest-benchmark>=4.0.0",
   ]
   docs = [
       "sphinx>=5.0.0",
       "sphinx-rtd-theme>=1.0.0",
       "myst-parser>=0.18.0",
   ]
   
   [project.urls]
   Homepage = "https://github.com/yourusername/calculator-pro"
   Documentation = "https://calculator-pro.readthedocs.io/"
   Repository = "https://github.com/yourusername/calculator-pro.git"
   "Bug Tracker" = "https://github.com/yourusername/calculator-pro/issues"
   Changelog = "https://github.com/yourusername/calculator-pro/blob/main/CHANGELOG.md"
   
   [project.scripts]
   calculator = "calculator.cli:main"
   calc = "calculator.cli:main"
   
   [project.entry-points."calculator.plugins"]
   basic = "calculator.operations"
   scientific = "calculator.scientific"
   
   [tool.setuptools]
   package-dir = {"" = "src"}
   
   [tool.setuptools.packages.find]
   where = ["src"]
   
   [tool.setuptools.package-data]
   calculator = ["config/*.env", "py.typed"]
   
   [tool.black]
   line-length = 88
   target-version = ['py310', 'py311', 'py312']
   include = '\.pyi?$'
   exclude = '''
   /(
       \.git
     | \.hg
     | \.mypy_cache
     | \.tox
     | \.venv
     | _build
     | buck-out
     | build
     | dist
   )/
   '''
   
   [tool.mypy]
   python_version = "3.10"
   warn_return_any = true
   warn_unused_configs = true
   disallow_untyped_defs = true
   disallow_incomplete_defs = true
   check_untyped_defs = true
   disallow_untyped_decorators = true
   no_implicit_optional = true
   warn_redundant_casts = true
   warn_unused_ignores = true
   warn_no_return = true
   warn_unreachable = true
   strict_equality = true
   
   [tool.pytest.ini_options]
   minversion = "7.0"
   addopts = [
       "--strict-markers",
       "--strict-config",
       "--cov=calculator",
       "--cov-report=term-missing",
       "--cov-report=html",
       "--cov-report=xml",
   ]
   testpaths = ["tests"]
   markers = [
       "slow: marks tests as slow (deselect with '-m \"not slow\"')",
       "integration: marks tests as integration tests",
       "unit: marks tests as unit tests",
   ]
   
   [tool.coverage.run]
   source = ["src/calculator"]
   
   [tool.coverage.report]
   exclude_lines = [
       "pragma: no cover",
       "def __repr__",
       "if self.debug:",
       "if settings.DEBUG",
       "raise AssertionError",
       "raise NotImplementedError",
       "if 0:",
       "if __name__ == .__main__.:",
       "class .*\\bProtocol\):",
       "@(abc\\.)?abstractmethod",
   ]
   
   [tool.pylint.messages_control]
   disable = [
       "missing-docstring",
       "too-few-public-methods",
   ]
   
   [tool.pylint.format]
   max-line-length = 88
   ````