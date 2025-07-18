# SLEEC to Clingo Converter

Input sleec file, output runnable clingo code!

## Usage

```bash
python3 convert.py <sleec_file>
```

eg:

```bash
python3 convert.py ../sleec_files/simple_rules/lightswitch.sleec
```

### Use the Converter Directly

```python
from converter.sleec_converter import SleecToClingoConverter
from converter.config import ConverterConfig

# Use default configuration
converter = SleecToClingoConverter()
clingo_code = converter.convert_file("example.sleec")
print(clingo_code)

# Or use custom configuration
config = ConverterConfig(max_time=10, numeric_max=20)
converter = SleecToClingoConverter(config)
clingo_code = converter.convert_file("example.sleec")
print(clingo_code)
```

## Output Format

The converter generates Clingo code with this structure:

1. **Header** - File description and rule list
2. **Domain Definitions** - Time, events, measures, and actions
3. **SLEEC Rule Definitions** - Antecedent/consequent structure for each rule
4. **Rule Satisfaction Logic** - holds_nv (non-vacuous) and holds_v (vacuous) satisfaction
5. **Action Generation and Constraints** - Choice rules and measure instantiation
6. **Output Specification** - What to show in answer sets

## Example

**Input (lightswitch.sleec):**

```sleec
def_start
    // Events
    event ButtonPress
    event LightOn
    event SetBrightnessToMax

    // Measures
    measure isNight: boolean
def_end

rule_start
    // When the button is pressed, turn the light on
    R1 when ButtonPress then LightOn
  
    // If the light is on and it is night, set the brightness to the maximum
    R2 when LightOn and {isNight} then SetBrightnessToMax
rule_end 
```

**Generated Clingo output:**

```prolog
% =============================================================================
        % SLEEC to Clingo Conversion (Dalal's Format)
        % =============================================================================
        % 
        % This file was automatically generated from SLEEC rules.
        % Format: Antecedent/consequent structure with rule satisfaction logic
        % 
        % Generated Rules:
        % R1: ButtonPress -> LightOn
% R2: LightOn and {isNight} -> SetBrightnessToMax

% =============================================================================
% DOMAIN DEFINITIONS
% =============================================================================

time(0..10).

% Events
event(buttonpress).
event(lighton).
event(setbrightnesstomax).

% Measures
measure(isnight).

% =============================================================================
% SLEEC RULE DEFINITIONS
% =============================================================================

exp(r1).

antecedent(r1, T) :- happens(buttonpress, T), time(T).

consequent(r1, T) :- time(T), happens(lighton, T).

exp(r2).

antecedent(r2, T) :- happens(lighton, T), holds_at(isnight, T), time(T).

consequent(r2, T) :- time(T), happens(setbrightnesstomax, T).

% =============================================================================
% RULE SATISFACTION LOGIC
% =============================================================================

% General holds logic
holds(G, T):-
    time(T), 
    exp(G),
    holds_nv(G, T).

holds(G, T):-
    time(T), 
    exp(G),
    holds_v(G, T).


% Non-vacuous satisfaction for r1
holds_nv(r1, T):-
    time(T),
    antecedent(r1, T),
    consequent(r1, T).


% Vacuous satisfaction for r1
holds_v(r1, T):-
    time(T),
    not antecedent(r1, T),
    not consequent(r1, T).


% Non-vacuous satisfaction for r2
holds_nv(r2, T):-
    time(T),
    antecedent(r2, T),
    consequent(r2, T).


% Vacuous satisfaction for r2
holds_v(r2, T):-
    time(T),
    not antecedent(r2, T),
    not consequent(r2, T).


% Hard constraint: every rule must be satisfied at every time point
:- exp(R), time(T), not holds(R,T).

% =============================================================================
% ACTION GENERATION AND CONSTRAINTS
% =============================================================================

% Triggering event instantiation
{ happens(buttonpress, T) } :- time(T).

% Action event instantiation
{ happens(setbrightnesstomax, T) } :- time(T).
{ happens(lighton, T) } :- time(T).

% Measure instantiation
{ holds_at(isnight, T) } :- time(T).

% =============================================================================
% OUTPUT SPECIFICATION
% =============================================================================

#show holds_at/2.

#show happens/2.
```
