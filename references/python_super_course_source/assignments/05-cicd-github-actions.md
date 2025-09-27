````markdown
# Assignment 5: CI/CD and Automation with GitHub Actions

## Learning Objectives
- Understand continuous integration and continuous deployment (CI/CD) concepts
- Set up automated testing and quality checks with GitHub Actions
- Implement security scanning and dependency management
- Create automated release workflows
- Apply DevOps best practices to Python projects

## Background

Continuous Integration/Continuous Deployment (CI/CD) automates the software development lifecycle from code changes to production deployment. This assignment will teach you to create professional automation workflows that are essential in modern software development teams.

### Historical Context

CI/CD practices evolved to address the challenges of manual testing and deployment:
- **1990s**: Manual testing and deployment caused delays and errors
- **Early 2000s**: Automated testing frameworks emerged (JUnit, pytest)
- **2010s**: Cloud-based CI services like Travis CI, Jenkins gained popularity
- **2018**: GitHub Actions launched, integrating CI/CD directly into GitHub
- **Present**: CI/CD is mandatory for professional development, with 90%+ of companies using automation

Modern teams deploy multiple times per day, which is only possible through automation.

## Prerequisites
- Completed Assignments 1-4
- GitHub repository with calculator project
- Basic understanding of YAML syntax
- Calculator project with tests and quality checks

## Time to Complete
Expect to spend approximately 3-4 hours on this assignment.

## Part 1: Setting Up Basic CI/CD Pipeline

### Task 1.1: Create Your First GitHub Actions Workflow

1. In your calculator repository, create the directory structure:
   ```bash
   mkdir -p .github/workflows
   ```

2. Create a basic CI workflow `.github/workflows/ci.yml`:
   ```yaml
   name: Continuous Integration
   
   on:
     push:
       branches: [ main, develop ]
     pull_request:
       branches: [ main ]
   
   permissions:
     contents: read
   
   jobs:
     test:
       runs-on: ubuntu-latest
       strategy:
         matrix:
           python-version: ['3.8', '3.10', '3.11']
       
       steps:
       - name: Checkout code
         uses: actions/checkout@v4
       
       - name: Set up Python ${{ matrix.python-version }}
         uses: actions/setup-python@v4
         with:
           python-version: ${{ matrix.python-version }}
           cache: 'pip'
       
       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install -e .
           pip install -r requirements-dev.txt
       
       - name: Run linting
         run: |
           pylint src tests
       
       - name: Run tests
         run: |
           pytest --cov=src --cov-report=xml --cov-report=term
       
       - name: Upload coverage to Codecov
         uses: codecov/codecov-action@v3
         if: matrix.python-version == '3.10'
         with:
           file: ./coverage.xml
           flags: unittests
   ```

3. Commit and push this workflow:
   ```bash
   git add .github/workflows/ci.yml
   git commit -m "feat: add CI workflow with testing and coverage"
   git push origin main
   ```

4. Go to your GitHub repository's "Actions" tab to see the workflow run.

### Task 1.2: Add Code Quality Checks

1. Create a separate quality workflow `.github/workflows/quality.yml`:
   ```yaml
   name: Code Quality
   
   on:
     push:
       branches: [ main, develop ]
     pull_request:
       branches: [ main ]
   
   jobs:
     quality:
       runs-on: ubuntu-latest
       
       steps:
       - name: Checkout code
         uses: actions/checkout@v4
       
       - name: Set up Python
         uses: actions/setup-python@v4
         with:
           python-version: '3.10'
           cache: 'pip'
       
       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install black isort flake8 mypy bandit safety
           pip install -e .
       
       - name: Check code formatting with Black
         run: |
           black --check src tests
       
       - name: Check import sorting with isort
         run: |
           isort --check-only src tests
       
       - name: Lint with flake8
         run: |
           flake8 src tests
       
       - name: Type checking with mypy
         run: |
           mypy src
         continue-on-error: true
       
       - name: Security analysis with bandit
         run: |
           bandit -r src/
       
       - name: Check for known security vulnerabilities
         run: |
           safety check
   ```

