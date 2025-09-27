# Student Python Development Guide

## Overview
A comprehensive guide designed for college students learning modern Python development tools and best practices. This repository serves as both a reference and a hands-on learning resource to help you build professional software engineering skills.

## Learning Objectives

After completing this guide, you will be able to:
- Set up and manage professional Python development environments
- Apply industry-standard code quality practices to Python projects
- Write effective automated tests using pytest
- Implement professional Git workflows for version control
- Configure continuous integration pipelines with GitHub Actions
- Use VS Code effectively for Python development
- Manage modern configuration, logging, and secrets
- Package and distribute Python applications professionally
- Deploy applications to production with monitoring

## Documentation

This repository contains detailed documentation organized into the following sections:

- [📚 Project Documentation Home](docs/README.md) - Start here for an overview of all documentation
- [🎯 Introduction and Concepts](docs/00-introduction-and-concepts.md) - Professional development mindset and fundamental concepts
- [🚀 Project Setup](docs/01-project-setup.md) - Step-by-step instructions for setting up Python virtual environments and managing dependencies
- [⚙️ Development Workflow](docs/02-development-workflow.md) - Best practices for writing, organizing, and maintaining Python code
- [🧪 Testing with pytest](docs/03-testing.md) - How to write effective tests and implement test-driven development
- [✅ Code Quality with pylint](docs/04-code-quality.md) - Tools and techniques to ensure your code follows Python standards
- [🔄 Automation with GitHub Actions](docs/05-github-actions.md) - Setting up continuous integration pipelines for your projects
- [💻 VS Code Integration](docs/06-vscode-setup.md) - Setting up VS Code for Python development across Windows, macOS, and Linux
- [📝 Git Best Practices](docs/07-git-best-practices.md) - Professional Git workflows including atomic commits and branching strategies
- [⚙️ Configuration Management](docs/08-configuration-management.md) - Modern configuration patterns, environment variables, and secrets management

## The Python Calculator Project

Throughout the assignments in this guide, you'll build a professional-grade calculator application that evolves from simple functions to a complete production-ready system. This progression demonstrates how modern software is developed:

**Foundation Setup (Assignment 0):**
- Professional development environment and mindset establishment
- Essential tool configuration and workflow foundation

**Foundation Assignments (1-4):**
- Setting up proper development environments
- Implementing test-driven development
- Ensuring code quality through linting
- Using professional Git workflows

**Professional Development (Assignments 5-8):**
- Implementing continuous integration and deployment
- Modern configuration management and secrets handling
- Python packaging and distribution to PyPI
- Production deployment with containerization and monitoring

By the end, you'll have a fully functional calculator with basic and scientific operations, memory management, a command-line interface, web API, comprehensive testing, CI/CD pipeline, and production deployment capabilities.

## Progressive Learning Path

The assignments follow a deliberate progression that mirrors complete professional software development lifecycles:

0. **Environment Setup** → Professional development environment and mindset
1. **Environment Management** → Virtual environments and dependency management
2. **Code Quality** → Professional coding standards and documentation
3. **Testing** → Test-driven development and automated testing
4. **Version Control** → Professional Git workflows and collaboration
5. **CI/CD** → Automated testing, security scanning, and deployment
6. **Configuration** → Environment management, logging, and secrets
7. **Packaging** → Modern Python packaging and PyPI distribution
8. **Deployment** → Production-ready deployment with monitoring

Each assignment builds directly on the previous one, creating a complete software development journey from initial setup to production deployment.

## Hands-on Assignments

The best way to learn is by doing! Complete these practical assignments to build real-world skills:

**Foundation Setup:**
- [**Assignment 0: Professional Development Environment Setup**](assignments/00-environment-setup.md) (3-4 hours)  
  Set up your complete professional development environment, configure essential tools, and establish professional workflows and mindset.

**Foundation Assignments (1-4):**
- [**Assignment 1: Virtual Environments and Pip**](assignments/01-virtual-env-pip.md) (2-3 hours)  
  Set up your development environment and create the basic calculator structure with addition and subtraction operations.

- [**Assignment 2: Code Quality with Pylint**](assignments/02-pylint-code-quality.md) (2-3 hours)  
  Apply code quality standards to your existing calculator code and improve its structure and documentation.

- [**Assignment 3: Testing with Pytest**](assignments/03-pytest.md) (3-4 hours)  
  Add comprehensive tests for your calculator and use test-driven development to implement multiplication and division features.

- [**Assignment 4: Professional Git Workflows**](assignments/04-git-workflows.md) (3-4 hours)  
  Use Git branching strategies to implement scientific calculator features (square root, power, etc.) and manage the project professionally.

**Professional Development Assignments (5-8):**
- [**Assignment 5: CI/CD with GitHub Actions**](assignments/05-cicd-github-actions.md) (3-4 hours)  
  Implement automated testing, security scanning, and deployment pipelines using GitHub Actions.

- [**Assignment 6: Configuration Management**](assignments/06-configuration-management.md) (3-4 hours)  
  Add professional configuration management, environment-specific settings, logging, and secrets management.

- [**Assignment 7: Python Packaging and Distribution**](assignments/07-packaging-distribution.md) (3-4 hours)  
  Package your calculator for distribution with modern pyproject.toml, publish to PyPI, and create command-line interfaces.

