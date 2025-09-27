# Configuration Management

This guide covers modern Python configuration management patterns and best practices for handling settings, secrets, and environment-specific configurations.

## Understanding Configuration Management

Configuration management involves handling settings that change between environments (development, testing, production) or based on deployment requirements. Proper configuration management makes applications:

- **Portable**: Easy to deploy across different environments
- **Secure**: Keeps sensitive information safe
- **Maintainable**: Clear separation of code and configuration
- **Flexible**: Easy to modify behavior without code changes

## Configuration Sources

Modern applications typically get configuration from multiple sources, in order of precedence:

1. **Command-line arguments**: Highest priority
2. **Environment variables**: Common for cloud deployments
3. **Configuration files**: TOML, YAML, JSON, or INI files
4. **Default values**: Fallback values in code

## Environment Variables

Environment variables are the most common way to configure applications, especially in cloud environments.

### Using Environment Variables in Python

```python
import os

# Basic usage
database_url = os.getenv('DATABASE_URL', 'sqlite:///default.db')
debug_mode = os.getenv('DEBUG', 'False').lower() == 'true'

# Type conversion
port = int(os.getenv('PORT', '8000'))
timeout = float(os.getenv('TIMEOUT', '30.0'))
```

### Environment Variable Best Practices

- Use UPPERCASE names with underscores: `DATABASE_URL`, `API_KEY`
- Provide sensible defaults for non-sensitive settings
- Never commit `.env` files with real secrets to version control
- Use descriptive names that indicate the purpose

### Using python-dotenv

For development environments, use python-dotenv to load variables from a `.env` file:

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY')
```

Example `.env` file:
```
DATABASE_URL=postgresql://localhost/myapp_dev
API_KEY=your-development-api-key
DEBUG=True
LOG_LEVEL=DEBUG
```

## Configuration Files

### TOML Configuration (Recommended)

TOML (Tom's Obvious, Minimal Language) is increasingly popular for Python configuration:

```bash
pip install tomli  # Python 3.10 and earlier
# Python 3.11+ includes tomllib in the standard library
```

Example `config.toml`:
```toml
[database]
host = "localhost"
port = 5432
name = "myapp"

[api]
base_url = "https://api.example.com"
timeout = 30.0
retry_attempts = 3

[logging]
level = "INFO"
format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

Python code to read TOML:
```python
import tomli

def load_config():
    with open("config.toml", "rb") as f:
        config = tomli.load(f)
    return config

config = load_config()
db_host = config["database"]["host"]
api_timeout = config["api"]["timeout"]
```

### YAML Configuration

YAML is human-readable but requires an external library:

```bash
pip install PyYAML
```

Example `config.yaml`:
```yaml
database:
  host: localhost
  port: 5432
  name: myapp

api:
  base_url: https://api.example.com
  timeout: 30.0
  retry_attempts: 3

logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

## Pydantic for Configuration Validation

Pydantic provides excellent configuration management with type validation:

```bash
pip install pydantic[dotenv]
```

```python
from pydantic import BaseSettings, Field
from typing import Optional

class DatabaseConfig(BaseSettings):
    host: str = "localhost"
    port: int = 5432
    name: str
    user: str
    password: str
    
    class Config:
        env_prefix = "DB_"  # Environment variables start with DB_

class APIConfig(BaseSettings):
    base_url: str
    api_key: str = Field(..., min_length=10)  # Required, minimum length
    timeout: float = 30.0
    
    class Config:
        env_prefix = "API_"

class AppConfig(BaseSettings):
    debug: bool = False
    log_level: str = "INFO"
    database: DatabaseConfig = DatabaseConfig()
    api: APIConfig = APIConfig()
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Usage
config = AppConfig()
print(f"Database host: {config.database.host}")
print(f"API timeout: {config.api.timeout}")
```

## Secrets Management

### Development Secrets

For development, use `.env` files but never commit them:

```bash
# Add to .gitignore
.env
.env.local
.env.*.local
```

Create a `.env.example` file to document required variables:
```
DATABASE_URL=postgresql://user:password@localhost/dbname
API_KEY=your-api-key-here
SECRET_KEY=your-secret-key-here
```

### Production Secrets

In production, never store secrets in files. Use:

- **Cloud provider secret managers**: AWS Secrets Manager, Azure Key Vault, etc.
- **Environment variables**: Set by deployment system
- **Container orchestration secrets**: Kubernetes secrets, Docker secrets
- **HashiCorp Vault**: For complex secret management needs

## Configuration Patterns

### Factory Pattern for Configuration

```python
from abc import ABC, abstractmethod