2. Update your `requirements-dev.txt` to include these tools:
   ```
   # Testing
   pytest>=7.0.0
   pytest-cov>=4.0.0
   
   # Code Quality
   pylint>=2.15.0
   black>=22.8.0
   isort>=5.10.0
   flake8>=5.0.0
   mypy>=0.991
   bandit>=1.7.0
   safety>=2.2.0
   
   # Type hints
   types-setuptools
   ```

## Part 2: Advanced CI/CD Features

### Task 2.1: Add Security Scanning

1. Create a security workflow `.github/workflows/security.yml`:
   ```yaml
   name: Security Scan
   
   on:
     push:
       branches: [ main ]
     pull_request:
       branches: [ main ]
     schedule:
       - cron: '0 0 * * 0'  # Weekly scan
   
   permissions:
     contents: read
     security-events: write
   
   jobs:
     codeql:
       name: CodeQL Analysis
       runs-on: ubuntu-latest
       
       steps:
       - name: Checkout repository
         uses: actions/checkout@v4
       
       - name: Initialize CodeQL
         uses: github/codeql-action/init@v2
         with:
           languages: python
       
       - name: Autobuild
         uses: github/codeql-action/autobuild@v2
       
       - name: Perform CodeQL Analysis
         uses: github/codeql-action/analyze@v2
   
     dependency-scan:
       name: Dependency Vulnerability Scan
       runs-on: ubuntu-latest
       
       steps:
       - name: Checkout code
         uses: actions/checkout@v4
       
       - name: Set up Python
         uses: actions/setup-python@v4
         with:
           python-version: '3.10'
       
       - name: Install pip-audit
         run: pip install pip-audit
       
       - name: Scan dependencies
         run: pip-audit --desc --format=json --output=audit-results.json
         continue-on-error: true
       
       - name: Upload audit results
         uses: actions/upload-artifact@v3
         if: always()
         with:
           name: audit-results
           path: audit-results.json
   ```

### Task 2.2: Create a Release Workflow

1. Create `.github/workflows/release.yml`:
   ```yaml
   name: Release
   
   on:
     push:
       tags:
         - 'v*'
   
   permissions:
     contents: write
   
   jobs:
     release:
       runs-on: ubuntu-latest
       
       steps:
       - name: Checkout code
         uses: actions/checkout@v4
       
       - name: Set up Python
         uses: actions/setup-python@v4
         with:
           python-version: '3.10'
       
       - name: Install build dependencies
         run: |
           python -m pip install --upgrade pip
           pip install build twine
       
       - name: Build package
         run: |
           python -m build
       
       - name: Create GitHub Release
         uses: softprops/action-gh-release@v1
         with:
           files: dist/*
           generate_release_notes: true
         env:
           GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
   ```

### Task 2.3: Add Performance Testing

1. Create a performance test file `tests/test_performance.py`:
   ```python
   """Performance tests for calculator operations."""
   import time
   import pytest
   from calculator.calculator import Calculator
   from calculator.operations import add, multiply
   
   
   def test_basic_operation_performance():
       """Test that basic operations complete quickly."""
       start_time = time.time()
       
       result = add(100, 200)
       
       end_time = time.time()
       execution_time = end_time - start_time
       
       assert execution_time < 0.001  # Should complete in less than 1ms
       assert result == 300
   
   
   def test_calculator_performance():
       """Test calculator class performance."""
       calc = Calculator()
       
       start_time = time.time()
       
       # Perform 1000 operations
       for i in range(1000):
           calc.add(i, i + 1)
       
       end_time = time.time()
       execution_time = end_time - start_time
       
       assert execution_time < 1.0  # Should complete in less than 1 second
       assert len(calc.get_history()) == 1000
   
   
   @pytest.mark.parametrize("operation_count", [100, 1000, 10000])
   def test_memory_usage_scaling(operation_count):
       """Test that memory usage scales reasonably."""
       import tracemalloc
       
       tracemalloc.start()
       
       calc = Calculator()
       for i in range(operation_count):
           calc.multiply(2, 3)
       
       current, peak = tracemalloc.get_traced_memory()
       tracemalloc.stop()
       
       # Memory should scale reasonably (less than 10KB per 1000 operations)
       memory_per_operation = peak / operation_count
       assert memory_per_operation < 10  # bytes per operation
   ```

2. Add performance testing to your CI workflow:
   ```yaml
   # Add this step to your ci.yml after the regular tests
   - name: Run performance tests
     run: |
       pytest tests/test_performance.py -v
   ```

