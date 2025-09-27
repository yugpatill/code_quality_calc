# Assignment 4: Professional Git Workflows

## Learning Objectives
- Understand the purpose and importance of version control
- Create atomic commits with meaningful messages
- Implement feature branching workflows
- Resolve merge conflicts
- Use Git effectively in a team environment
- Apply Git best practices to a Python project

## Background

Git, created by Linus Torvalds in 2005 for Linux kernel development, has become the industry standard for version control. This assignment will teach you professional Git workflows using our calculator project as an example.

### Historical Context

Version control systems have evolved significantly over time:
- **1972**: Source Code Control System (SCCS) - First version control system
- **1982**: Revision Control System (RCS) - Improved file-level versioning
- **1990**: Concurrent Versions System (CVS) - Added multi-file commits
- **2000**: Apache Subversion (SVN) - Improved CVS with atomic commits
- **2005**: Git - Created by Linus Torvalds after a dispute with the proprietary BitKeeper VCS
- **2008**: GitHub launched, making Git more accessible and adding social coding features

Git revolutionized version control with its distributed nature, allowing every developer to have a full copy of the repository history.

## Prerequisites
- Git installed on your system
- Python >= 3.10 installed
- Virtual environment setup (from Assignment 1)
- Calculator project from previous assignments
- Basic Git knowledge (init, add, commit, push)

## Time to Complete
Expect to spend approximately 3-4 hours on this assignment.

## Part 1: Setting Up the Repository

### Task 1.1: Initializing a Git Repository

If you haven't already, initialize a Git repository for your calculator project:

```bash
cd python_calculator
git init
```

### Task 1.2: Creating a .gitignore File

1. Create a `.gitignore` file:
   ```bash
   touch .gitignore
   ```

2. Add standard Python ignores:
   ```
   # Virtual Environment
   venv/
   new_venv/
   
   # Python
   __pycache__/
   *.py[cod]
   *$py.class
   .pytest_cache/
   .coverage
   htmlcov/
   
   # IDE
   .vscode/
   .idea/
   
   # OS specific
   .DS_Store
   Thumbs.db
   ```

3. Make your first commit:
   ```bash
   git add .gitignore
   git commit -m "Initial commit: Add .gitignore file"
   ```

### Task 1.3: Adding Your Calculator Project

1. Add your existing calculator files:
   ```bash
   git add .
   git status  # Review what will be committed
   ```

2. Make an atomic commit:
   ```bash
   git commit -m "Add calculator project with basic operations"
   ```

## Part 2: Implementing Atomic Commits

### Task 2.1: Understanding Atomic Commits

An atomic commit represents a single logical change to your codebase. Benefits include:
- Easier to understand what each commit does
- Simpler to review code changes
- Ability to revert specific changes without affecting others
- Better debugging through history

### Task 2.2: Adding Trigonometric Functions with Atomic Commits

1. Create a feature branch:
   ```bash
   git checkout -b feature/trigonometry
   ```

2. Create a new file `src/calculator/trigonometry.py`:
   ```python
   """Trigonometric functions for the calculator."""
   import math
   
   def sin(x):
       """
       Calculate the sine of x (in radians).
       
       Args:
           x: Angle in radians
           
       Returns:
           The sine of x
       """
       return math.sin(x)
   ```

3. Make an atomic commit for this function:
   ```bash
   git add src/calculator/trigonometry.py
   git commit -m "feat: implement sine function for calculator"
   ```

4. Add the cosine function:
   ```python
   def cos(x):
       """
       Calculate the cosine of x (in radians).
       
       Args:
           x: Angle in radians
           
       Returns:
           The cosine of x
       """
       return math.cos(x)
   ```

5. Make another atomic commit:
   ```bash
   git add src/calculator/trigonometry.py
   git commit -m "feat: add cosine function to trigonometry module"
   ```

