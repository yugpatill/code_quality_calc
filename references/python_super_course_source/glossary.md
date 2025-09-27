# Glossary of Python Development Terms

## Python Development Environments

**Python Interpreter**
: The program that reads and executes Python code. Python is an interpreted language, meaning code is executed line by line by the interpreter.

**Virtual Environment**
: An isolated Python environment that allows you to install packages for a specific project without affecting other projects or the system Python installation.

**venv**
: The standard library module for creating virtual environments in Python 3.3 and later.

**virtualenv**
: A third-party tool that predates venv and provides similar virtual environment functionality with some additional features.

**pip**
: The standard package manager for Python, used to install and manage packages from the Python Package Index (PyPI).

**PyPI (Python Package Index)**
: The official repository of Python packages, containing thousands of libraries that can be installed using pip.

**requirements.txt**
: A file that lists all the dependencies of a Python project, typically used with pip to install all required packages.

**setup.py**
: A Python file used to specify how a package should be installed, including its dependencies, metadata, and entry points.

## Code Quality and Testing

**Linter**
: A tool that analyzes source code to flag programming errors, bugs, stylistic errors, and suspicious constructs.

**Pylint**
: A popular Python linter that checks for errors, enforces coding standards, and looks for code smells.

**PEP 8**
: The style guide for Python code, providing conventions for formatting Python code for maximum readability.

**Unit Test**
: A test that checks a small, specific piece of functionality in isolation.

**Integration Test**
: A test that verifies that different parts of a system work together correctly.

**pytest**
: A testing framework for Python that makes it easy to write simple and scalable tests.

**Test Fixture**
: In pytest, a function that provides a fixed baseline for tests to run from, setting up any needed data or state.

**Test Coverage**
: A measure of how much of your code is executed during your tests, typically expressed as a percentage.

**TDD (Test-Driven Development)**
: A software development approach where tests are written before the code that needs to be tested.

## Version Control

**Git**
: A distributed version control system for tracking changes in source code during software development.

**Repository (Repo)**
: A storage location for a project containing all of its files and the revision history for each file.

**Commit**
: A snapshot of changes made to a repository at a specific point in time.

**Branch**
: A parallel version of a repository that allows you to work on different features or fixes without affecting the main codebase.

**Pull Request (PR)**
: A method of submitting contributions to a project, requesting that changes from one branch be pulled into another (typically the main branch).

**Merge Conflict**
: Occurs when Git can't automatically resolve differences in code between two commits.

**Atomic Commit**
: A commit that represents a single logical change to the codebase.

## Continuous Integration/Deployment

**CI/CD**
: Continuous Integration/Continuous Deployment, practices of automatically building, testing, and potentially deploying code changes.

**GitHub Actions**
: A CI/CD platform integrated with GitHub that automates workflows based on GitHub events.

**Workflow**
: In GitHub Actions, a configurable automated process made up of one or more jobs.

**Runner**
: A server that runs your GitHub Actions workflows.

**Pipeline**
: A defined set of stages for code to pass through from development to production.

## Python Project Structure

**Package**
: A directory containing Python modules and an `__init__.py` file.

**Module**
: A Python file containing definitions and statements.

**`__init__.py`**
: A file that marks a directory as a Python package, allowing it to be imported.

**Docstring**
: A string literal that appears as the first statement in a module, function, class, or method definition, used for documentation.

## IDE and Development Tools

**IDE (Integrated Development Environment)**
: Software that provides comprehensive facilities for software development, typically including a code editor, build tools, and debugger.

**VS Code**
: Visual Studio Code, a popular lightweight code editor with strong support for Python development through extensions.

**Debugger**
: A tool that helps find and fix bugs in software by executing code step by step and examining variables at runtime.

**Breakpoint**
: A designated point in code where execution will pause, allowing for inspection of the program state.

**Terminal/Shell**
: A text-based interface for entering commands to interact with the operating system.

**WSL (Windows Subsystem for Linux)**
: A compatibility layer for running Linux binary executables natively on Windows, useful for Python development in a Linux-like environment.

## Package Management Terminology

**Dependency**
: A software package that another package requires to function properly.

**Semantic Versioning**
: A versioning scheme in the format MAJOR.MINOR.PATCH, where each number has specific meaning regarding compatibility.

**Wheel**
: A built package format for Python that can be installed without requiring the build process that source distributions need.

**editable install**
: An installation mode (`pip install -e .`) that allows you to modify a package's source code without reinstalling it.

**lock file**
: A file that records the exact versions of all dependencies to ensure reproducible installations.

## Configuration Management

**Environment Variables**
: Key-value pairs stored outside the application code that configure application behavior, commonly used for settings that vary between environments.

**Configuration File**
: A file (TOML, YAML, JSON, INI) that contains application settings and can be modified without changing the code.

**pyproject.toml**
: A configuration file that follows PEP 518 standards for modern Python project configuration, replacing setup.py and consolidating tool configurations.

**Secrets Management**
: The practice of securely storing and accessing sensitive information like API keys, passwords, and tokens.

**Environment-specific Configuration**
: Different configuration values for different deployment environments (development, testing, production).

## Containerization

**Docker**
: A platform that packages applications and their dependencies into lightweight, portable containers.

**Container**
: A standardized unit of software that packages code and all its dependencies so the application runs quickly and reliably across computing environments.

**Dockerfile**
: A text file containing instructions for building a Docker image, specifying the base image, dependencies, and configuration.

**Docker Compose**
: A tool for defining and running multi-container Docker applications using a YAML file.

## Security

**Dependency Scanning**
: The process of analyzing project dependencies for known security vulnerabilities.

**pip-audit**
: Official Python tool for scanning installed packages for known security vulnerabilities.

**Bandit**
: A security linter for Python that identifies common security issues in code.

**CodeQL**
: GitHub's semantic code analysis engine for finding security vulnerabilities and code quality issues.


