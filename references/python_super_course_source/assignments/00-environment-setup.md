# Assignment 00: Professional Development Environment Setup and Mindset

## Learning Objectives
- Set up a complete professional Python development environment
- Configure essential development tools (VS Code, terminal, Git)
- Establish professional documentation and communication practices
- Apply scientific problem-solving methodology to debugging
- Practice effective help-seeking and research skills
- Create your first professional project repository
- Develop a growth mindset for continuous learning

## Background

Before diving into Python programming, professional developers invest time in setting up their development environment properly. This isn't just about installing software—it's about creating a workflow that supports productivity, collaboration, and continuous learning.

Think of this like a master carpenter organizing their workshop. They don't just throw tools in a box; they carefully arrange everything for efficiency, safety, and precision. Your development environment is your digital workshop.

## Prerequisites
- A computer running Windows, macOS, or Linux
- Administrative access to install software
- Internet connection for downloads and research
- No prior programming experience required
- Enthusiasm for learning professional practices

## Time to Complete
Expect to spend approximately 3-4 hours on this assignment, spread across multiple sessions.

---

## Part 1: Development Tool Installation and Configuration

### Task 1.1: Install and Configure Python

#### For macOS Users:
1. **Check if Python is already installed:**
   ```bash
   python3 --version
   ```
   
2. **If Python >= 3.10 is not installed, install using Homebrew:**
   ```bash
   # Install Homebrew if you don't have it
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install Python
   brew install python
   ```

#### For Windows Users:
1. **Download Python (>= 3.10) from the official website:**
   - Go to https://python.org/downloads/
   - Download Python 3.10 or later
   - **IMPORTANT**: Check "Add Python to PATH" during installation

2. **Verify installation in PowerShell:**
   ```powershell
   python --version
   pip --version
   ```

#### For Linux Users:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv

# CentOS/RHEL/Fedora
sudo dnf install python3 python3-pip
```

#### Verification Task:
Create a file called `python_check.py` with this content:
```python
import sys
import platform

print(f"Python version: {sys.version}")
print(f"Platform: {platform.system()} {platform.release()}")
print(f"Python executable: {sys.executable}")
print("✅ Python is working correctly!")
```

Run it with: `python3 python_check.py` (or `python python_check.py` on Windows)

### Task 1.2: Install and Configure VS Code

1. **Download and install VS Code:**
   - Visit https://code.visualstudio.com/
   - Download for your operating system
   - Follow the installation instructions

2. **Install essential extensions:**
   Open VS Code and install these extensions (Ctrl/Cmd + Shift + X):
   - **Python** (by Microsoft) - Python language support
   - **Pylance** (by Microsoft) - Advanced Python language features
   - **GitLens** (by GitKraken) - Enhanced Git capabilities
   - **Auto Rename Tag** (by Jun Han) - HTML/XML tag management
   - **Bracket Pair Colorizer 2** (by CoenraadS) - Visual bracket matching
   - **Material Icon Theme** (by Philipp Kief) - Better file icons

3. **Configure VS Code settings:**
   Open Settings (Ctrl/Cmd + ,) and configure:
   - Font size: 14-16 (adjust for comfort)
   - Auto Save: afterDelay
   - Format On Save: enabled
   - Word Wrap: on

### Task 1.3: Configure Your Terminal

#### For macOS/Linux Users:
1. **Customize your shell prompt** (optional but recommended):
   Add to your `~/.zshrc` or `~/.bashrc`:
   ```bash
   # Add some color and useful info to your prompt
   export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "
   ```

2. **Install useful command-line tools:**
   ```bash
   # macOS with Homebrew
   brew install tree git wget curl
   
   # Linux
   sudo apt install tree git wget curl  # Ubuntu/Debian
   sudo dnf install tree git wget curl  # CentOS/RHEL/Fedora
   ```

#### For Windows Users:
1. **Set up Windows Subsystem for Linux (WSL2)** - Recommended:
   ```powershell
   # Run as Administrator
   wsl --install
   ```
   After restart, set up Ubuntu from Microsoft Store.

2. **Alternative: Use PowerShell with useful modules:**
   ```powershell
   # Install PowerShell modules
   Install-Module -Name PSReadLine -Force
   Install-Module -Name posh-git -Force
   ```

### Task 1.4: Install and Configure Git

1. **Install Git:**
   ```bash
   # macOS (if not already installed)
   brew install git
   
   # Windows (download from git-scm.com or use package manager)
   winget install Git.Git
   
   # Linux
   sudo apt install git  # Ubuntu/Debian
   sudo dnf install git  # CentOS/RHEL/Fedora
   ```

2. **Configure Git with your identity:**
   ```bash
   git config --global user.name "Your Full Name"
   git config --global user.email "your.email@example.com"
   git config --global init.defaultBranch main
   git config --global core.editor "code --wait"
   ```

3. **Set up SSH keys for GitHub** (we'll use this later):
   ```bash
   # Generate SSH key
   ssh-keygen -t ed25519 -C "your.email@example.com"
   
   # Start SSH agent and add key
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   
   # Copy public key to clipboard
   # macOS:
   pbcopy < ~/.ssh/id_ed25519.pub
   
   # Linux:
   cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard
   
   # Windows (in Git Bash):
   clip < ~/.ssh/id_ed25519.pub
   ```

---

## Part 2: Professional Documentation and Communication

### Task 2.1: Create Your First Professional README

1. **Create a project directory:**
   ```bash
   mkdir learning-portfolio
   cd learning-portfolio
   ```

2. **Initialize Git repository:**
   ```bash
   git init
   ```

3. **Create a professional README.md file:**
   
   Open VS Code in this directory: `code .`
   
   Create `README.md` with this template (customize with your information):

```markdown
# My Professional Development Learning Portfolio

