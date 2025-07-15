# SLEEC to Clingo Converter Test Suite

This comprehensive test suite validates the correctness, reliability, and robustness of the SLEEC to Clingo converter.

## 📁 Structure

```
tests/
├── __init__.py                     # Test package initialization
├── test_converter.py               # Main test suite
├── run_tests.py                    # Custom test runner
├── pytest.ini                     # Pytest configuration
├── requirements.txt                # Test dependencies
├── README.md                       # This file
├── test_cases/                     # SLEEC test files
│   ├── simple/                     # Basic rule patterns
│   │   ├── single_event.sleec
│   │   ├── single_measure.sleec
│   │   ├── event_and_measure.sleec
│   │   └── multiple_rules.sleec
│   ├── complex/                    # Advanced patterns
│   │   ├── nested_conditions.sleec
│   │   ├── multiple_measures.sleec
│   │   ├── event_chains.sleec
│   │   └── complex_logic.sleec
│   ├── edge_cases/                 # Boundary conditions
│   │   ├── empty_rules.sleec
│   │   ├── single_condition.sleec
│   │   ├── no_measures.sleec
│   │   └── no_events.sleec
│   └── regression/                 # Known working cases
│       ├── door.sleec
│       ├── lightswitch.sleec
│       └── ASPEN_R1_R2.sleec
└── expected_outputs/               # Expected Clingo outputs (future)
```

## 🧪 Test Categories

### 1. Unit Tests

Test individual converter methods in isolation:

- **Condition conversion** - SLEEC conditions → Clingo antecedents
- **Parentheses handling** - Logical grouping syntax fixes
- **Event identification** - Triggering vs action event classification
- **Rule generation** - Individual rule component creation

### 2. Integration Tests

Test complete conversion pipeline:

- **Full conversion** - SLEEC file → valid Clingo program
- **Syntax validation** - Generated Clingo passes syntax checks
- **Section generation** - All required sections present and correct

### 3. Behavioral Tests

Test logical correctness and rule compliance:

- **Rule satisfaction** - Generated models comply with SLEEC rules
- **Choice rules** - Proper event/measure instantiation
- **Multi-rule interaction** - Complex rule sets work correctly

### 4. Regression Tests

Test known working cases to prevent regressions:

- **Door system** - Security alarm rules
- **Lightswitch system** - Multi-rule event chains
- **ASPEN system** - Complex conditional logic

### 5. Edge Case Tests

Test boundary conditions and error handling:

- **Empty rule sets** - No rules defined
- **Minimal files** - Single rule/event/measure
- **Error conditions** - Invalid SLEEC syntax

## 🚀 Running Tests

### Option 1: Using pytest (recommended)

```bash
# Install dependencies
pip install -r tests/requirements.txt

# Run all tests
pytest tests/

# Run specific categories
pytest tests/ -m unit
pytest tests/ -m integration  
pytest tests/ -m behavioral
pytest tests/ -m regression

# Run with coverage
pytest tests/ --cov=converter --cov-report=html
```

### Option 2: Using custom runner

```bash
# Run all tests
python tests/run_tests.py

# Run specific categories  
python tests/run_tests.py unit
python tests/run_tests.py integration
python tests/run_tests.py behavioral
python tests/run_tests.py regression
```

### Option 3: Direct execution

```bash
# Run main test file directly
python tests/test_converter.py
```

## ✅ Test Results Interpretation

### Success Indicators

- **Unit tests pass** - Individual methods work correctly
- **Integration tests pass** - Full pipeline generates valid output
- **Behavioral tests pass** - Logic compliance verified
- **Regression tests pass** - No functionality broken

### Failure Investigation

1. **Unit test failures** - Check method implementation
2. **Integration failures** - Check syntax generation
3. **Behavioral failures** - Check rule logic compliance
4. **Regression failures** - Compare with known working outputs

## 📊 Coverage Goals

- **100% method coverage** for core conversion logic
- **90%+ line coverage** for entire converter
- **All known edge cases** covered by tests
- **All regression cases** passing consistently

## 🔧 Adding New Tests

### For new SLEEC features:

1. Add test case files to appropriate `test_cases/` subdirectory
2. Add unit tests for new methods in `test_converter.py`
3. Add integration test for complete feature
4. Update this README

### For bug fixes:

1. Add regression test reproducing the bug
2. Verify test fails before fix
3. Apply fix and verify test passes
4. Add to regression suite

## 🐛 Common Issues

### Import Errors

- **Symptom**: `ModuleNotFoundError` for converters
- **Solution**: Run tests from project root directory

### Clingo Not Available

- **Symptom**: Syntax validation tests skipped
- **Solution**: Install clingo or run non-syntax tests only

### Path Issues

- **Symptom**: SLEEC test files not found
- **Solution**: Ensure test_cases/ directory structure is correct

## 📈 Performance Benchmarks

The test suite should complete within:

- **Unit tests**: < 5 seconds
- **Integration tests**: < 15 seconds
- **Behavioral tests**: < 30 seconds
- **Full suite**: < 60 seconds

## 🔄 CI/CD Integration

This test suite is designed for integration with:

- **GitHub Actions** - Automated testing on push/PR
- **Pre-commit hooks** - Quick validation before commits
- **Nightly builds** - Extended testing with large rule sets

## 📝 Test Writing Guidelines

1. **Descriptive names** - Clear test purpose from name
2. **Single responsibility** - One concept per test
3. **Comprehensive assertions** - Check all expected behaviors
4. **Good error messages** - Clear failure diagnosis
5. **Fast execution** - Optimize for quick feedback

## 🎯 Success Metrics

A successful test run indicates:

- ✅ Converter generates syntactically valid Clingo
- ✅ Generated models comply with SLEEC rule semantics
- ✅ No regressions in known working cases
- ✅ Edge cases handled gracefully
- ✅ Error conditions managed appropriately

## 📚 Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Clingo Documentation](https://potassco.org/clingo/)
- [SLEEC Language Guide](../language guides/sleec_guide.md)
- [Converter README](../converter/README.md)
