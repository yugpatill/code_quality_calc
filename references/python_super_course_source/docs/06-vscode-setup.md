# VS Code Integration Guide

This guide explains how to set up Visual Studio Code (VS Code) for Python development across Windows (including WSL2), macOS, and Linux.

## Installing VS Code

1. Download VS Code from the [official website](https://code.visualstudio.com/)
2. Follow the installation instructions for your platform

### For WSL2 Users
If you're using WSL2 on Windows, you have two options:

1. **Remote WSL Development** (Recommended):
   - Install VS Code on Windows
   - Install the "Remote - WSL" extension
   - Open your WSL terminal and type `code .` to launch VS Code connected to WSL

2. **Native WSL Installation**:
   - Install VS Code directly in WSL (more advanced)
   - Follow the [official guide](https://code.visualstudio.com/docs/remote/wsl)

## Essential Extensions

Install these extensions for Python development:

1. **Python** (Microsoft) - Core Python support
   - Intellisense, linting, debugging, code navigation, etc.

2. **Pylance** - Fast, feature-rich language support
   - Type checking, import organization, etc.

3. **Python Test Explorer** - Visual testing interface

4. **Python Indent** - Correct Python indentation

5. **GitLens** - Enhanced Git capabilities

6. **Jupyter** - For notebook support

## Installing Extensions

1. Click the Extensions icon in the Activity Bar
2. Search for each extension
3. Click Install

For WSL2 users, install extensions in your WSL window to ensure they're available in your Linux environment.

## Setting Up Python in VS Code

### Selecting a Python Interpreter

1. Open a Python file
2. Click on the Python version in the bottom status bar (or press `Ctrl+Shift+P`)
3. Select "Python: Select Interpreter"
4. Choose your virtual environment (usually `./venv/bin/python`)

### Configuring Python Settings

Create a `.vscode/settings.json` file in your project with these settings:

```json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.pylintPath": "${workspaceFolder}/venv/bin/pylint",
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.pytestPath": "${workspaceFolder}/venv/bin/pytest",
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.formatting.blackPath": "${workspaceFolder}/venv/bin/black",
    "python.sortImports.args": ["--profile", "black"],
    "files.exclude": {
        "**/__pycache__": true,
        "**/.pytest_cache": true,
        "**/*.pyc": true
    }
}
```

For Windows (non-WSL) users, replace `/bin/` with `/Scripts/` in the paths.

## Debugging Python in VS Code

### Setting Up Debugging

1. Click the Run and Debug icon in the Activity Bar
2. Click "create a launch.json file"
3. Select "Python"
4. Choose "Python File" for simple scripts or "Python: Django" for Django projects

Example `launch.json` file:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: Debug Tests",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "purpose": ["debug-test"],
            "console": "integratedTerminal",
            "justMyCode": false
        }
    ]
}
```

### Using the Debugger

1. Set breakpoints by clicking in the left margin
2. Start debugging with F5
3. Use the debug toolbar to step through code
4. Inspect variables in the Variables panel

## Terminal Integration

### Using the Integrated Terminal

1. Open the terminal with `` Ctrl+` `` (backtick)
2. Select the appropriate shell:
   - WSL2: Ubuntu (or your distro)
   - Windows: PowerShell or Command Prompt
   - macOS/Linux: bash, zsh, etc.

### Activating Virtual Environments

The terminal will open in your project directory. Activate your virtual environment:

```bash
# On WSL2, macOS, or Linux:
source venv/bin/activate

# On Windows Command Prompt:
venv\Scripts\activate

# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
```

## Working with Linting and Testing

### Linting with Pylint

1. Ensure pylint is installed in your virtual environment:
   ```bash
   pip install pylint
   ```

2. Linting will run automatically when you open Python files
3. View problems in the Problems panel
4. Configure rules in `.pylintrc` or settings.json

### Running Tests

1. Ensure pytest is installed:
   ```bash
   pip install pytest
   ```

2. Click the Testing icon in the Activity Bar
3. Click "Discover Tests"
4. Run tests by clicking the play button

## Platform-Specific Tips

### Windows (WSL2)

- Always use the WSL terminal for commands
- Keep your code in the Linux filesystem for best performance
- Use forward slashes (/) in paths, even in settings files

### macOS

- If using zsh, consider adding virtual environment activation to your `.zshrc`
- Install Command Line Tools for best experience: `xcode-select --install`

### Linux

- Ensure you have build tools installed for some packages:
  ```bash
  sudo apt install build-essential
  ```

## VS Code Keyboard Shortcuts

| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Open Command Palette | Ctrl+Shift+P | Cmd+Shift+P |
| Quick Open File | Ctrl+P | Cmd+P |
| Toggle Terminal | Ctrl+` | Cmd+` |
| Format Document | Shift+Alt+F | Shift+Option+F |
| Start Debugging | F5 | F5 |
| Toggle Breakpoint | F9 | F9 |
| Step Over | F10 | F10 |
| Step Into | F11 | F11 |

## Troubleshooting VS Code Issues

### Python Extension Not Working

1. Check that the Python extension is installed
2. Ensure the correct interpreter is selected
3. Try reloading VS Code

### Path Issues in WSL2

If VS Code can't find Python or tools in WSL2:
1. Make sure you opened VS Code from WSL with `code .`
2. Check that the Remote-WSL extension is installed
3. Verify your paths use forward slashes and are relative to your workspace

### Virtual Environment Not Recognized

1. Make sure the virtual environment is created and activated
2. Select the correct interpreter from the virtual environment
3. Try reopening the folder in VS Code

## Next Steps

Now that your VS Code environment is set up, check out these guides:

- [Development Workflow](02-development-workflow.md) for best practices
- [Testing with pytest](03-testing.md) to learn test-driven development
- [Code Quality with pylint](04-code-quality.md) for writing better code