## About Me

**Name:** [Your Name]  
**Program:** [Your Degree/Program]  
**Expected Graduation:** [Date]  
**GitHub:** [Your GitHub username when you create it]

## Professional Development Goals

I am learning professional software development practices to prepare for a career in [your field of interest]. This portfolio documents my journey from basic programming concepts to industry-standard development practices.

### Current Learning Focus
- Professional Python development workflows
- Test-driven development and quality assurance
- Version control and collaboration practices
- Continuous integration and deployment
- Industry-standard tooling and methodologies

## Skills Development Tracker

### Environment Setup ✅
- [x] Python development environment configured
- [x] VS Code with professional extensions
- [x] Git configuration and SSH keys
- [x] Terminal customization and tools

### Foundation Skills (In Progress)
- [ ] Virtual environments and package management
- [ ] Code quality tools and linting
- [ ] Testing with pytest
- [ ] Git workflows and collaboration

### Professional Practices (Planned)
- [ ] Continuous integration with GitHub Actions
- [ ] Configuration management and secrets
- [ ] Package distribution and publishing
- [ ] Production deployment strategies

## Projects

### Calculator Project
**Status:** Planning  
**Description:** A professional-grade calculator application built using test-driven development, proper documentation, and industry-standard practices.

**Learning Objectives:**
- Apply virtual environment management
- Implement comprehensive testing strategy
- Use professional Git workflows
- Integrate continuous integration
- Practice code quality standards

## Reflection and Learning Notes

