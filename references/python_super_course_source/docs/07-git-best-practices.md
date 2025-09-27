# Git Best Practices

This guide covers professional Git workflows and best practices for software development.

## The History of Git

Git was created by Linus Torvalds in 2005 for managing Linux kernel development. After a dispute with the proprietary version control system BitKeeper, Torvalds needed a distributed version control system that was:

- Fast
- Distributed (no central server required)
- Capable of efficiently handling large projects like Linux

Git was designed to be significantly different from CVS and SVN (centralized version control systems), with an emphasis on:
- Distributed workflows
- Data integrity
- Non-linear development (branching)
- Speed

## Key Git Concepts

### Distributed Version Control

Unlike centralized systems (SVN, CVS), with Git:
- Every developer has a full copy of the repository
- You can commit changes locally without network access
- Multiple remote repositories can exist simultaneously

### Git Data Model

Git stores data as:
- **Commits**: Snapshots of your project at a point in time
- **Trees**: Directories in your project
- **Blobs**: File contents
- **References**: Pointers to commits (branches, tags)

## Atomic Commits

An atomic commit is a commit that represents a single logical change to your codebase.

### Why Atomic Commits Matter

1. **Easier to understand**: Each commit does one thing and does it well
2. **Easier to review**: Reviewers can focus on one logical change
3. **Easier to revert**: If a change needs to be undone, it's isolated
4. **Better history**: The project history tells a clear story

### Non-Atomic vs. Atomic Commits

❌ **Non-Atomic Commit**:
```
"Fixed login bug, updated header styles, and added new user profile page"
```

✅ **Atomic Commits**:
```
"Fix authentication bug in login form"
"Update header styles for better mobile display"
"Add user profile page"
```

### Creating Atomic Commits

1. Make frequent, small commits
2. Use `git add -p` to stage specific parts of files:
   ```bash
   git add -p
   ```
3. Create multiple commits from your changes:
   ```bash
   # Stage specific files or changes
   git add src/login.js
   git commit -m "Fix authentication bug in login form"
   
   git add src/styles/header.css
   git commit -m "Update header styles for better mobile display"
   ```

## Writing Effective Commit Messages

Good commit messages are crucial for maintaining a useful project history.

### Conventional Commits Format

Follow the conventional commits format:
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types include:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, missing semicolons, etc.
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `test`: Adding or correcting tests
- `chore`: Changes to the build process, tools, etc.

### Examples:

```
feat(auth): add Google OAuth login option

Implements Google OAuth strategy with Passport.js.
Includes token validation and user profile fetching.

Closes #123
```

```
fix: prevent race condition in data processing

The data processor was not waiting for file operations
to complete before moving to the next step.

Fixes #456
```

## Branching Strategies

Different teams use different branching strategies based on their needs.

### 1. GitFlow

A complex but comprehensive branching model with dedicated branches:

- `main` or `master`: Production code
- `develop`: Integration branch for development
- `feature/*`: New features
- `release/*`: Preparing for a release
- `hotfix/*`: Emergency fixes for production

Ideal for teams with scheduled releases and multiple versions.

### 2. GitHub Flow

A simpler workflow:

- `main` or `master`: Always deployable
- Feature branches: Created for each change
- Pull requests: Used to merge changes after review

Ideal for continuous delivery and smaller teams.

### 3. Trunk-Based Development

An even simpler approach:

- Most work happens on `main` or `trunk`
- Short-lived feature branches when necessary
- Emphasis on small, frequent commits

Ideal for CI/CD environments and experienced teams.

## The Pull Request Workflow

Pull requests (PRs) facilitate code review and collaboration.

### Creating an Effective PR

1. **Keep it focused**: One logical change per PR
2. **Write a clear description**:
   - What changes were made
   - Why they were necessary
   - How to test the changes
3. **Include relevant information**:
   - Screenshots (for UI changes)
   - Links to related issues
   - Performance considerations

### Reviewing PRs

When reviewing others' code:

1. **Be respectful and constructive**
2. **Focus on the code, not the person**
3. **Ask questions rather than making demands**
4. **Provide specific, actionable feedback**
5. **Approve when requirements are met**

### Responding to Reviews

When your code is being reviewed:

1. **Be open to feedback**
2. **Respond to all comments**
3. **Explain your decisions when necessary**
4. **Make requested changes promptly**

## Advanced Git Techniques

### Interactive Rebase

Interactive rebase allows you to modify commits before pushing:

```bash
# Rebase the last 3 commits
git rebase -i HEAD~3
```

This opens an editor where you can:
- Reorder commits
- Edit commit messages
- Combine (squash) commits
- Split commits

### Cherry-Picking

Apply specific commits from one branch to another:

```bash
# Find the commit hash
git log

# Apply that commit to your current branch
git cherry-pick abc123
```

Useful for applying specific fixes across branches.

### Stashing

Save changes temporarily without committing:

```bash
# Stash current changes
git stash

# Do other work...

# Retrieve stashed changes
git stash pop
```

### Bisect

Find which commit introduced a bug:

```bash
# Start bisect
git bisect start

# Mark current state as bad
git bisect bad

# Mark a known good commit
git bisect good abc123

# Git will checkout commits for you to test
# After testing, mark as good or bad
git bisect good  # or git bisect bad

# When found, end the bisect
git bisect reset
```

## Git Hooks and Automation

Git hooks are scripts that run automatically at certain points in Git's execution.

### Common Hook Use Cases

1. **pre-commit**: Run linters and tests before allowing a commit
2. **prepare-commit-msg**: Auto-format commit messages
3. **post-merge**: Update dependencies after pulling changes

### Setting Up Hooks

Hooks are stored in `.git/hooks/`, but for team sharing, tools like Husky can help:

```bash
# Install Husky
npm install husky --save-dev

# Configure in package.json
"husky": {
  "hooks": {
    "pre-commit": "npm run lint && npm test",
    "prepare-commit-msg": "node scripts/prepare-commit-msg.js"
  }
}
```

## Integrating with CI/CD

Git workflows integrate seamlessly with CI/CD pipelines:

1. Push to a feature branch triggers CI tests
2. PR creation runs additional validation
3. Merging to main triggers deployment

### GitHub Actions Example

```yaml
name: CI

on:
  push:
    branches: [ feature/* ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.10'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
    - name: Lint
      run: pylint src tests
    - name: Test
      run: pytest
```

## Real-World Git Scenarios

### Scenario 1: Resolving Merge Conflicts

```bash
# Pull latest changes
git pull origin main

# If conflicts occur, check status
git status

# Open conflicted files, look for <<<<<<, =======, >>>>>>>
# Edit files to resolve conflicts

# Add resolved files
git add resolved-file.py

# Complete the merge
git commit
```

### Scenario 2: Recovering Lost Work

```bash
# See reflog to find lost commits
git reflog

# Recover a specific commit
git checkout -b recovery-branch abc123

# Or recover uncommitted changes
git fsck --lost-found
```

### Scenario 3: Cleaning Up Before PR

```bash
# Squash multiple commits
git rebase -i HEAD~5

# Fix up any issues
git commit --amend

# Force push to your feature branch (never force push to shared branches)
git push --force-with-lease origin feature/my-feature
```

## Best Practices Summary

1. **Make atomic commits** with clear messages
2. **Branch strategically** based on your team's needs
3. **Pull regularly** to stay in sync with the team
4. **Review code carefully** before merging
5. **Never force push** to shared branches
6. **Automate testing** with hooks and CI
7. **Document your workflow** for new team members

## Additional Resources

- [Pro Git Book](https://git-scm.com/book/en/v2) - Free comprehensive guide
- [Conventional Commits](https://www.conventionalcommits.org/) - Specification for commit messages
- [GitHub Flow](https://guides.github.com/introduction/flow/) - Simple, effective workflow
- [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/) - Detailed branching strategy
- [Git Hooks Documentation](https://git-scm.com/docs/githooks) - Official documentation
