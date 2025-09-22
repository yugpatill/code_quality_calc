![CI](https://github.com/kaw393939/code_quality_calc/actions/workflows/quality.yml/badge.svg?branch=main)

# 🧮 Professional Python Calculator — Learn Industry-Grade Development

> **Transform a simple calculator into production-ready software** while mastering professional Python development practices used by top tech companies.

This isn't just another coding tutorial. You'll build a **real production system** with the same tools, processes, and quality standards used at companies like Google, Netflix, and Spotify.

## 🎯 What You'll Build

- **High-performance calculator** with comprehensive test coverage (100%)
- **Production-ready CLI** with professional error handling and validation
- **Complete CI/CD pipeline** with automated testing, security scanning, and deployment
- **Professional codebase** that passes enterprise-grade quality checks
- **VS Code workspace** optimized for Python development

## 🚀 Platform Setup — Start Here First!

**All commands in this project use Unix/Linux standards.** Choose your platform:

### 🍎 **macOS Users — You're Ready!**
Your terminal already supports all commands. Proceed to [Quick Start](#quick-start).

### 🪟 **Windows Users — Enable Unix/Linux Environment**

**Option 1: WSL2 Ubuntu (Recommended)**
```powershell
# Run in PowerShell as Administrator
wsl --install -d Ubuntu
# Restart your computer when prompted
# After restart, complete Ubuntu setup with username/password
```

**Option 2: Git Bash**
- Install [Git for Windows](https://git-scm.windows.com/) with Git Bash
- Use Git Bash terminal for all commands

### 🐧 **Linux Users — You're Ready!**
Your terminal already supports all commands. Proceed to [Quick Start](#quick-start).

---

## ⚡ Quick Start (2 minutes)

**Prerequisites**: Python 3.11+ and Git installed

```bash
# 1. Clone and enter the project
git clone <your-repo-url>
cd calc_start_f25

# 2. Set up Python environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows Git Bash: source .venv/Scripts/activate
python -m pip install --upgrade pip

# 3. Install development tools
pip install -r requirements-dev.txt

# 4. Verify everything works
pytest --cov=src --cov-report=term-missing -q
```

**✅ Success!** You should see all tests passing with 100% coverage.

## 🎮 Try It Out

**Basic calculator operations:**
```bash
# Method 1: Direct module execution
python -m src.main add 2 3        # Output: 5.0
python -m src.main multiply 4 5   # Output: 20.0
python -m src.main divide 10 2    # Output: 5.0

# Method 2: Install as CLI tool
pip install -e .
calc add 2 3                      # Output: 5.0
calc subtract 10 3                # Output: 7.0
```

**Run the complete quality suite:**
```bash
# Option 1: Individual commands
pytest --cov=src --cov-report=term-missing -q
flake8 $(git ls-files '*.py' | tr '\n' ' ')
pylint -j 0 $(git ls-files '*.py' | tr '\n' ' ')
mypy src
make security

# Option 2: VS Code task (if using VS Code)
# Command Palette → "Run Task" → "quality: all"

# Option 3: Makefile shortcut
make qa
```

## 🎯 Learning Path

This project includes a **comprehensive learning system** with three tracks:

### 📚 **Detailed Learning Guide**
**Start here:** [`docs/index.md`](docs/index.md) — Complete textbook with 15+ chapters

**Quick navigation:**
- 🚀 [Project Overview](docs/01-overview.md) — Understanding the goals
- ⚙️ [Setup Guide](docs/02-setup.md) — Detailed environment setup
- 🧪 [Testing](docs/05-testing.md) — Achieving 100% test coverage
- 💻 [VS Code Setup](docs/09-vscode.md) — Professional IDE configuration
- 🔄 [CI/CD](docs/08-ci.md) — Automated quality checks

### 🏗️ **Project Structure**
```
calc_start_f25/
├── src/                          # Calculator implementation
│   ├── main.py                   # CLI entry point
│   └── operations/               # Mathematical operations
├── tests/                        # 100% test coverage
├── .vscode/                      # VS Code configuration
├── .github/workflows/            # CI/CD automation
├── docs/                         # Complete learning guide
└── pyproject.toml               # Modern Python packaging
```

### 🛠️ **Professional Tools Integrated**
- **Testing**: pytest with coverage reporting
- **Code Quality**: Black, isort, Flake8, Pylint
- **Type Safety**: mypy static type checking
- **Security**: Bandit, pip-audit, Dependabot
- **CI/CD**: GitHub Actions with automated quality gates
- **IDE**: VS Code with optimized Python development setup

## 🎓 What You'll Learn

### **Foundation Skills**
- ✅ Professional Python project structure (`src/` layout)
- ✅ Virtual environment management and dependency isolation
- ✅ Test-driven development with 100% coverage
- ✅ Code formatting and quality standards (PEP 8)
- ✅ Static type checking for reliability

### **Professional Practices**
- ✅ Continuous Integration and automated testing
- ✅ Security scanning and vulnerability management
- ✅ Professional Git workflows and commit practices
- ✅ Command-line interface design and packaging
- ✅ Performance monitoring and optimization

### **Industry Tools**
- ✅ VS Code configuration for Python development
- ✅ GitHub Actions for CI/CD pipelines
- ✅ Docker containerization (advanced topics)
- ✅ Documentation and project maintenance
- ✅ Collaboration and code review processes

## 🆘 Need Help?

### **Quick Troubleshooting**
```bash
# Common issues and solutions

# Issue: ModuleNotFoundError
# Solution: Activate virtual environment and run from project root
source .venv/bin/activate
cd /path/to/calc_start_f25

# Issue: Import errors in VS Code
# Solution: Select correct Python interpreter
# VS Code → Bottom status bar → Select .venv/bin/python

# Issue: Tests failing
# Solution: Ensure all dependencies installed
pip install -r requirements-dev.txt
pytest --cov=src --cov-report=term-missing
```

### **Comprehensive Support**
- 📖 **Detailed troubleshooting**: [`docs/12-troubleshooting.md`](docs/12-troubleshooting.md)
- 🔧 **Configuration guide**: [`docs/appendix-configs.md`](docs/appendix-configs.md)
- 💼 **Career guidance**: [`docs/careers.md`](docs/careers.md)
- 📝 **Glossary**: [`docs/glossary.md`](docs/glossary.md)

## 🌟 Why This Approach Works

### **Real-World Relevance**
Every tool and practice in this project is used daily by professional Python developers. You're not just learning syntax—you're mastering the **complete professional workflow**.

### **Portfolio Ready**
This project demonstrates professional competency to employers:
- Clean, tested, documented code
- Modern development practices
- CI/CD pipeline experience
- Production-ready software design

### **Foundation for Growth**
The patterns you learn here scale from simple calculators to complex distributed systems. These are the **fundamentals that matter** for any Python career path.

---

## 📈 Next Steps

1. **Start Learning**: Open [`docs/index.md`](docs/index.md) for the complete guide
2. **Try Exercises**: Each chapter includes hands-on activities
3. **Build Your Version**: Fork this repo and customize it
4. **Join the Community**: Share your progress and get help

**Ready to build professional-grade Python software?** [Start your journey here →](docs/index.md)

# Basic Calculator — Professional Python Project Template

This repo is a tiny calculator used to teach professional Python practices: clean structure, tests with coverage, linting/formatting, typing, security checks, CI, and VS Code workflows.

Looking for the full student guide? Read the textbook in [docs](docs/index.md):

- Start here: docs/index.md
- Or jump to: Setup (docs/02-setup.md), Testing (docs/05-testing.md), VS Code (docs/09-vscode.md), CI (docs/08-ci.md)

## Quickstart (macOS + zsh)

```zsh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
```

Run the quality suite:

```zsh
pytest --cov=src --cov-report=term-missing -q
flake8 $(git ls-files '*.py' | tr '\n' ' ')
pylint -j 0 $(git ls-files '*.py' | tr '\n' ' ')
mypy src
make security
```

## CLI usage

Install in editable mode to use the `calc` command:

```zsh
. .venv/bin/activate
pip install -e .
calc add 2 3
```

Or run without installing:

```zsh
python -m src.main add 2 3
```

## What’s inside

- `src/` — calculator code and CLI
- `tests/` — pytest suite with 100% coverage on `src/`
- `pyproject.toml` — tool configs (Black, isort, Flake8, Pylint, mypy) and console script
- `.vscode/` — tasks, settings, and debug configs
- `.github/workflows/quality.yml` — CI for format/lint/typecheck/security
- `docs/` — the full student textbook for this project

For details, see the textbook: `docs/index.md`.
