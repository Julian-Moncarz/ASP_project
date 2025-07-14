# SLEEC to Clingo Converters Package

This package contains two SLEEC to Clingo converters that share a common parsing foundation.

## Package Structure

```
converters/
├── __init__.py          # Package exports and imports
├── parser.py            # Shared SLEEC parsing logic
├── original_converter.py   # Original converter (direct rule translation)
├── dalal_converter.py      # Dalal's converter (antecedent/consequent structure)
├── README.md           # This file
├── README_original.md  # Original converter documentation
└── README_dalal.md     # Dalal converter documentation
```

## Quick Start

### As a Package (Recommended)

```python
from converters import SleecToClingoConverter, CorrectSleecConverter

# Original converter
original = SleecToClingoConverter()
clingo_code = original.convert_file("example.sleec")

# Dalal converter  
dalal = CorrectSleecConverter()
clingo_code = dalal.convert_file("example.sleec")
```

### Using Entry Scripts

From the project root:

```bash
# Original converter
python original_converter.py sleec_files/simple_rules/lightswitch.sleec

# Dalal converter  
python dalal_converter.py sleec_files/simple_rules/lightswitch.sleec
```

## Available Classes

### Converters
- **`SleecToClingoConverter`** - Original converter using direct rule translation
- **`CorrectSleecConverter`** - Dalal's converter using antecedent/consequent structure

### Shared Parser
- **`SleecParser`** - Shared SLEEC parsing functionality
- **`MeasureType`** - Enumeration for measure types (boolean, numeric, scale)

### Data Classes
- **`Event`** - Represents SLEEC events with line number tracking
- **`Measure`** - Represents SLEEC measures with type and scale information
- **`Constant`** - Represents SLEEC constants with values
- **`Rule`** - Represents SLEEC rules with conditions and actions

## Key Features

### Shared Benefits
✅ **Consistent parsing** - Both converters use the same robust parsing logic  
✅ **Validation** - Strict validation with helpful error messages and line numbers  
✅ **Line number tracking** - Precise error reporting with file locations  
✅ **Support for all SLEEC features** - Events, measures, constants, rules with otherwise clauses  

### Original Converter
- Direct rule translation following ASPEN.lp patterns
- Simple and straightforward Clingo generation
- Good for basic SLEEC rule translation

### Dalal Converter  
- Formal antecedent/consequent structure
- Rule satisfaction logic with triggering events
- More sophisticated semantic modeling

## Converter Comparison

| Feature | Original | Dalal |
|---------|----------|-------|
| **Rule Structure** | Direct translation | Antecedent/consequent |
| **Triggering Events** | All events can trigger | Only condition events trigger |
| **Rule Satisfaction** | Implicit | Explicit with `satisfied()` predicate |
| **Action Generation** | Direct `happens()` facts | Choice rules with constraints |
| **Complexity** | Simple | More sophisticated |
| **Use Case** | Basic rule translation | Formal semantic modeling |

## Error Handling

Both converters provide detailed error messages with:
- **Line numbers** for precise error location
- **Suggested fixes** for missing definitions  
- **Validation of all references** to ensure consistency

Example error output:
```
❌ Validation failed:
Error: Undefined event 'lighton' referenced in rule R1 at line 12

Please add these definitions to your SLEEC file:

Events:
event lighton
```

## Documentation

- **[Original Converter Documentation](README_original.md)** - Detailed documentation for the original converter
- **[Dalal Converter Documentation](README_dalal.md)** - Detailed documentation for Dalal's converter

## Example Usage

See the individual README files for comprehensive examples and usage patterns for each converter. 