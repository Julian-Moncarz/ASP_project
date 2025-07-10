# SLEEC to Clingo Converter

This tool automatically converts simple SLEEC rules into Clingo (Answer Set Programming) format, following the pattern established in your ASPEN.lp file.

## Features

- **Automatic parsing** of SLEEC definitions and rules
- **Event detection** from rule actions and conditions  
- **Measure handling** for boolean, numeric, and scale types
- **Rule translation** with proper logical operators
- **Conflict detection** built-in with contradiction checking
- **Clingo-compatible output** ready to run

## Usage

### Basic Usage

```bash
# From project root - Convert a single SLEEC file
python3 convert_sleec.py "sleec_test_examples/access_control_rules.sleec"

# From project root - Convert all SLEEC files  
python3 convert_sleec.py --all

# From sleec_converter directory
python3 -m test_converter "../sleec_test_examples/access_control_rules.sleec"

# Or use the converter directly in Python
python3 -c "
from sleec_converter import SleecToClingoConverter
converter = SleecToClingoConverter()
result = converter.convert_file('your_file.sleec')
print(result)
"
```

### SLEEC Input Format

Your SLEEC files should follow this structure:

```sleec
def_start
    // Events that can occur
    event EventName1
    event EventName2
    
    // Measures that can be evaluated
    measure measureName1: boolean
    measure measureName2: scale(value1, value2, value3)
    measure measureName3: numeric
    
    // Optional constants
    constant maxValue = 10
def_end

rule_start
    // Rules in the format: R<number> when <condition> then <action> [otherwise <action>]
    R1 when EventName1 and {measureName1} then EventName2
    R2 when EventName1 and ({measureName2} = value1) then EventName2 otherwise EventName3
rule_end
```

### Generated Clingo Structure

The converter generates well-structured Clingo code with these sections:

1. **Time Domain**: `time(0..10)` (configurable)
2. **Event Definitions**: All events from definitions and rules
3. **Measure Definitions**: All measures from definitions and rules  
4. **Measure Instantiation**: Choice rules for boolean/numeric, constraints for scales
5. **Triggering Events**: Choice rules for events that appear in `when` clauses
6. **Rule Implementations**: Your SLEEC rules converted to ASP logic
7. **Contradiction Detection**: Automatic conflict detection
8. **Output Specification**: What to show in answer sets

## Examples

### Example 1: Simple Access Control

**Input (access_control.sleec):**
```sleec
def_start
    event UserLogin
    event AccessGranted
    event AccessDenied
    
    measure hasValidCredentials: boolean
    measure securityLevel: scale(low, medium, high)
def_end

rule_start
    R1 when UserLogin and {hasValidCredentials} then AccessGranted
    R2 when UserLogin and ({securityLevel} = high) then AccessDenied otherwise AccessGranted
rule_end
```

**Generated Clingo output:**
```prolog
% Time domain
time(0..10).

% Events
event(UserLogin).
event(AccessGranted).
event(AccessDenied).

% Measures  
measure(hasValidCredentials).
measure(securityLevel).

% Measure instantiation
{ holds(hasValidCredentials, T) } :- time(T).
1 { holds(securityLevel, low, T) ; holds(securityLevel, medium, T) ; holds(securityLevel, high, T) } 1 :- time(T).

% Triggering events
{ happens(UserLogin, T) } :- time(T).

% Rule implementations
happens(AccessGranted, T) :- happens(UserLogin, T), holds(hasValidCredentials, T), time(T).
happens(AccessDenied, T) :- happens(UserLogin, T), holds(securityLevel, high, T), time(T).
happens(AccessGranted, T) :- not (happens(UserLogin, T), holds(securityLevel, high, T)), time(T).

% Contradiction detection
contradiction(E, T) :- happens(E, T), nothappens(E, T), event(E), time(T).

% Output
#show happens/2.
#show holds/2.  
#show holds/3.
#show contradiction/2.
```

### Example 2: Smart Home Lighting

**Input:**
```sleec
def_start
    event ButtonPress
    event LightOn
    event SetBrightnessToMax
    
    measure isNight: boolean
def_end

rule_start
    R1 when ButtonPress then LightOn
    R2 when LightOn and {isNight} then SetBrightnessToMax
rule_end
```

This generates a complete Clingo program that you can run with:
```bash
clingo generated_file.lp
```

## Advanced Features

### Custom Time Domain
```python
converter = SleecToClingoConverter(max_time=20)  # Use 0..20 instead of 0..10
```

### Implicit Definition Detection
The converter automatically detects:
- Events mentioned in rule actions but not explicitly defined
- Measures referenced in conditions but not explicitly defined
- Assigns sensible defaults (boolean for measures, triggering events for conditions)

### Contradiction Detection
Built-in detection of conflicting rules that would cause an event to both happen and not happen at the same time.

## Running the Generated Code

Once you have a generated `.lp` file, you can:

1. **Run with Clingo:**
   ```bash
   clingo your_generated_file.lp
   ```

2. **Test for conflicts:**
   ```bash
   clingo your_generated_file.lp --models=0
   ```

3. **Get specific time steps:**
   ```bash
   clingo your_generated_file.lp -c max_time=5
   ```

## Limitations and Future Improvements

### Current Limitations
- Simple negation logic for "otherwise" clauses
- No support for temporal operators (`within`, `until`, etc.)
- Basic scale measure comparisons
- No support for complex nested conditions

### Potential Enhancements
- Better temporal logic support
- More sophisticated condition parsing
- Support for numeric comparisons and arithmetic
- Integration with existing Clingo constraint libraries

## File Structure

```
sleec_converter/
├── __init__.py                    # Package initialization
├── sleec_to_clingo_converter.py   # Main converter class
├── test_converter.py              # Command-line interface
├── convert_all_sleec.py           # Batch converter
└── README_converter.md            # This documentation

convert_sleec.py                   # Main script (project root)
*_converted.lp                     # Generated Clingo files
```

The generated Clingo code follows the same patterns as your manually-created ASPEN.lp, ensuring consistency with your existing work.

## Important Notes

- **Lowercase atoms**: All event and measure names are automatically converted to lowercase to comply with Clingo requirements
- **Safe variables**: The converter ensures all variables are properly grounded in Clingo rules
- **Time domain**: Default time range is 0..10, configurable via `SleecToClingoConverter(max_time=N)` 