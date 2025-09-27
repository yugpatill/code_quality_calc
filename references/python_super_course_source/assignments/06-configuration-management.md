````markdown
# Assignment 6: Configuration Management and Environment Setup

## Learning Objectives
- Implement modern configuration management patterns
- Handle environment-specific settings and secrets
- Use environment variables and configuration files effectively
- Apply the 12-factor app methodology
- Implement logging and monitoring for production applications

## Background

Configuration management is crucial for building applications that work across different environments (development, testing, production). This assignment teaches you to handle settings, secrets, and environment-specific configurations professionally.

### The 12-Factor App Methodology

This assignment implements principles from the [12-Factor App](https://12factor.net/), specifically:
- **Config**: Store configuration in environment variables
- **Logs**: Treat logs as event streams
- **Dev/prod parity**: Keep development and production as similar as possible

Modern applications must be configurable without code changes and secure by default.

## Prerequisites
- Completed Assignments 1-5
- Calculator project with CI/CD pipeline
- Understanding of environment variables
- Basic knowledge of logging concepts

## Time to Complete
Expect to spend approximately 3-4 hours on this assignment.

## Part 1: Setting Up Configuration Architecture

### Task 1.1: Create Configuration Classes

1. Create `src/calculator/config.py`:
   ```python
   """Configuration management for the calculator application."""
   import os
   from pathlib import Path
   from typing import Optional
   from pydantic import BaseSettings, Field, validator
   
   
   class DatabaseConfig(BaseSettings):
       """Database configuration settings."""
       url: str = Field(default="sqlite:///calculator.db")
       pool_size: int = Field(default=5, ge=1, le=20)
       echo: bool = Field(default=False)
       
       class Config:
           env_prefix = "DB_"
   
   
   class LoggingConfig(BaseSettings):
       """Logging configuration settings."""
       level: str = Field(default="INFO")
       format: str = Field(
           default="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
       )
       file_path: Optional[str] = Field(default=None)
       max_bytes: int = Field(default=10_485_760)  # 10MB
       backup_count: int = Field(default=5)
       
       @validator('level')
       def validate_log_level(cls, v):
           valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
           if v.upper() not in valid_levels:
               raise ValueError(f'Log level must be one of: {valid_levels}')
           return v.upper()
       
       class Config:
           env_prefix = "LOG_"
   
   
   class CalculatorConfig(BaseSettings):
       """Main calculator application configuration."""
       # Application settings
       precision: int = Field(default=10, ge=2, le=15)
       max_history: int = Field(default=100, ge=10, le=1000)
       scientific_notation: bool = Field(default=False)
       
       # Display settings
       display_width: int = Field(default=20, ge=10, le=50)
       thousands_separator: bool = Field(default=True)
       
       # API settings
       api_host: str = Field(default="localhost")
       api_port: int = Field(default=8000, ge=1024, le=65535)
       api_debug: bool = Field(default=False)
       
       # Security
       secret_key: str = Field(default="dev-secret-key-change-in-production")
       
       # File paths
       base_dir: Path = Field(default_factory=lambda: Path(__file__).parent.parent.parent)
       data_dir: Path = Field(default=None)
       log_dir: Path = Field(default=None)
       
       def __init__(self, **kwargs):
           super().__init__(**kwargs)
           if self.data_dir is None:
               self.data_dir = self.base_dir / "data"
           if self.log_dir is None:
               self.log_dir = self.base_dir / "logs"
       
       @validator('secret_key')
       def validate_secret_key(cls, v):
           if v == "dev-secret-key-change-in-production" and os.getenv("ENVIRONMENT") == "production":
               raise ValueError("Must set SECRET_KEY environment variable in production")
           return v
       
       class Config:
           env_prefix = "CALC_"
           env_file = ".env"
           env_file_encoding = "utf-8"
   
   
   class AppConfig(BaseSettings):
       """Complete application configuration."""
       environment: str = Field(default="development")
       debug: bool = Field(default=True)
       
       calculator: CalculatorConfig = Field(default_factory=CalculatorConfig)
       database: DatabaseConfig = Field(default_factory=DatabaseConfig)
       logging: LoggingConfig = Field(default_factory=LoggingConfig)
       
       @validator('environment')
       def validate_environment(cls, v):
           valid_envs = ['development', 'testing', 'staging', 'production']
           if v not in valid_envs:
               raise ValueError(f'Environment must be one of: {valid_envs}')
           return v
       
       @validator('debug')
       def debug_false_in_production(cls, v, values):
           if values.get('environment') == 'production' and v is True:
               raise ValueError('Debug must be False in production environment')
           return v
       
       def init_directories(self):
           """Create necessary directories."""
           self.calculator.data_dir.mkdir(exist_ok=True, parents=True)
           self.calculator.log_dir.mkdir(exist_ok=True, parents=True)
       
       class Config:
           env_file = ".env"
           env_file_encoding = "utf-8"
   
   
   # Global configuration instance
   config = AppConfig()
   ```

2. Update `requirements-dev.txt` to include Pydantic:
   ```
   # Add to existing requirements
   pydantic[dotenv]>=1.10.0
   ```

### Task 1.2: Create Environment Files

1. Create `.env.example` (template for environment variables):
   ```
   # Environment Configuration
   ENVIRONMENT=development
   DEBUG=true
   
   # Calculator Settings
   CALC_PRECISION=10
   CALC_MAX_HISTORY=100
   CALC_SCIENTIFIC_NOTATION=false
   CALC_DISPLAY_WIDTH=20
   CALC_API_HOST=localhost
   CALC_API_PORT=8000
   CALC_SECRET_KEY=your-secret-key-here
   
   # Database Settings
   DB_URL=sqlite:///calculator.db
   DB_POOL_SIZE=5
   DB_ECHO=false
   
   # Logging Settings
   LOG_LEVEL=INFO
   LOG_FORMAT="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
   LOG_FILE_PATH=logs/calculator.log
   LOG_MAX_BYTES=10485760
   LOG_BACKUP_COUNT=5
   ```

2. Create `.env` for local development:
   ```
   ENVIRONMENT=development
   DEBUG=true
   CALC_PRECISION=8
   LOG_LEVEL=DEBUG
   ```

3. Update `.gitignore` to exclude environment files:
   ```
   # Environment files
   .env
   .env.local
   .env.*.local
   
   # Data and logs
   data/
   logs/
   *.db
   ```

## Part 2: Implementing Logging System

### Task 2.1: Create Logging Module

1. Create `src/calculator/logging_config.py`:
   ```python
   """Logging configuration and setup."""
   import logging
   import logging.handlers
   from pathlib import Path
   from typing import Optional
   
   from .config import config
   
   
   def setup_logging(
       level: Optional[str] = None,
       log_file: Optional[str] = None,
       format_string: Optional[str] = None
   ) -> logging.Logger:
       """
       Set up application logging.
       
       Args:
           level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
           log_file: Path to log file (optional)
           format_string: Custom log format (optional)
           
       Returns:
           Configured logger instance
       """
       # Use config values if not provided
       level = level or config.logging.level
       log_file = log_file or config.logging.file_path
       format_string = format_string or config.logging.format
       
       # Create logger
       logger = logging.getLogger('calculator')
       logger.setLevel(getattr(logging, level))
       
       # Clear existing handlers
       logger.handlers.clear()
       
       # Create formatter
       formatter = logging.Formatter(format_string)
       
       # Console handler
       console_handler = logging.StreamHandler()
       console_handler.setLevel(getattr(logging, level))
       console_handler.setFormatter(formatter)
       logger.addHandler(console_handler)
       
       # File handler (if log file specified)
       if log_file:
           log_path = Path(log_file)
           log_path.parent.mkdir(parents=True, exist_ok=True)
           
           file_handler = logging.handlers.RotatingFileHandler(
               log_path,
               maxBytes=config.logging.max_bytes,
               backupCount=config.logging.backup_count
           )
           file_handler.setLevel(getattr(logging, level))
           file_handler.setFormatter(formatter)
           logger.addHandler(file_handler)
       
       return logger
   
   
   def get_logger(name: str) -> logging.Logger:
       """Get a logger with the specified name."""
       return logging.getLogger(f'calculator.{name}')
   ```

### Task 2.2: Update Calculator Classes with Logging

1. Update `src/calculator/calculator.py` to include logging:
   ```python
   """Calculator implementation with configuration and logging."""
   from typing import List, Union
   from .operations import add, subtract, multiply, divide
   from .scientific import square_root, power, sin, cos, tan
   from .config import config
   from .logging_config import get_logger
   
   
   logger = get_logger('calculator')
   
   
   class Calculator:
       """Calculator class with configuration and logging support."""
       
       def __init__(self):
           """Initialize calculator with configuration."""
           self.memory = 0.0
           self.history: List[str] = []
           self.display = "0"
           
           # Load configuration
           self.precision = config.calculator.precision
           self.max_history = config.calculator.max_history
           self.scientific_notation = config.calculator.scientific_notation
           self.display_width = config.calculator.display_width
           
           logger.info("Calculator initialized")
           logger.debug(f"Configuration: precision={self.precision}, "
                       f"max_history={self.max_history}, "
                       f"scientific_notation={self.scientific_notation}")
       
       def _format_result(self, result: float) -> str:
           """Format result according to configuration."""
           if self.scientific_notation and abs(result) > 10**6:
               formatted = f"{result:.{self.precision}e}"
           else:
               formatted = f"{result:.{self.precision}f}".rstrip('0').rstrip('.')
           
           # Handle thousands separator if enabled
           if config.calculator.thousands_separator and not self.scientific_notation:
               if '.' in formatted:
                   integer_part, decimal_part = formatted.split('.')
                   integer_part = f"{int(integer_part):,}"
                   formatted = f"{integer_part}.{decimal_part}"
               else:
                   formatted = f"{int(float(formatted)):,}"
           
           return formatted
       
       def _add_to_history(self, operation: str, a: float, b: float, result: float):
           """Add operation to history with size management."""
           formatted_result = self._format_result(result)
           history_entry = f"{a} {operation} {b} = {formatted_result}"
           
           self.history.append(history_entry)
           logger.debug(f"Added to history: {history_entry}")
           
           # Maintain history size limit
           while len(self.history) > self.max_history:
               removed = self.history.pop(0)
               logger.debug(f"Removed from history: {removed}")
       
       def add(self, a: float, b: float) -> float:
           """Add two numbers."""
           try:
               result = add(a, b)
               self._add_to_history('+', a, b, result)
               self.display = self._format_result(result)
               logger.info(f"Addition: {a} + {b} = {result}")
               return result
           except Exception as e:
               logger.error(f"Error in addition: {e}")
               raise
       
       def subtract(self, a: float, b: float) -> float:
           """Subtract b from a."""
           try:
               result = subtract(a, b)
               self._add_to_history('-', a, b, result)
               self.display = self._format_result(result)
               logger.info(f"Subtraction: {a} - {b} = {result}")
               return result
           except Exception as e:
               logger.error(f"Error in subtraction: {e}")
               raise
       
       def multiply(self, a: float, b: float) -> float:
           """Multiply two numbers."""
           try:
               result = multiply(a, b)
               self._add_to_history('*', a, b, result)
               self.display = self._format_result(result)
               logger.info(f"Multiplication: {a} * {b} = {result}")
               return result
           except Exception as e:
               logger.error(f"Error in multiplication: {e}")
               raise
       
       def divide(self, a: float, b: float) -> float:
           """Divide a by b."""
           try:
               result = divide(a, b)
               self._add_to_history('/', a, b, result)
               self.display = self._format_result(result)
               logger.info(f"Division: {a} / {b} = {result}")
               return result
           except Exception as e:
               logger.error(f"Error in division: {e}")
               raise
       
       def square_root(self, x: float) -> float:
           """Calculate square root of x."""
           try:
               result = square_root(x)
               history_entry = f"√{x} = {self._format_result(result)}"
               self.history.append(history_entry)
               self.display = self._format_result(result)
               logger.info(f"Square root: √{x} = {result}")
               return result
           except Exception as e:
               logger.error(f"Error in square root: {e}")
               raise
       
       def power(self, base: float, exponent: float) -> float:
           """Calculate base raised to the power of exponent."""
           try:
               result = power(base, exponent)
               self._add_to_history('^', base, exponent, result)
               self.display = self._format_result(result)
               logger.info(f"Power: {base} ^ {exponent} = {result}")
               return result
           except Exception as e:
               logger.error(f"Error in power: {e}")
               raise
       
       def memory_store(self, value: float):
           """Store a value in memory."""
           old_memory = self.memory
           self.memory = value
           logger.info(f"Memory store: {old_memory} -> {value}")
       
       def memory_recall(self) -> float:
           """Recall the value from memory."""
           logger.debug(f"Memory recall: {self.memory}")
           return self.memory
       
       def memory_clear(self):
           """Clear the memory."""
           old_memory = self.memory
           self.memory = 0.0
           logger.info(f"Memory cleared: {old_memory} -> 0.0")
       
       def get_history(self) -> List[str]:
           """Return the calculation history."""
           logger.debug(f"History requested: {len(self.history)} items")
           return self.history.copy()
       
       def clear_history(self):
           """Clear the calculation history."""
           history_size = len(self.history)
           self.history.clear()
           logger.info(f"History cleared: {history_size} items removed")
       
       def get_stats(self) -> dict:
           """Get calculator statistics."""
           stats = {
               'memory_value': self.memory,
               'history_count': len(self.history),
               'display': self.display,
               'precision': self.precision,
               'max_history': self.max_history
           }
           logger.debug(f"Stats requested: {stats}")
           return stats
   ```

## Part 3: Environment-Specific Configuration

### Task 3.1: Create Configuration for Different Environments

1. Create `config/development.env`:
   ```
   ENVIRONMENT=development
   DEBUG=true
   CALC_PRECISION=8
   CALC_MAX_HISTORY=50
   LOG_LEVEL=DEBUG
   LOG_FILE_PATH=logs/calculator-dev.log
   DB_URL=sqlite:///calculator-dev.db
   ```

2. Create `config/testing.env`:
   ```
   ENVIRONMENT=testing
   DEBUG=false
   CALC_PRECISION=6
   CALC_MAX_HISTORY=25
   LOG_LEVEL=WARNING
   DB_URL=sqlite:///:memory:
   ```

3. Create `config/production.env.example`:
   ```
   ENVIRONMENT=production
   DEBUG=false
   CALC_PRECISION=10
   CALC_MAX_HISTORY=100
   CALC_SECRET_KEY=your-production-secret-key
   LOG_LEVEL=INFO
   LOG_FILE_PATH=/var/log/calculator/calculator.log
   DB_URL=postgresql://user:pass@localhost/calculator_prod
   ```

### Task 3.2: Create Configuration Factory

1. Create `src/calculator/config_factory.py`:
   ```python
   """Configuration factory for different environments."""
   import os
   from pathlib import Path
   from typing import Dict, Type
   
   from .config import AppConfig
   
   
   class DevelopmentConfig(AppConfig):
       """Development environment configuration."""
       environment: str = "development"
       debug: bool = True
       
       class Config:
           env_file = "config/development.env"
   
   
   class TestingConfig(AppConfig):
       """Testing environment configuration."""
       environment: str = "testing"
       debug: bool = False
       
       class Config:
           env_file = "config/testing.env"
   
   
   class StagingConfig(AppConfig):
       """Staging environment configuration."""
       environment: str = "staging"
       debug: bool = False
       
       class Config:
           env_file = "config/staging.env"
   
   
   class ProductionConfig(AppConfig):
       """Production environment configuration."""
       environment: str = "production"
       debug: bool = False
       
       class Config:
           env_file = "config/production.env"
   
   
   # Configuration registry
   config_registry: Dict[str, Type[AppConfig]] = {
       'development': DevelopmentConfig,
       'testing': TestingConfig,
       'staging': StagingConfig,
       'production': ProductionConfig,
       'default': DevelopmentConfig
   }
   
   
   def get_config(environment: str = None) -> AppConfig:
       """
       Get configuration for the specified environment.
       
       Args:
           environment: Environment name (development, testing, staging, production)
           
       Returns:
           Configuration instance for the environment
       """
       if environment is None:
           environment = os.getenv('ENVIRONMENT', 'development')
       
       config_class = config_registry.get(environment, config_registry['default'])
       return config_class()
   
   
   def validate_config(config_instance: AppConfig) -> bool:
       """
       Validate configuration for the current environment.
       
       Args:
           config_instance: Configuration instance to validate
           
       Returns:
           True if configuration is valid
           
       Raises:
           ValueError: If configuration is invalid
       """
       # Validate required directories exist
       if not config_instance.calculator.base_dir.exists():
           raise ValueError(f"Base directory does not exist: {config_instance.calculator.base_dir}")
       
       # Production-specific validations
       if config_instance.environment == 'production':
           if config_instance.debug:
               raise ValueError("Debug mode must be disabled in production")
           
           if config_instance.calculator.secret_key == "dev-secret-key-change-in-production":
               raise ValueError("Must set production secret key")
           
           if 'localhost' in config_instance.database.url:
               raise ValueError("Production database should not use localhost")
       
       return True
   ```

## Part 4: Secrets Management

### Task 4.1: Implement Secrets Handling

1. Create `src/calculator/secrets.py`:
   ```python
   """Secure secrets management."""
   import os
   import base64
   from typing import Optional
   from cryptography.fernet import Fernet
   
   from .logging_config import get_logger
   
   
   logger = get_logger('secrets')
   
   
   class SecretsManager:
       """Manage application secrets securely."""
       
       def __init__(self, encryption_key: Optional[str] = None):
           """
           Initialize secrets manager.
           
           Args:
               encryption_key: Base64-encoded encryption key
           """
           if encryption_key is None:
               encryption_key = os.getenv('ENCRYPTION_KEY')
           
           if encryption_key:
               self.cipher = Fernet(encryption_key.encode())
               logger.info("Secrets manager initialized with encryption")
           else:
               self.cipher = None
               logger.warning("Secrets manager initialized without encryption")
       
       @staticmethod
       def generate_key() -> str:
           """Generate a new encryption key."""
           key = Fernet.generate_key()
           return key.decode()
       
       def encrypt_secret(self, secret: str) -> str:
           """
           Encrypt a secret value.
           
           Args:
               secret: Plain text secret to encrypt
               
           Returns:
               Base64-encoded encrypted secret
           """
           if not self.cipher:
               logger.warning("No encryption key available, returning plain text")
               return secret
           
           encrypted = self.cipher.encrypt(secret.encode())
           return base64.b64encode(encrypted).decode()
       
       def decrypt_secret(self, encrypted_secret: str) -> str:
           """
           Decrypt a secret value.
           
           Args:
               encrypted_secret: Base64-encoded encrypted secret
               
           Returns:
               Decrypted plain text secret
           """
           if not self.cipher:
               logger.warning("No encryption key available, returning as-is")
               return encrypted_secret
           
           try:
               encrypted_bytes = base64.b64decode(encrypted_secret.encode())
               decrypted = self.cipher.decrypt(encrypted_bytes)
               return decrypted.decode()
           except Exception as e:
               logger.error(f"Failed to decrypt secret: {e}")
               raise
       
       def get_secret(self, key: str, default: Optional[str] = None, encrypted: bool = False) -> Optional[str]:
           """
           Get a secret from environment variables.
           
           Args:
               key: Environment variable name
               default: Default value if not found
               encrypted: Whether the stored value is encrypted
               
           Returns:
               Secret value (decrypted if necessary)
           """
           value = os.getenv(key, default)
           if value and encrypted:
               return self.decrypt_secret(value)
           return value
   
   
   # Global secrets manager instance
   secrets_manager = SecretsManager()
   ```

2. Add cryptography to `requirements-dev.txt`:
   ```
   # Add to existing requirements
   cryptography>=3.4.0
   ```

### Task 4.2: Update Configuration to Use Secrets

1. Update `src/calculator/config.py` to integrate secrets:
   ```python
   # Add this import at the top
   from .secrets import secrets_manager
   
   # Update the CalculatorConfig class
   class CalculatorConfig(BaseSettings):
       # ... existing fields ...
       
       # Security
       secret_key: str = Field(default="dev-secret-key-change-in-production")
       
       def __init__(self, **kwargs):
           super().__init__(**kwargs)
           # ... existing initialization ...
           
           # Load secret key from secrets manager if available
           if secrets_manager:
               secret_from_env = secrets_manager.get_secret('SECRET_KEY', encrypted=True)
               if secret_from_env:
                   self.secret_key = secret_from_env
   ```

## Part 5: Testing Configuration

### Task 5.1: Create Configuration Tests

1. Create `tests/test_config.py`:
   ```python
   """Tests for configuration management."""
   import os
   import tempfile
   from pathlib import Path
   from unittest.mock import patch
   import pytest
   
   from calculator.config import AppConfig, CalculatorConfig
   from calculator.config_factory import get_config, validate_config
   from calculator.secrets import SecretsManager
   
   
   def test_default_configuration():
       """Test default configuration values."""
       config = CalculatorConfig()
       assert config.precision == 10
       assert config.max_history == 100
       assert config.scientific_notation is False
   
   
   @patch.dict(os.environ, {
       'CALC_PRECISION': '5',
       'CALC_MAX_HISTORY': '50',
       'CALC_SCIENTIFIC_NOTATION': 'true'
   })
   def test_environment_override():
       """Test that environment variables override defaults."""
       config = CalculatorConfig()
       assert config.precision == 5
       assert config.max_history == 50
       assert config.scientific_notation is True
   
   
   def test_configuration_validation():
       """Test configuration validation."""
       config = AppConfig()
       # Should not raise an exception
       assert validate_config(config) is True
   
   
   @patch.dict(os.environ, {'ENVIRONMENT': 'testing'})
   def test_testing_configuration():
       """Test testing environment configuration."""
       config = get_config('testing')
       assert config.environment == 'testing'
       assert config.debug is False
   
   
   def test_secrets_manager():
       """Test secrets manager functionality."""
       manager = SecretsManager()
       
       # Test encryption/decryption if key is available
       if manager.cipher:
           secret = "test-secret"
           encrypted = manager.encrypt_secret(secret)
           decrypted = manager.decrypt_secret(encrypted)
           assert decrypted == secret
   
   
   def test_secrets_manager_without_key():
       """Test secrets manager without encryption key."""
       manager = SecretsManager(encryption_key=None)
       secret = "test-secret"
       
       # Should return plain text when no encryption
       assert manager.encrypt_secret(secret) == secret
       assert manager.decrypt_secret(secret) == secret
   
   
   @patch.dict(os.environ, {
       'ENVIRONMENT': 'production',
       'DEBUG': 'true'
   })
   def test_production_validation_failure():
       """Test that production validation catches debug mode."""
       config = get_config('production')
       with pytest.raises(ValueError, match="Debug mode must be disabled"):
           validate_config(config)
   
   
   def test_directory_creation():
       """Test that configuration creates necessary directories."""
       with tempfile.TemporaryDirectory() as temp_dir:
           config = AppConfig()
           config.calculator.base_dir = Path(temp_dir)
           config.calculator.data_dir = Path(temp_dir) / "data"
           config.calculator.log_dir = Path(temp_dir) / "logs"
           
           config.init_directories()
           
           assert config.calculator.data_dir.exists()
           assert config.calculator.log_dir.exists()
   ```

### Task 5.2: Test Logging Configuration

1. Create `tests/test_logging.py`:
   ```python
   """Tests for logging configuration."""
   import logging
   import tempfile
   from pathlib import Path
   
   from calculator.logging_config import setup_logging, get_logger
   
   
   def test_basic_logging_setup():
       """Test basic logging setup."""
       logger = setup_logging(level='DEBUG')
       assert logger.name == 'calculator'
       assert logger.level == logging.DEBUG
   
   
   def test_file_logging():
       """Test file logging configuration."""
       with tempfile.TemporaryDirectory() as temp_dir:
           log_file = Path(temp_dir) / "test.log"
           logger = setup_logging(level='INFO', log_file=str(log_file))
           
           # Test logging
           logger.info("Test message")
           
           # Check file was created and contains message
           assert log_file.exists()
           content = log_file.read_text()
           assert "Test message" in content
   
   
   def test_get_logger():
       """Test getting named loggers."""
       setup_logging()
       logger = get_logger('test_module')
       assert logger.name == 'calculator.test_module'
   ```

## Part 6: Environment-Specific Deployment

### Task 6.1: Update CI/CD with Configuration

1. Update `.github/workflows/ci.yml` to test different environments:
   ```yaml
   # Add this job to your existing CI workflow
   test-environments:
     runs-on: ubuntu-latest
     strategy:
       matrix:
         environment: [development, testing, staging]
     
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
         pip install -e .
         pip install -r requirements-dev.txt
     
     - name: Test configuration
       env:
         ENVIRONMENT: ${{ matrix.environment }}
       run: |
         python -c "
         from calculator.config_factory import get_config, validate_config
         config = get_config('${{ matrix.environment }}')
         validate_config(config)
         print(f'Configuration valid for ${{ matrix.environment }}')
         "
     
     - name: Test logging
       env:
         ENVIRONMENT: ${{ matrix.environment }}
         LOG_LEVEL: INFO
       run: |
         python -c "
         from calculator.logging_config import setup_logging
         from calculator.calculator import Calculator
         setup_logging()
         calc = Calculator()
         calc.add(1, 2)
         print('Logging test completed')
         "
   ```

### Task 6.2: Create Configuration Documentation

1. Create `docs/configuration.md`:
   ```markdown
   # Configuration Guide
   
   ## Environment Variables
   
   ### Application Settings
   - `ENVIRONMENT`: Application environment (development/testing/staging/production)
   - `DEBUG`: Enable debug mode (true/false)
   
   ### Calculator Settings
   - `CALC_PRECISION`: Number precision (2-15, default: 10)
   - `CALC_MAX_HISTORY`: Maximum history entries (10-1000, default: 100)
   - `CALC_SCIENTIFIC_NOTATION`: Use scientific notation (true/false, default: false)
   - `CALC_SECRET_KEY`: Application secret key (required in production)
   
   ### Database Settings
   - `DB_URL`: Database connection URL
   - `DB_POOL_SIZE`: Connection pool size (1-20, default: 5)
   - `DB_ECHO`: Enable SQL logging (true/false, default: false)
   
   ### Logging Settings
   - `LOG_LEVEL`: Logging level (DEBUG/INFO/WARNING/ERROR/CRITICAL)
   - `LOG_FILE_PATH`: Path to log file (optional)
   - `LOG_MAX_BYTES`: Maximum log file size in bytes
   - `LOG_BACKUP_COUNT`: Number of backup log files
   
   ## Security
   
   ### Secrets Management
   - Use environment variables for sensitive data
   - Never commit secrets to version control
   - Use encryption for stored secrets in production
   - Rotate secrets regularly
   
   ### Production Checklist
   - [ ] Set `ENVIRONMENT=production`
   - [ ] Set `DEBUG=false`
   - [ ] Configure production database
   - [ ] Set secure `SECRET_KEY`
   - [ ] Configure log file paths
   - [ ] Set up monitoring and alerting
   ```

## Common Pitfalls

- **Hardcoding configuration**: Always use environment variables for deployment-specific settings
- **Committing secrets**: Never commit `.env` files or secrets to version control
- **Missing validation**: Always validate configuration at startup
- **Log file permissions**: Ensure log directories are writable in production
- **Configuration drift**: Keep development and production configurations in sync

## What Success Looks Like

By the end of this assignment, you should have:
- A robust configuration system that works across all environments
- Proper secrets management with encryption support
- Comprehensive logging throughout your application
- Environment-specific configuration files
- Validated configuration in your CI/CD pipeline

## Self-Assessment Questions

1. How does proper configuration management improve application security?
2. What are the benefits of the 12-factor app methodology?
3. How would you handle database credentials in different environments?
4. What logging information is most valuable for debugging production issues?
5. How does configuration validation prevent deployment problems?

## Submission Requirements

Submit the following:

1. Your updated calculator project with complete configuration management
2. Evidence of environment-specific configurations working
3. Test results showing configuration validation
4. A reflection document (400-600 words) addressing:
   - How configuration management changes your development process
   - Security considerations for different environments
   - The importance of logging in production applications
   - How these practices scale to larger applications

## Additional Resources

- [The 12-Factor App](https://12factor.net/)
- [Pydantic Settings Documentation](https://pydantic-docs.helpmanual.io/usage/settings/)
- [Python Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Secrets Management Best Practices](https://www.vaultproject.io/docs/secrets)
- [Environment Variables in Python](https://realpython.com/python-environment-variables/)

````