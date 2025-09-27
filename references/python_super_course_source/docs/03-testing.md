# Testing with pytest

This guide explains how to write and run tests using pytest.

## Setting Up pytest

Ensure pytest is installed in your virtual environment:

```bash
pip install pytest
```

## Writing Your First Test

Create a file named `test_example.py`:

```python
# A simple function to test
def add(a, b):
    return a + b

# A test function
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

## Running Tests

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run a specific test file
pytest test_example.py

# Run a specific test function
pytest test_example.py::test_add
```

## Test Structure

Good tests follow the AAA pattern:
- **Arrange**: Set up test data
- **Act**: Call the function being tested
- **Assert**: Check if the result matches the expected outcome

Example:

```python
def test_user_creation():
    # Arrange
    name = "John"
    email = "john@example.com"
    
    # Act
    user = create_user(name, email)
    
    # Assert
    assert user.name == name
    assert user.email == email
    assert user.is_active == True
```

## Fixtures

Fixtures are a way to set up preconditions for your tests:

```python
import pytest

@pytest.fixture
def sample_data():
    return {
        'name': 'Test User',
        'email': 'test@example.com',
        'age': 25
    }

def test_user_properties(sample_data):
    user = create_user(sample_data['name'], sample_data['email'])
    assert user.name == sample_data['name']
    assert user.email == sample_data['email']
```

## Parameterized Tests

Test multiple inputs with a single test function:

```python
import pytest

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, -5, 0),
    (100, 200, 300),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
```

## Test Coverage

To check your test coverage:

```bash
# Install coverage tool
pip install pytest-cov

# Run tests with coverage report
pytest --cov=your_package_name

# Generate HTML coverage report
pytest --cov=your_package_name --cov-report=html
```

## Performance Testing Considerations

While unit tests focus on correctness, performance testing ensures your code meets speed and resource requirements.

### Basic Performance Testing with pytest

```python
import time
import pytest

def test_function_performance():
    """Test that a function completes within acceptable time."""
    start_time = time.time()
    
    # Call your function
    result = slow_function()
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    # Assert the function completes within 1 second
    assert execution_time < 1.0
    assert result is not None
```

### Using pytest-benchmark

For more sophisticated performance testing:

```bash
pip install pytest-benchmark
```

```python
def test_add_performance(benchmark):
    """Benchmark the add function."""
    result = benchmark(add, 100, 200)
    assert result == 300

def test_complex_calculation_performance(benchmark):
    """Benchmark a complex calculation."""
    def complex_calc():
        return sum(i**2 for i in range(1000))
    
    result = benchmark(complex_calc)
    assert result > 0
```

### Performance Testing Best Practices

- **Baseline measurements**: Establish performance baselines for critical functions
- **Consistent environment**: Run performance tests in consistent environments
- **Statistical significance**: Run multiple iterations to account for variance
- **Resource monitoring**: Monitor memory usage, not just execution time
- **Regression detection**: Fail tests if performance degrades significantly

### Memory Testing

```python
import tracemalloc

def test_memory_usage():
    """Test that function doesn't use excessive memory."""
    tracemalloc.start()
    
    # Your function call
    result = memory_intensive_function()
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Assert memory usage is reasonable (in bytes)
    assert peak < 1024 * 1024  # Less than 1MB
    assert result is not None
```

### When to Use Performance Tests

- **Critical performance paths**: Functions that affect user experience
- **Resource-intensive operations**: File I/O, database queries, calculations
- **Scalability validation**: Ensure code scales with input size
- **Regression prevention**: Catch performance regressions early

## Next Steps

After writing tests, learn how to ensure code quality with [pylint](04-code-quality.md).
