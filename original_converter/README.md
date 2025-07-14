# Original SLEEC to Clingo Converter

* Input sleec file
* Output: kinda hacked clingo

## Usage

```bash
python3 convert_single.py <sleec_file>
```

eg:

```bash
python3 convert_single.py ../sleec_files/simple_rules/lightswitch.sleec
```

### Use the Converter Directly

```python
from sleec_to_clingo_converter import SleecToClingoConverter

converter = SleecToClingoConverter(max_time=10)
clingo_code = converter.convert_file("example.sleec")
print(clingo_code)
```

## Output Format

The converter generates Clingo code with this structure:

1. **Header** - File description and rule list
2. **Time Domain** - `time(0..10)` (configurable)
3. **Event Definitions** - All events from definitions and rules
4. **Measure Definitions** - All measures from definitions and rules
5. **Measure Instantiation** - Choice rules for boolean/numeric, constraints for scales
6. **Triggering Events** - Choice rules for events that appear in `when` clauses
7. **Rule Implementations** - SLEEC rules converted to ASP logic
8. **Output Specification** - What to show in answer sets

## Example

**Input (lightswitch.sleec):**

```sleec
def_start
    event ButtonPress
    event LightOn
    measure isNight: boolean
def_end

rule_start
    R1 when ButtonPress then LightOn
    R2 when LightOn and {isNight} then SetBrightnessToMax
rule_end
```

**Generated Clingo output:**

```prolog
% =============================================================================
% SLEEC to Clingo Conversion (Original Format)
% =============================================================================

time(0..10).

% Event definitions
event(buttonpress).
event(lighton).
event(setbrightnesstomax).

% Measure definitions
measure(isnight).

% Measure instantiation
{ holds(isnight, T) } :- time(T).

% Triggering events
{ happens(buttonpress, T) } :- time(T).

% Rule implementations
happens(lighton, T) :- happens(buttonpress, T), time(T).
happens(setbrightnesstomax, T) :- happens(lighton, T), holds(isnight, T), time(T).

% Output specification
#show happens/2.
#show holds/2.
#show holds/3.
```