### Week 1: Environment Setup
**Date:** [Today's date]

**What I learned:**
- Setting up a professional development environment requires more than just installing software
- The importance of standardized tooling for collaboration
- How proper configuration saves time and prevents issues later

**Challenges faced:**
- [Document any issues you encountered and how you solved them]

**Resources that helped:**
- [List helpful documentation, tutorials, or people who assisted]

**Next steps:**
- Begin working with virtual environments
- Start the calculator project foundation

---

*This portfolio is part of my professional development coursework and demonstrates my commitment to learning industry-standard practices.*
```

4. **Commit your first professional documentation:**
   ```bash
   git add README.md
   git commit -m "docs: add initial professional portfolio README

   - Establish professional documentation standards
   - Document learning objectives and progress tracking
   - Create foundation for ongoing portfolio development"
   ```

### Task 2.2: Practice Effective Help-Seeking

1. **Research Exercise:**
   Research ONE of these topics and write a brief summary (2-3 paragraphs):
   - What is test-driven development and why do professionals use it?
   - How do virtual environments prevent "dependency hell" in Python?
   - What are the benefits of using version control for solo projects?
   - Why do companies use continuous integration?

2. **Create a well-formed technical question:**
   Write a sample Stack Overflow or forum question about a Python concept you're curious about. Use this structure:
   - **Clear, specific title**
   - **Context and background**
   - **What you've tried**
   - **Specific question**
   - **Expected vs actual behavior**
   - **Minimal reproducible example** (if applicable)

3. **Document your research:**
   Add a section to your README called "Research and Learning" and include your summary and sample question.

---

## Part 3: Scientific Problem-Solving and Debugging

### Task 3.1: Debug a Broken Script

Here's a Python script with several issues. Your job is to apply systematic debugging methodology:

Create `debugging_exercise.py`:

```python
import math

def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        print("Error: Radius cannot be negative")
        return
    
    area = math.pi * radius ** 2
    return area

def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    if length <= 0 or width <= 0:
        print("Error: Length and width must be positive")
        return
    
    area = length * width
    return area

def main():
    print("Area Calculator")
    print("===============")
    
    # Circle calculation
    radius = input("Enter circle radius: ")
    circle_area = calculate_circle_area(radius)
    print(f"Circle area: {circle_area}")
    
    # Rectangle calculation
    length = input("Enter rectangle length: ")
    width = input("Enter rectangle width: ")
    rectangle_area = calculate_rectangle_area(length, width)
    print(f"Rectangle area: {rectangle_area}")

if __name__ == "__main__":
    main()
```

**Debugging Process:**

1. **Run the script and observe behavior:**
   ```bash
   python3 debugging_exercise.py
   ```

2. **Apply systematic debugging:**
   - **Reproduce:** Can you consistently reproduce any issues?
   - **Gather information:** What error messages or unexpected behavior do you see?
   - **Form hypothesis:** What do you think is causing the issue?
   - **Test:** Make minimal changes to test your hypothesis
   - **Verify:** Confirm your fix works for various inputs

3. **Document your debugging process:**
   Create `debugging_log.md` and document:
   - Issues found
   - Your hypothesis for each issue
   - How you tested your hypothesis
   - The final solution
   - What you learned from the process

### Task 3.2: Create a Fixed Version

Create `calculator_fixed.py` with your corrected version. Consider:
- Data type handling
- Input validation
- Error handling
- Code organization
- User experience

---

## Part 4: Professional Workflow and Reflection

### Task 4.1: Create a Development Workflow

1. **Document your workflow:**
   Add a section to your README called "My Development Workflow" that describes your process for:
   - Starting a new coding session
   - Saving and backing up work
   - Testing changes
   - Documenting problems and solutions

2. **Practice your workflow:**
   Make a small improvement to your calculator script and practice your documented workflow.

### Task 4.2: Weekly Reflection Journal

Create `reflection_journal.md` and write your first entry:

```markdown
# Professional Development Reflection Journal

## Week 1: Foundation Setup and Mindset

**Date:** [Today's date]

### What I Accomplished
- [List specific tasks completed]

### Key Insights
- [What surprised you or challenged your assumptions?]

### Challenges and How I Overcame Them
- [Specific problems and your solutions]

### Skills Demonstrated
- [What professional skills did you practice?]

### Questions for Further Research
- [What do you want to learn more about?]

### Preparation for Next Steps
- [How do you feel prepared for the next assignment?]

### Professional Growth
- [How do these skills connect to your career goals?]
```

---

## Part 5: Environment Verification and Submission

### Task 5.1: Comprehensive Environment Test

Create `environment_test.py`:

```python
#!/usr/bin/env python3
"""
Professional Development Environment Verification
Tests that all required tools and configurations are working properly.
"""

import sys
import subprocess
import platform
from pathlib import Path

def test_python_installation():
    """Verify Python installation and version."""
    print("🐍 Testing Python Installation...")
    version = sys.version_info
    print(f"   Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("   ✅ Python version is suitable for professional development")
        return True
    else:
        print("   ❌ Python version should be 3.8 or higher")
        return False

def test_pip_installation():
    """Verify pip is available."""
    print("\n📦 Testing pip Installation...")
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"   ✅ pip is working: {result.stdout.strip()}")
            return True
        else:
            print("   ❌ pip is not working properly")
            return False
    except Exception as e:
        print(f"   ❌ Error testing pip: {e}")
        return False

def test_git_installation():
    """Verify Git installation and configuration."""
    print("\n🔀 Testing Git Installation...")
    try:
        # Test Git is installed
        result = subprocess.run(["git", "--version"], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print("   ❌ Git is not installed or not in PATH")
            return False
        
        print(f"   ✅ Git is installed: {result.stdout.strip()}")
        
        # Test Git configuration
        name_result = subprocess.run(["git", "config", "user.name"], 
                                   capture_output=True, text=True)
        email_result = subprocess.run(["git", "config", "user.email"], 
                                    capture_output=True, text=True)
        
        if name_result.returncode == 0 and email_result.returncode == 0:
            print(f"   ✅ Git user: {name_result.stdout.strip()}")
            print(f"   ✅ Git email: {email_result.stdout.strip()}")
            return True
        else:
            print("   ❌ Git user name and email not configured")
            return False
            
    except Exception as e:
        print(f"   ❌ Error testing Git: {e}")
        return False

def test_project_structure():
    """Verify project structure and files."""
    print("\n📁 Testing Project Structure...")
    
    required_files = [
        "README.md",
        "debugging_exercise.py",
        "calculator_fixed.py",
        "debugging_log.md",
        "reflection_journal.md"
    ]
    
    all_present = True
    for file in required_files:
        if Path(file).exists():
            print(f"   ✅ {file} exists")
        else:
            print(f"   ❌ {file} is missing")
            all_present = False
    
    return all_present

def main():
    """Run all environment tests."""
    print("🔧 Professional Development Environment Verification")
    print("=" * 55)
    
    tests = [
        test_python_installation,
        test_pip_installation,
        test_git_installation,
        test_project_structure
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 55)
    print("📋 SUMMARY")
    
    if all(results):
        print("🎉 Congratulations! Your development environment is properly configured.")
        print("🚀 You're ready to begin professional Python development!")
    else:
        print("⚠️  Some issues need to be resolved before proceeding.")
        print("📚 Review the failed tests and seek help if needed.")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
```

Run the verification: `python3 environment_test.py`

### Task 5.2: Final Git Workflow

1. **Add all your work to Git:**
   ```bash
   git add .
   git status  # Review what you're about to commit
   ```

2. **Create a comprehensive commit:**
   ```bash
   git commit -m "feat: complete professional development environment setup

   - Configure Python, VS Code, Git, and terminal
   - Create professional documentation standards
   - Practice systematic debugging methodology  
   - Establish reflection and learning practices
   - Verify environment with comprehensive testing

   This foundation enables professional development workflows
   and establishes habits for continuous learning and growth."
   ```

3. **View your commit history:**
   ```bash
   git log --oneline
   ```

---

## Reflection Questions

Before submitting, reflect on these questions in your reflection journal:

1. **Professional Mindset:** How has your understanding of "professional development" changed from when you started?

2. **Tool Appreciation:** Which tool or configuration do you think will have the biggest impact on your productivity? Why?

3. **Problem-Solving:** Describe how the systematic debugging approach differs from how you might have approached problems before.

4. **Future Applications:** How do you see these setup practices applying to other projects or coursework?

5. **Growth Mindset:** What aspects of professional development are you most excited to learn about next?

## Submission Requirements

Your submission should include:

1. **All project files** in your `learning-portfolio` directory
2. **Completed README.md** with your professional portfolio
3. **Fixed calculator script** with proper error handling
4. **Debugging log** documenting your systematic approach
5. **Reflection journal** with thoughtful first entry
6. **Successful environment test** results
7. **Clean Git history** with meaningful commit messages

## Assessment Criteria

Your work will be evaluated on:

- **Completeness:** All tasks completed thoroughly
- **Documentation Quality:** Clear, professional writing and formatting
- **Problem-Solving Approach:** Evidence of systematic, scientific methodology
- **Professional Practices:** Proper Git usage, file organization, and workflows
- **Reflection Depth:** Thoughtful analysis of learning and growth
- **Environment Configuration:** Properly working development setup

## What's Next?

With your professional development environment established, you're ready to begin Assignment 1: Virtual Environments and Package Management. You'll build upon this foundation to create isolated project environments and manage dependencies professionally.

The habits and mindset you've developed in this assignment will serve you throughout your career in software development. Professional developers invest in their tools and workflows because it multiplies their effectiveness over time.

Welcome to the professional development journey! 🚀