## Part 3: Implementing Pre-commit Hooks

### Task 3.1: Set Up Pre-commit

1. Add pre-commit to your `requirements-dev.txt`:
   ```
   pre-commit>=2.20.0
   ```

2. Create `.pre-commit-config.yaml`:
   ```yaml
   repos:
     - repo: https://github.com/pre-commit/pre-commit-hooks
       rev: v4.4.0
       hooks:
         - id: trailing-whitespace
         - id: end-of-file-fixer
         - id: check-yaml
         - id: check-added-large-files
         - id: check-merge-conflict
   
     - repo: https://github.com/psf/black
       rev: 22.10.0
       hooks:
         - id: black
           language_version: python3
   
     - repo: https://github.com/pycqa/isort
       rev: 5.10.1
       hooks:
         - id: isort
   
     - repo: https://github.com/pycqa/flake8
       rev: 5.0.4
       hooks:
         - id: flake8
   
     - repo: https://github.com/pre-commit/mirrors-mypy
       rev: v0.991
       hooks:
         - id: mypy
           additional_dependencies: [types-setuptools]
   ```

3. Install and set up pre-commit:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

4. Test the hooks:
   ```bash
   pre-commit run --all-files
   ```

### Task 3.2: Create Development Scripts

1. Create a `scripts/` directory with development utilities:
   ```bash
   mkdir scripts
   ```

2. Create `scripts/setup-dev.sh`:
   ```bash
   #!/bin/bash
   # Development environment setup script
   
   set -e
   
   echo "Setting up development environment..."
   
   # Create virtual environment if it doesn't exist
   if [ ! -d "venv" ]; then
       python3 -m venv venv
   fi
   
   # Activate virtual environment
   source venv/bin/activate
   
   # Upgrade pip
   pip install --upgrade pip
   
   # Install development dependencies
   pip install -r requirements-dev.txt
   pip install -e .
   
   # Set up pre-commit hooks
   pre-commit install
   
   echo "Development environment setup complete!"
   echo "Run 'source venv/bin/activate' to activate the environment."
   ```

3. Create `scripts/run-tests.sh`:
   ```bash
   #!/bin/bash
   # Comprehensive test script
   
   set -e
   
   echo "Running comprehensive test suite..."
   
   # Code formatting
   echo "Checking code formatting..."
   black --check src tests
   isort --check-only src tests
   
   # Linting
   echo "Running linters..."
   flake8 src tests
   pylint src tests
   
   # Type checking
   echo "Type checking..."
   mypy src
   
   # Security checks
   echo "Security analysis..."
   bandit -r src/
   safety check
   
   # Unit tests with coverage
   echo "Running tests with coverage..."
   pytest --cov=src --cov-report=html --cov-report=term
   
   echo "All checks passed!"
   ```

4. Make scripts executable:
   ```bash
   chmod +x scripts/*.sh
   ```

## Part 4: Documentation and Deployment

### Task 4.1: Automated Documentation

1. Add documentation dependencies to `requirements-dev.txt`:
   ```
   # Documentation
   sphinx>=5.0.0
   sphinx-rtd-theme>=1.0.0
   ```

2. Create a documentation workflow `.github/workflows/docs.yml`:
   ```yaml
   name: Documentation
   
   on:
     push:
       branches: [ main ]
     pull_request:
       branches: [ main ]
   
   jobs:
     docs:
       runs-on: ubuntu-latest
       
       steps:
       - name: Checkout code
         uses: actions/checkout@v4
       
       - name: Set up Python
         uses: actions/setup-python@v4
         with:
           python-version: '3.10'
       
       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install -e .
           pip install sphinx sphinx-rtd-theme
       
       - name: Build documentation
         run: |
           cd docs
           make html
       
       - name: Deploy to GitHub Pages
         uses: peaceiris/actions-gh-pages@v3
         if: github.ref == 'refs/heads/main'
         with:
           github_token: ${{ secrets.GITHUB_TOKEN }}
           publish_dir: ./docs/_build/html
   ```

### Task 4.2: Environment-Specific Deployments

