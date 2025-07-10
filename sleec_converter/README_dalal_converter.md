# Correct SLEEC Converter (Dalal's Format)

This converter transforms SLEEC rules into Clingo format following **Dalal's approach**, which uses antecedent/consequent structure and rule satisfaction logic.

## Key Features

- **Antecedent/Consequent Structure**: Rules are broken down into `antecedent(rule_id, T)` and `consequent(rule_id, T)` predicates
- **Rule Satisfaction Logic**: Implements `holds()`, `holds_nv()`, and `holds_v()` predicates for proper rule evaluation
- **Hard Constraints**: Enforces rule satisfaction with `:- exp(R), time(T), not holds(R,T).`
- **Proper Action Generation**: Uses appropriate choice rules for event generation
- **Measure Support**: Handles boolean, numeric, and scale measures correctly

## Usage

### Convert a Single File

```python
from sleec_converter import CorrectSleecConverter

converter = CorrectSleecConverter(max_time=10)
clingo_code = converter.convert_file("example.sleec")
print(clingo_code)

# Or from string
sleec_content = """
def_start
    event OpenDoor
    event PlaySound
    measure isDaytime: boolean
def_end

rule_start
    R1 when OpenDoor and {isDaytime} then PlaySound
rule_end
"""
clingo_code = converter.convert_sleec_string(sleec_content)
```

### Convert All SLEEC Files

```bash
cd sleec_converter
python convert_all_sleec_dalal.py
```

This will:
1. Find all `.sleec` files in the project
2. Convert each to Dalal format
3. Save as `{filename}_dalal.lp`
4. Provide a conversion summary

## Output Format

The converter generates Clingo code with the following structure:

### 1. Domain Definitions
- Uses `event()` declarations for events when measures are present
- Uses `action()` declarations for simple cases without measures
- Includes `measure()` declarations for all measures
- Defines time domain `time(0..N)`

### 2. SLEEC Rule Definition
- Declares rules with `exp(rule_id)`
- Separates antecedent logic: `antecedent(rule_id, T) :- conditions.`
- Separates consequent logic: `consequent(rule_id, T) :- actions.`

### 3. Rule Satisfaction Logic
- General holds logic for non-vacuous and vacuous satisfaction
- Specific holds logic for each rule
- Hard constraints ensuring all rules are satisfied

### 4. Action Generation
- Choice rules: `0{happens(A,T):event(A), time(T)}.`
- Optional optimization (commented out by default)

### 5. Output Specification
- Sample measure values for testing
- Show statements for `#show holds_at/2.` and `#show happens/2.`

## Example Output

For a simple rule like "When OpenDoor and {isDaytime} then PlaySound":

```prolog
% Rule identifier
exp(r1).

% Antecedent logic
antecedent(r1,T):-
    time(T),
    happens(opendoor,T),
    holds_at(isDaytime,T).

% Consequent logic  
consequent(r1,T):-
    time(T),
    happens(playsound,T).

% Rule satisfaction
holds_nv(r1,T):-
    time(T),
    antecedent(r1,T),
    consequent(r1,T).

holds_v(r1,T):-
    time(T),
    not antecedent(r1,T),
    not consequent(r1,T).

% Hard constraint
:- exp(R), time(T), not holds(R,T).
```

## Differences from Original Converter

| Feature | Original Converter | Dalal Format Converter |
|---------|-------------------|------------------------|
| Rule Structure | Direct `happens()` rules | Antecedent/consequent separation |
| Rule Satisfaction | Basic event generation | Explicit satisfaction logic |
| Constraints | Soft optimization | Hard constraints |
| Event Types | Always `event()` | `action()` or `event()` based on context |
| Measures | Direct `holds()` | `holds_at()` predicates |

## Generated Files

When you run the batch converter, it creates `*_dalal.lp` files for each `.sleec` file found:

- `ASPEN.sleec` → `ASPEN_dalal.lp`
- `access_control.sleec` → `access_control_dalal.lp`
- `light_switch_rules.sleec` → `light_switch_rules_dalal.lp`
- etc.

## Testing

You can test the converter by running the built-in example:

```bash
cd sleec_converter
python correct_sleec_converter.py
```

This will convert a test SLEEC rule and display the output. 