class Config(ABC):
    """Base configuration class."""
    DEBUG = False
    TESTING = False
    
    @abstractmethod
    def init_app(self, app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = "sqlite:///dev.db"
    
    def init_app(self, app):
        pass

class ProductionConfig(Config):
    DATABASE_URL = os.getenv('DATABASE_URL')
    
    def init_app(self, app):
        # Production-specific initialization
        pass

class TestingConfig(Config):
    TESTING = True
    DATABASE_URL = "sqlite:///:memory:"
    
    def init_app(self, app):
        pass

# Configuration factory
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
```

### Hierarchical Configuration

```python
class ConfigManager:
    def __init__(self):
        self.config = {}
        self.load_defaults()
        self.load_config_file()
        self.load_environment()
    
    def load_defaults(self):
        """Load default configuration values."""
        self.config.update({
            'debug': False,
            'port': 8000,
            'host': 'localhost'
        })
    
    def load_config_file(self):
        """Load configuration from file if it exists."""
        try:
            with open('config.toml', 'rb') as f:
                file_config = tomli.load(f)
                self.config.update(file_config)
        except FileNotFoundError:
            pass
    
    def load_environment(self):
        """Load configuration from environment variables."""
        env_mapping = {
            'APP_DEBUG': ('debug', bool),
            'APP_PORT': ('port', int),
            'APP_HOST': ('host', str),
        }
        
        for env_var, (config_key, type_func) in env_mapping.items():
            value = os.getenv(env_var)
            if value is not None:
                if type_func == bool:
                    self.config[config_key] = value.lower() == 'true'
                else:
                    self.config[config_key] = type_func(value)
    
    def get(self, key, default=None):
        return self.config.get(key, default)
```

## Configuration for Calculator Project

For your calculator project, create a simple configuration system:

```python
# src/calculator/config.py
import os
from pathlib import Path

class CalculatorConfig:
    """Configuration for the calculator application."""
    
    # Application settings
    PRECISION = int(os.getenv('CALC_PRECISION', '10'))
    MAX_HISTORY = int(os.getenv('CALC_MAX_HISTORY', '100'))
    
    # Display settings
    DISPLAY_WIDTH = int(os.getenv('CALC_DISPLAY_WIDTH', '20'))
    SCIENTIFIC_NOTATION = os.getenv('CALC_SCI_NOTATION', 'False').lower() == 'true'
    
    # File paths
    BASE_DIR = Path(__file__).parent.parent.parent
    CONFIG_DIR = BASE_DIR / 'config'
    LOG_DIR = BASE_DIR / 'logs'
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = LOG_DIR / 'calculator.log'
    
    @classmethod
    def init_directories(cls):
        """Create necessary directories."""
        cls.CONFIG_DIR.mkdir(exist_ok=True)
        cls.LOG_DIR.mkdir(exist_ok=True)
```

Usage in your calculator:
```python
from calculator.config import CalculatorConfig

class Calculator:
    def __init__(self):
        self.config = CalculatorConfig()
        self.config.init_directories()
        self.memory = 0
        self.history = []
        self.max_history = self.config.MAX_HISTORY
    
    def format_result(self, result):
        """Format result based on configuration."""
        if self.config.SCIENTIFIC_NOTATION and abs(result) > 10**6:
            return f"{result:.{self.config.PRECISION}e}"
        return f"{result:.{self.config.PRECISION}f}".rstrip('0').rstrip('.')
```

## Testing Configuration

Always test your configuration logic:

```python
# tests/test_config.py
import os
import pytest
from unittest.mock import patch
from calculator.config import CalculatorConfig

def test_default_configuration():
    """Test default configuration values."""
    config = CalculatorConfig()
    assert config.PRECISION == 10
    assert config.MAX_HISTORY == 100

@patch.dict(os.environ, {'CALC_PRECISION': '5', 'CALC_MAX_HISTORY': '50'})
def test_environment_override():
    """Test that environment variables override defaults."""
    config = CalculatorConfig()
    assert config.PRECISION == 5
    assert config.MAX_HISTORY == 50

def test_boolean_environment_variables():
    """Test boolean environment variable parsing."""
    with patch.dict(os.environ, {'CALC_SCI_NOTATION': 'true'}):
        config = CalculatorConfig()
        assert config.SCIENTIFIC_NOTATION is True
    
    with patch.dict(os.environ, {'CALC_SCI_NOTATION': 'false'}):
        config = CalculatorConfig()
        assert config.SCIENTIFIC_NOTATION is False
```

## Common Pitfalls

- **Hardcoding sensitive information**: Never put passwords or API keys in code
- **Not providing defaults**: Always have sensible fallback values
- **Type confusion**: Remember environment variables are strings
- **Configuration drift**: Keep development and production configs in sync
- **Overly complex configuration**: Start simple and add complexity as needed

## Best Practices Summary

1. **Use environment variables** for deployment-specific settings
2. **Provide sensible defaults** for development
3. **Validate configuration** at application startup
4. **Document configuration options** in README or code comments
5. **Never commit secrets** to version control
6. **Use type hints** and validation libraries like Pydantic
7. **Test configuration logic** like any other code
8. **Keep it simple** - don't over-engineer configuration

## Further Resources

- [The Twelve-Factor App: Config](https://12factor.net/config)
- [Pydantic Settings](https://pydantic-docs.helpmanual.io/usage/settings/)
- [Python-dotenv Documentation](https://python-dotenv.readthedocs.io/)
- [TOML Specification](https://toml.io/en/)
- [Environment Variables in Python](https://realpython.com/python-environment-variables/)