1. Create deployment configuration in `.github/workflows/deploy.yml`:
   ```yaml
   name: Deploy
   
   on:
     push:
       branches: [ main ]
     release:
       types: [ published ]
   
   jobs:
     deploy-staging:
       if: github.ref == 'refs/heads/main'
       runs-on: ubuntu-latest
       environment: staging
       
       steps:
       - name: Checkout code
         uses: actions/checkout@v4
       
       - name: Deploy to staging
         run: |
           echo "Deploying to staging environment..."
           # Add your staging deployment commands here
   
     deploy-production:
       if: github.event_name == 'release'
       runs-on: ubuntu-latest
       environment: production
       needs: [deploy-staging]
       
       steps:
       - name: Checkout code
         uses: actions/checkout@v4
       
       - name: Deploy to production
         run: |
           echo "Deploying to production environment..."
           # Add your production deployment commands here
   ```

## Part 5: Monitoring and Notifications

### Task 5.1: Set Up Status Badges

1. Update your `README.md` to include status badges:
   ```markdown
   # Calculator Project
   
   ![CI](https://github.com/yourusername/python_calculator/workflows/Continuous%20Integration/badge.svg)
   ![Quality](https://github.com/yourusername/python_calculator/workflows/Code%20Quality/badge.svg)
   ![Security](https://github.com/yourusername/python_calculator/workflows/Security%20Scan/badge.svg)
   [![codecov](https://codecov.io/gh/yourusername/python_calculator/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/python_calculator)
   
   A professional-grade calculator application built with Python, demonstrating modern software development practices.
   ```

### Task 5.2: Configure Notifications

1. Add notification settings to your workflows:
   ```yaml
   # Add this to any workflow for Slack notifications
   - name: Notify on failure
     if: failure()
     uses: 8398a7/action-slack@v3
     with:
       status: failure
       channel: '#dev-alerts'
       webhook_url: ${{ secrets.SLACK_WEBHOOK }}
   ```

## Common Pitfalls

- **Workflow file syntax errors**: YAML is sensitive to indentation and formatting
- **Missing permissions**: Ensure workflows have necessary permissions for their actions
- **Secrets management**: Never commit sensitive information; use GitHub Secrets
- **Resource limits**: Be mindful of GitHub Actions usage limits
- **Dependency conflicts**: Pin action versions to avoid breaking changes
- **Test environment differences**: Ensure CI environment matches local development

## Troubleshooting

### Issue: Workflow Not Triggering

**Solution:**
- Check file location: Must be in `.github/workflows/`
- Verify YAML syntax
- Ensure trigger conditions are met

### Issue: Permission Denied Errors

**Solution:**
- Add necessary permissions to workflow:
  ```yaml
  permissions:
    contents: read
    pull-requests: write
    security-events: write
  ```

### Issue: Tests Passing Locally but Failing in CI

**Solution:**
- Check environment differences
- Ensure all dependencies are in requirements files
- Verify file paths are correct
- Check for timing-sensitive tests

## What Success Looks Like

By the end of this assignment, you should have:
- A complete CI/CD pipeline that automatically tests, analyzes, and deploys your code
- Automated security scanning and dependency management
- Pre-commit hooks preventing low-quality code from being committed
- Performance testing to catch regressions
- Professional-grade automation workflows used in industry

## Self-Assessment Questions

1. How does CI/CD improve software quality and development velocity?
2. What security practices have you implemented in your pipeline?
3. How would you modify these workflows for a larger team?
4. What would you add to handle database migrations or infrastructure changes?
5. How do these automation practices relate to DevOps culture?
6. What monitoring and alerting would you add for a production system?

## Submission Requirements

Submit the following:

1. Your complete GitHub repository with all CI/CD workflows
2. Screenshots of successful workflow runs in GitHub Actions
3. Evidence of status badges on your README
4. A reflection document (500-750 words) addressing:
   - How automation changes your development process
   - What challenges you faced setting up CI/CD
   - How you would adapt these practices for different types of projects
   - The business value of automated testing and deployment

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Awesome Actions](https://github.com/sdras/awesome-actions) - Community action collection
- [CI/CD Best Practices](https://about.gitlab.com/topics/ci-cd/)
- [The DevOps Handbook](https://itrevolution.com/the-devops-handbook/) - Comprehensive DevOps guide
- [Continuous Delivery: Reliable Software Releases](https://continuousdelivery.com/) - Classic CI/CD book

````