- [**Assignment 8: CLI Interface and Production Deployment**](assignments/08-cli-deployment.md) (4-5 hours)  
  Build advanced CLI features, containerize with Docker, implement monitoring, and deploy to production environments.

Each assignment includes detailed instructions, example code, and reflection questions to deepen your understanding.

## Prerequisites

This guide assumes:
- Basic familiarity with Python syntax (variables, functions, conditionals)
- Access to a computer where you can install software
- Ability to use a command-line terminal (basic commands)
- No prior experience with virtual environments, testing, or version control is required

## Quick Start for Experienced Developers

If you're already familiar with some concepts, feel free to jump to specific sections:

1. Already comfortable with virtual environments? Start with [Assignment 2](assignments/02-pylint-code-quality.md).
2. Know Python and linting already? Jump to [Assignment 3](assignments/03-pytest.md).
3. Experienced with most tools but want to learn Git workflows? Go straight to [Assignment 4](assignments/04-git-workflows.md).
4. Ready for advanced topics? Skip to [Assignment 5](assignments/05-cicd-github-actions.md) for CI/CD.
5. Want to learn modern packaging? Jump to [Assignment 7](assignments/07-packaging-distribution.md).
6. Interested in production deployment? Go to [Assignment 8](assignments/08-cli-deployment.md).

## Who This Guide Is For

This guide is ideal for:
- College students studying computer science or software engineering
- Self-taught programmers looking to adopt professional practices
- Junior developers wanting to improve their development workflow
- Anyone transitioning from casual Python coding to professional development

## How to Measure Your Progress

Each assignment includes:
- ✅ Clear completion criteria
- 🧠 Reflection questions to deepen understanding
- 🔄 Opportunities to apply concepts to your own projects

Consider keeping a learning journal as you work through these assignments to track your growth and insights.

## What Success Looks Like

By the end of this guide, you will have:
- A fully functional calculator application with basic and scientific operations
- A professional command-line interface with interactive and batch modes
- A web API with health checks and monitoring capabilities
- A clean, well-documented codebase that passes industry-standard quality checks
- A comprehensive test suite with high coverage and performance benchmarks
- Modern configuration management with environment-specific settings
- A distributable Python package published to PyPI
- Production-ready deployment with Docker containerization
- Complete CI/CD pipeline with automated testing and security scanning
- Hands-on experience with the same workflows used in professional software teams

## Common Pitfalls to Avoid

- Forgetting to activate your virtual environment before installing packages
- Running tests from the wrong directory
- Committing sensitive information to Git
- Installing packages globally when they should be in the virtual environment
- Not following naming conventions for test files (they should start with `test_`)
- Ignoring linter warnings instead of addressing them

## Platform Support

This guide provides instructions for:
- **Windows** with WSL2 (Windows Subsystem for Linux)
- **macOS** using Terminal
- **Linux** distributions (Ubuntu, Debian, etc.)

## Getting Started

Follow these steps to begin your learning journey:

```bash
# Clone the repository
git clone https://github.com/kaw393939/student_python_dev_guide.git

# Navigate to the project directory
cd student_python_dev_guide

# Set up virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows with WSL2 or Linux:
source venv/bin/activate
# On Windows Command Prompt:
venv\Scripts\activate
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# On macOS:
source venv/bin/activate

# Install dependencies (if applicable)
pip install -r requirements.txt
```

For detailed setup instructions, see our [Assignment 0: Environment Setup](assignments/00-environment-setup.md), [Project Setup Guide](docs/01-project-setup.md) and [VS Code Integration Guide](docs/06-vscode-setup.md).

## Purpose

This guide is designed for college students aiming to develop professional software engineering skills with Python. You'll learn:

- **Virtual Environments**: Create isolated development environments to avoid dependency conflicts
- **Package Management**: Use pip effectively to manage project dependencies
- **Testing**: Write automated tests to verify your code works correctly
- **Code Quality**: Follow industry standards for clean, maintainable code
- **CI/CD**: Implement continuous integration workflows using GitHub Actions
- **Version Control**: Master Git workflows and collaborative development

These skills are essential for internships, jobs, and personal projects, giving you a competitive edge in the software development industry.

## Job Market Relevance

The practices taught in this guide are specifically chosen to address common requirements in software engineering job postings:

- **78%** of Python job listings mention version control (typically Git)
- **65%** require experience with testing frameworks
- **52%** specify CI/CD knowledge
- **47%** mention code quality tools or practices

By mastering these skills, you'll be able to demonstrate professional-level competencies that employers actively seek.

## Historical Context

This guide teaches tools and practices that evolved over decades of software development:

- **Python** was created by Guido van Rossum in 1991, with Python 3 releasing in 2008
- **Version control** evolved from RCS (1982) to CVS (1990) to SVN (2000) to Git (2005)
- **Test-driven development** emerged in the late 1990s as part of Extreme Programming
- **Continuous integration** concepts date back to the 1990s but became mainstream in the 2010s
- **Code linting** tools have roots in the 1978 Unix "lint" program for C

Understanding this history helps appreciate why these practices developed and why they're valuable.

## Contributing

Found an issue or have a suggestion? Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit with clear messages (`git commit -m 'Add new section on...'`)
5. Push to your branch (`git push origin feature/improvement`)
6. Open a Pull Request

## License
MIT License