6. Add the tangent function:
   ```python
   def tan(x):
       """
       Calculate the tangent of x (in radians).
       
       Args:
           x: Angle in radians
           
       Returns:
           The tangent of x
           
       Raises:
           ValueError: If x is a multiple of π/2 (undefined)
       """
       # Check for undefined values
       if abs(math.cos(x)) < 1e-10:
           raise ValueError("Tangent is undefined at this value")
       return math.tan(x)
   ```

7. Make another atomic commit:
   ```bash
   git add src/calculator/trigonometry.py
   git commit -m "feat: add tangent function with domain validation"
   ```

### Task 2.3: Writing Good Commit Messages

Follow the Conventional Commits format:
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types include:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `test`: Adding or correcting tests

Example of a complete commit message:
```
feat(trigonometry): add inverse trigonometric functions

Implement asin, acos, and atan functions to complement existing
trigonometric functions. These provide the ability to calculate
angles from ratio values.

Closes #42
```

## Part 3: Branching Strategies

### Task 3.1: Understanding Branching Strategies

Common branching strategies include:
- **GitFlow**: Complex but comprehensive, with develop/feature/release/hotfix branches
- **GitHub Flow**: Simpler workflow with feature branches and PRs
- **Trunk-Based Development**: Most work on main, with short-lived feature branches

For this assignment, you'll implement GitHub Flow:
1. Create feature branches from main
2. Commit changes to feature branches
3. Open pull requests
4. Discuss and review code
5. Merge to main

### Task 3.2: Creating a Feature Branch for Calculator Memory

1. Switch back to the main branch:
   ```bash
   git checkout main
   ```

2. Create a new feature branch:
   ```bash
   git checkout -b feature/memory-functions
   ```

3. Update your Calculator class in `src/calculator/calculator.py` to add memory functionality:
   ```python
   def memory_add(self, value):
       """
       Add a value to the memory.
       
       Args:
           value: Value to add to memory
       """
       self.memory += value
   
   def memory_subtract(self, value):
       """
       Subtract a value from the memory.
       
       Args:
           value: Value to subtract from memory
       """
       self.memory -= value
   ```

4. Make an atomic commit:
   ```bash
   git add src/calculator/calculator.py
   git commit -m "feat: add memory_add and memory_subtract functions"
   ```

5. Add tests for the new functionality in `tests/test_calculator.py`.

6. Make another atomic commit:
   ```bash
   git add tests/test_calculator.py
   git commit -m "test: add tests for memory_add and memory_subtract functions"
   ```

## Part 4: Handling Merge Conflicts

### Task 4.1: Creating a Conflict

1. Switch back to the main branch:
   ```bash
   git checkout main
   ```

2. Create another feature branch:
   ```bash
   git checkout -b feature/display
   ```

3. Modify the Calculator class to add a display property:
   ```python
   class Calculator:
       """Calculator class to perform arithmetic operations."""
       
       def __init__(self):
           """Initialize calculator with memory set to 0 and empty display."""
           self.memory = 0
           self.display = "0"
       
       # Add this method
       def update_display(self, value):
           """Update the calculator display."""
           self.display = str(value)
   ```

4. Commit this change:
   ```bash
   git add src/calculator/calculator.py
   git commit -m "feat: add display functionality to calculator"
   ```

### Task 4.2: Resolving the Conflict

1. Try to merge the memory feature branch:
   ```bash
   git checkout main
   git merge feature/memory-functions
   ```

2. Merge the display feature branch (this will create a conflict):
   ```bash
   git merge feature/display
   ```

3. Resolve the conflict in `src/calculator/calculator.py` by editing the file to include both changes:
   ```python
   class Calculator:
       """Calculator class to perform arithmetic operations."""
       
       def __init__(self):
           """Initialize calculator with memory set to 0 and empty display."""
           self.memory = 0
           self.display = "0"
       
       # ... other methods ...
       
       def memory_add(self, value):
           """Add a value to the memory."""
           self.memory += value
       
       def memory_subtract(self, value):
           """Subtract a value from the memory."""
           self.memory -= value
       
       def update_display(self, value):
           """Update the calculator display."""
           self.display = str(value)
   ```

4. Mark the conflict as resolved:
   ```bash
   git add src/calculator/calculator.py
   ```

