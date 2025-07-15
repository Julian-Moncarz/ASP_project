# SLEEC to Clingo Converter Tests

Test suite for validating the SLEEC to Clingo converter functionality.

## Running Tests

### Quick Start

```bash
# Install test dependencies
pip install -r tests/requirements.txt

# Run all tests
python tests/run_tests.py

# Or use pytest directly
pytest tests/
```

### Test Categories

Run specific test types using the custom runner:

```bash
python tests/run_tests.py unit         # Individual method tests
python tests/run_tests.py integration  # Full conversion pipeline tests  
python tests/run_tests.py behavioral   # Rule compliance tests
python tests/run_tests.py regression   # Known working cases
```

Or with pytest markers:

```bash
pytest tests/ -m unit
pytest tests/ -m integration
pytest tests/ -m behavioral
pytest tests/ -m regression
```

## Test Structure

```
tests/
├── test_converter.py      # All test cases
├── run_tests.py          # Test runner script
├── test_cases/           # SLEEC input files for testing
│   ├── simple/           # Basic patterns
│   ├── complex/          # Advanced patterns
│   ├── edge_cases/       # Boundary conditions
│   └── regression/       # Known working cases
└── expected_outputs/     # Expected Clingo outputs
```

## Test Coverage

The tests cover:
- Individual converter methods (unit tests)
- Complete SLEEC to Clingo conversion (integration tests)
- Generated Clingo rule compliance (behavioral tests)
- Known working systems (regression tests)
- Edge cases and error handling

## Adding Tests

1. Add SLEEC test files to appropriate `test_cases/` subdirectory
2. Add test methods to `test_converter.py` with appropriate pytest markers
3. Run tests to verify functionality

## Requirements

- Python 3.7+
- pytest 7.0+
- Dependencies in `requirements.txt`

Run from project root directory to avoid import issues.
