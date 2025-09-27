# Automation with GitHub Actions

This guide explains how to set up continuous integration using GitHub Actions.

## Understanding GitHub Actions

GitHub Actions is a CI/CD platform that allows you to automate your build, test, and deployment pipelines directly from GitHub.

Key components:
- **Workflows**: Automated procedures made up of one or more jobs
- **Jobs**: Sets of steps that execute on the same runner
- **Steps**: Individual tasks that run commands in a job
- **Actions**: Standalone commands combined into steps to create a job
- **Runners**: Servers that run your workflows

## Setting Up Your First Workflow

1. Create a `.github/workflows` directory in your repository
2. Add a YAML file (e.g., `main.yml`) to define your workflow

Example workflow file:

```yaml
name: Python Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
        pip install pytest pylint
    
    - name: Lint with pylint
      run: |
        pylint $(git ls-files '*.py')
    
    - name: Test with pytest
      run: |
        pytest
```

## Workflow Triggers

GitHub Actions workflows can be triggered by various events:

- **push**: When code is pushed to the repository
- **pull_request**: When a PR is opened, updated, or closed
- **schedule**: At scheduled times using cron syntax
- **workflow_dispatch**: Manually triggered by a user
- **repository_dispatch**: Triggered by external events

## Viewing Workflow Results

1. Go to your GitHub repository
2. Click on the "Actions" tab
3. Select the workflow run to view details
4. Check the logs for each job and step

## Common GitHub Actions for Python Projects

- **actions/checkout**: Check out your repository code
- **actions/setup-python**: Set up a Python environment
- **pip install**: Install dependencies
- **pytest**: Run tests
- **pylint/flake8**: Check code quality
- **codecov/codecov-action**: Upload coverage reports
- **pypa/gh-action-pypi-publish**: Publish packages to PyPI

## Advanced Configurations

### Matrix Testing

Test across multiple Python versions:

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10']
    
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}
```

### Caching Dependencies

Speed up workflows by caching pip packages:

```yaml
steps:
- uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

### Security Scanning and Best Practices

Modern CI/CD pipelines should include security scanning to identify vulnerabilities early.

#### Dependency Scanning

Add security scanning to your workflow:

```yaml
name: Security and Quality Checks

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  security:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pip-audit safety bandit
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    
    - name: Run pip-audit for dependency vulnerabilities
      run: |
        pip-audit
    
    - name: Run Safety check
      run: |
        safety check
    
    - name: Run Bandit for security issues
      run: |
        bandit -r src/ -f json -o bandit-report.json
    
    - name: Upload Bandit results
      uses: actions/upload-artifact@v3
      if: always()
      with:
        name: bandit-results
        path: bandit-report.json
```

#### Code Quality and Security with CodeQL

GitHub's CodeQL can analyze your code for security vulnerabilities:

```yaml
name: CodeQL Analysis

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 0 * * 0'  # Weekly scan

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language: [ 'python' ]

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Initialize CodeQL
      uses: github/codeql-action/init@v2
      with:
        languages: ${{ matrix.language }}

    - name: Autobuild
      uses: github/codeql-action/autobuild@v2

    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v2
```

#### Secrets Scanning

Never commit secrets to your repository. Use GitHub's secret scanning and Dependabot:

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
    reviewers:
      - "your-username"
    assignees:
      - "your-username"
```

#### Security Best Practices in Actions

1. **Pin action versions**: Use specific commit SHAs instead of tags
   ```yaml
   # Good: Pinned to specific commit
   - uses: actions/checkout@8e5e7e5ab8b370d6c329ec480221332ada57f0ab
   
   # Acceptable: Major version pinning
   - uses: actions/checkout@v3
   
   # Avoid: Latest or floating tags
   - uses: actions/checkout@main
   ```

2. **Limit permissions**: Use minimum required permissions
   ```yaml
   jobs:
     test:
       runs-on: ubuntu-latest
       permissions:
         contents: read
         pull-requests: write
   ```

3. **Use secrets for sensitive data**:
   ```yaml
   - name: Deploy to production
     env:
       API_KEY: ${{ secrets.PRODUCTION_API_KEY }}
       DATABASE_URL: ${{ secrets.DATABASE_URL }}
     run: |
       python deploy.py
   ```

4. **Validate inputs**: Always validate external inputs
   ```yaml
   - name: Run user command
     run: |
       if [[ "${{ github.event.inputs.command }}" =~ ^[a-zA-Z0-9_-]+$ ]]; then
         echo "Valid command: ${{ github.event.inputs.command }}"
       else
         echo "Invalid command format"
         exit 1
       fi
   ```

### Complete Secure Workflow Example

```yaml
name: Secure Python CI/CD

on:
  push:
    branches: [ main ]
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
      uses: actions/checkout@8e5e7e5ab8b370d6c329ec480221332ada57f0ab
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@61a6322f88396a6271a6ee3565807d608ecaddd1
      with:
        python-version: ${{ matrix.python-version }}
        cache: 'pip'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    
    - name: Security audit
      run: |
        pip-audit --desc
    
    - name: Lint with pylint
      run: |
        pylint src tests
    
    - name: Security analysis with bandit
      run: |
        bandit -r src/
    
    - name: Test with pytest
      run: |
        pytest --cov=src --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@eaaf4bedf32dbdc6b720b63067d99c4d77d6047d
      with:
        file: ./coverage.xml
        flags: unittests
        name: codecov-umbrella
        fail_ci_if_error: false

  security-scan:
    runs-on: ubuntu-latest
    if: github.event_name == 'push'
    
    steps:
    - name: Checkout code
      uses: actions/checkout@8e5e7e5ab8b370d6c329ec480221332ada57f0ab
    
    - name: Run Trivy vulnerability scanner
      uses: aquasecurity/trivy-action@9ab158e8597f3b310480b9a69402b419bc03dbd5
      with:
        scan-type: 'fs'
        scan-ref: '.'
        format: 'sarif'
        output: 'trivy-results.sarif'
    
    - name: Upload Trivy scan results to GitHub Security tab
      uses: github/codeql-action/upload-sarif@32dc499307d133bb5085bae78498c0ac2cf762d5
      if: always()
      with:
        sarif_file: 'trivy-results.sarif'
```

## Security Best Practices

- Use secrets for sensitive information
- Limit permissions in workflow files
- Pin action versions to specific commits

## Further Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Marketplace for Actions](https://github.com/marketplace?type=actions)
- [GitHub Actions Community Forum](https://github.community/c/actions/41)
