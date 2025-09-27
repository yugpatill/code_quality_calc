# Project Setup

This guide will walk you through setting up your Python development environment across different platforms.

## Python: A Brief History

Python was created by Guido van Rossum and first released in 1991. Its design philosophy emphasizes code readability with its notable use of significant whitespace.

- **Python 2 vs Python 3**: Python 3, released in 2008, intentionally broke backward compatibility to address fundamental design flaws. Python 2 reached end-of-life on January 1, 2020, and is no longer maintained.
- **Recommended Version**: This guide assumes Python >= 3.10, which includes modern features like improved type hints, structural pattern matching, and better error messages.

## Installing Python

### Windows
1. Download the installer from [python.org](https://www.python.org/downloads/windows/)
2. Run the installer, check "Add Python to PATH"
3. Click "Install Now"

### macOS
1. Option 1: Download from [python.org](https://www.python.org/downloads/macos/)
2. Option 2: Use Homebrew:
   ```bash
   brew install python
   ```

### Linux
Most Linux distributions come with Python pre-installed. To install or update:

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Fedora
sudo dnf install python3 python3-pip
```

## Setting Up Windows Subsystem for Linux (WSL2)

WSL2 provides a Linux environment on Windows, which is excellent for Python development.

### Historical Context
WSL was introduced by Microsoft in 2016 as part of their embrace of open-source technology. WSL2, released in 2019, uses a real Linux kernel and offers significantly better performance and compatibility than the original WSL.

1. Open PowerShell as Administrator and run:
   ```powershell
   wsl --install
   ```

2. Restart your computer

3. Set up Ubuntu (or your chosen distribution):
   ```bash
   # Update packages
   sudo apt update && sudo apt upgrade

   # Install Python development tools
   sudo apt install python3-pip python3-venv
   ```

4. Verify installation:
   ```bash
   python3 --version
   pip3 --version
   ```

## Virtual Environments: Solving Dependency Conflicts

### Historical Context
Before virtual environments, Python developers faced "dependency hell" - when different projects required conflicting versions of the same package. Virtual environments, introduced with `virtualenv` in 2007 and later integrated into Python as `venv` (Python 3.3+), solved this problem by creating isolated Python environments for each project.

### Creating a Virtual Environment

```bash
# Navigate to your project directory
cd your-project-directory

# Create a virtual environment
## On Windows with WSL2, macOS, or Linux:
python3 -m venv venv

## On Windows (PowerShell or Command Prompt):
python -m venv venv
```

### Activating the Virtual Environment

```bash
# On Windows with WSL2, macOS, or Linux:
source venv/bin/activate

# On Windows Command Prompt:
venv\Scripts\activate

# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
```

When the virtual environment is active, you'll see `(venv)` in your command prompt.

### Installing Dependencies

```bash
# Install project dependencies
pip install -r requirements.txt

# If you don't have a requirements.txt, install packages individually:
pip install pytest pylint
```

## Package Management Evolution

Package management in Python has evolved significantly:
- **Distutils** (1998): Basic distribution utilities
- **Setuptools/Easy Install** (2004): Extended distutils with dependency resolution
- **Pip** (2008): Replaced Easy Install, offering better dependency resolution and uninstallation
- **Pipenv/Poetry** (2017+): Modern tools combining dependency management and virtual environments

### Understanding Semantic Versioning

Python packages generally follow Semantic Versioning (SemVer):

```
MAJOR.MINOR.PATCH
```

- **MAJOR**: Incompatible API changes
- **MINOR**: Add functionality (backward-compatible)
- **PATCH**: Bug fixes (backward-compatible)

### Version Specifiers in requirements.txt

```
# Exact version
requests==2.28.1

# Minimum version
requests>=2.28.1

# Compatible release (same as >=2.28.1,<2.29.0)
requests~=2.28.1

# Greater than or equal to 2.28.1 AND less than 2.30.0
requests>=2.28.1,<2.30.0

# Not equal to
requests!=2.29.0
```

### Dependency Security

Modern development requires attention to dependency security:

#### Security Scanning Tools

1. **pip-audit**: Official tool for scanning Python packages for known vulnerabilities
   ```bash
   # Install pip-audit
   pip install pip-audit
   
   # Scan your current environment
   pip-audit
   
   # Scan a requirements file
   pip-audit -r requirements.txt
   ```

2. **Safety**: Alternative security scanner
   ```bash
   pip install safety
   safety check
   ```

#### Security Best Practices

- **Regular updates**: Keep dependencies updated, but test thoroughly
- **Pinned versions**: Use exact versions in production for reproducibility
- **Minimal dependencies**: Only include packages you actually need
- **Monitor advisories**: Subscribe to security advisories for your dependencies
- **Lock files**: Use tools like `pip-tools` to generate lock files with exact versions

#### Generating Lock Files with pip-tools

```bash
# Install pip-tools
pip install pip-tools

# Create requirements.in with your direct dependencies
echo "requests>=2.28.0" > requirements.in

# Generate pinned requirements.txt
pip-compile requirements.in

# Install from the lock file
pip-sync requirements.txt
```

### Creating a requirements.txt File

```bash
# Generate requirements.txt from your current environment
pip freeze > requirements.txt
```

### Modern Python Packaging with pyproject.toml

While `setup.py` and `requirements.txt` are still widely used, modern Python projects increasingly use `pyproject.toml` for configuration. This file follows the PEP 518 standard and provides a more declarative approach to project configuration.

#### Creating a pyproject.toml File

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "calculator"
version = "0.1.0"
description = "A simple calculator for learning Python development practices"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.10"
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Education",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]
dependencies = [
    # Runtime dependencies go here
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "pylint>=2.15.0",
    "black>=22.8.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "--cov=src --cov-report=html --cov-report=term"

[tool.pylint.main]
py-version = "3.10"

[tool.black]
line-length = 88
target-version = ['py310']
```

#### Benefits of pyproject.toml

- **Single configuration file**: Replaces multiple configuration files
- **Tool configuration**: Can configure pytest, pylint, black, and other tools
- **PEP 517/518 compliance**: Modern Python packaging standard
- **Better dependency management**: Separates runtime and development dependencies

#### Installing with pyproject.toml

```bash
# Install the project in development mode
pip install -e .

# Install with development dependencies
pip install -e ".[dev]"
```

### Deactivating the Virtual Environment

When you're done working on your project:

```bash
deactivate
```

## Git Configuration

If you haven't set up Git yet:

```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize a new Git repository (if needed)
git init

# Create a .gitignore file
touch .gitignore
```

Example content for `.gitignore`:
```
# Virtual Environment
venv/
env/
.env/

# Python cache files
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/

# Distribution / packaging
dist/
build/
*.egg-info/

# Coverage reports
htmlcov/
.coverage
.coverage.*
coverage.xml
*.cover

# VS Code
.vscode/
!.vscode/settings.json.example
!.vscode/launch.json.example

# PyCharm
.idea/

# Jupyter Notebook
.ipynb_checkpoints
```

## Real-World Scenarios

### Scenario 1: Joining an Existing Project Team

```bash
# Clone the repository
git clone https://github.com/company/project.git
cd project

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Or appropriate command for your OS

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (if separate)
pip install -r requirements-dev.txt

# Run tests to verify setup
pytest
```

### Scenario 2: Managing Multiple Python Versions

Using `pyenv` (a Python version manager):

```bash
# Install pyenv
# On macOS:
brew install pyenv

# On Linux:
curl https://pyenv.run | bash

# Install specific Python versions
pyenv install 3.8.12
pyenv install 3.10.4

# Set global Python version
pyenv global 3.10.4

# Set project-specific Python version
cd my-project
pyenv local 3.8.12
```

### Scenario 3: Debugging Environment Differences

When your code works locally but fails in production:

1. **Create a clean environment**: Set up a fresh virtual environment
2. **Use a lock file**: Generate a detailed requirements file with exact versions
   ```bash
   pip freeze > requirements-lock.txt
   ```
3. **Compare environments**: Use `pip list` in both environments and compare outputs
4. **Check Python versions**: Ensure versions match using `python --version`
5. **Consider containerization**: Use Docker to ensure environment consistency

### Introduction to Containerization

Containers solve the "it works on my machine" problem by packaging your application with all its dependencies and runtime environment.

#### Why Containers Matter

- **Consistency**: Same environment across development, testing, and production
- **Isolation**: Applications don't interfere with each other
- **Portability**: Run anywhere that supports containers
- **Reproducibility**: Exact same environment every time

#### Docker Basics for Python Projects

Docker is the most popular containerization platform. Here's a simple Dockerfile for a Python project:

```dockerfile
# Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/
COPY tests/ ./tests/

# Install the application
RUN pip install -e .

# Set the default command
CMD ["python", "-m", "calculator"]
```

#### Using Docker Compose for Development

Docker Compose simplifies multi-container applications:

```yaml
# docker-compose.yml
version: '3.8'

services:
  calculator:
    build: .
    volumes:
      - .:/app
    environment:
      - PYTHONPATH=/app/src
      - DEBUG=True
    ports:
      - "8000:8000"
    
  test:
    build: .
    command: pytest
    volumes:
      - .:/app
    environment:
      - PYTHONPATH=/app/src
```

#### Basic Docker Commands

```bash
# Build the image
docker build -t calculator:latest .

# Run the container
docker run -it calculator:latest

# Run with volume mounting for development
docker run -it -v $(pwd):/app calculator:latest

# Using Docker Compose
docker-compose up --build
docker-compose run test
```

#### When to Consider Containerization

- **Team consistency**: Multiple developers need identical environments
- **Complex dependencies**: System-level dependencies beyond Python packages
- **Production deployment**: Ensuring production matches development
- **CI/CD pipelines**: Consistent test environments
- **Microservices**: When building distributed applications

#### Container Best Practices

- **Multi-stage builds**: Separate build and runtime environments
- **Minimal base images**: Use slim or alpine variants
- **Security scanning**: Scan images for vulnerabilities
- **Layer optimization**: Order Dockerfile commands for optimal caching
- **Non-root users**: Don't run containers as root in production

## Troubleshooting Common Issues

### Python Command Not Found

**Windows:**
- Ensure Python is added to PATH during installation
- Try using `py` instead of `python`

**macOS/Linux:**
- Use `python3` instead of `python`
- Verify installation with `which python3`

### Permission Issues (macOS/Linux)

If you get permission errors:
```bash
# Use the --user flag
pip install --user package_name

# Or use a virtual environment (recommended)
```

### WSL2 File System Performance

For best performance with WSL2:
- Store your project files in the Linux file system (`/home/username/`)
- Access them in Windows via `\\wsl$\Ubuntu\home\username\`

## Next Steps

- Check out the [VS Code Integration Guide](06-vscode-setup.md) to set up your editor
- Learn about best practices in the [Development Workflow](02-development-workflow.md) guide
- Master Git workflows in the [Git Best Practices](07-git-best-practices.md) guide