5. Complete the merge:
   ```bash
   git commit -m "merge: combine memory and display features"
   ```

## Part 5: Remote Repositories and Collaboration

### Task 5.1: Setting Up a Remote Repository

1. Create a new repository on GitHub (or another Git hosting service)

2. Add the remote to your local repository:
   ```bash
   git remote add origin https://github.com/yourusername/python_calculator.git
   ```

3. Push your main branch:
   ```bash
   git push -u origin main
   ```

4. Push your feature branches:
   ```bash
   git push origin feature/trigonometry
   git push origin feature/memory-functions
   git push origin feature/display
   ```

### Task 5.2: Creating a Pull Request

1. Go to your repository on GitHub
2. Select one of your feature branches
3. Click "Compare & pull request"
4. Write a clear title and description for your PR
5. Submit the pull request

### Task 5.3: Code Review Process

1. Review your own PR, looking for:
   - Code style and quality
   - Potential bugs
   - Test coverage
   - Documentation

2. Add comments to your PR with improvements you would make

3. Merge the PR once you're satisfied with the quality

## Part 6: Advanced Git Techniques

### Task 6.1: Using git log to Understand History

1. View the commit history with a better format:
   ```bash
   git log --oneline --graph --all
   ```

2. View changes in a specific commit:
   ```bash
   git show <commit-id>
   ```

### Task 6.2: Using Tags for Releases

1. Create a tag for your first release:
   ```bash
   git tag -a v0.1.0 -m "First release of Calculator with basic and scientific operations"
   ```

2. Push the tag to GitHub:
   ```bash
   git push origin v0.1.0
   ```

## Common Pitfalls

- **Forgetting to create a branch**: Always work in a feature branch, not directly in main
- **Large, non-atomic commits**: Keep commits small and focused on a single change
- **Poor commit messages**: Use the conventional commits format for clarity
- **Merging without testing**: Always test after resolving merge conflicts
- **Forgetting to push**: Remember to push your branches to share your work
- **Committing sensitive information**: Be careful not to commit API keys, passwords, etc.

## Troubleshooting

### Issue: "Failed to push some refs"

**Solution:**
- Pull the latest changes first:
  ```bash
  git pull origin main
  ```
- Then try pushing again

### Issue: Accidentally committed to the wrong branch

**Solution:**
- Use git stash to save your changes:
  ```bash
  git stash
  git checkout correct-branch
  git stash pop
  ```

### Issue: Need to undo a commit

**Solution:**
- For the most recent commit:
  ```bash
  git reset --soft HEAD~1
  ```
- This keeps your changes but undoes the commit

## What Success Looks Like

By the end of this assignment, you should have:
- A Git repository with a clean, logical commit history
- Multiple feature branches demonstrating proper branching strategy
- Experience resolving merge conflicts
- A remote repository on GitHub with at least one PR
- A tagged release of your calculator application

## Self-Assessment Questions

1. What are the benefits of atomic commits?
2. How does branching help in collaborative development?
3. What branching strategy would you recommend for a small team? For a large team?
4. What should you do when you encounter a merge conflict?
5. How does Git's distributed nature differ from centralized version control systems?
6. Why is it important to write good commit messages?

## Submission Requirements

Submit the following:

1. The URL to your GitHub repository
2. Screenshots of:
   - Your commit history (git log)
   - A resolved merge conflict
   - Your pull request on GitHub

3. A reflection document (300-500 words) addressing:
   - How atomic commits improved your development process
   - What challenges you faced with merge conflicts and how you resolved them
   - How you would adapt these Git workflows for team projects
   - How Git supports or enhances software quality

## Additional Resources

- [Pro Git Book](https://git-scm.com/book/en/v2) - Comprehensive Git guide
- [Conventional Commits](https://www.conventionalcommits.org/) - Specification for commit messages
- [GitHub Flow](https://guides.github.com/introduction/flow/) - Simple workflow using GitHub
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) - Quick reference
- [Learn Git Branching](https://learngitbranching.js.org/) - Interactive Git visualization tool
