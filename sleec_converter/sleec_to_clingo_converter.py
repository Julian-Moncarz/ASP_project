#!/usr/bin/env python3
"""
SLEEC to Clingo Converter
========================

This module converts simple SLEEC rules into Clingo (Answer Set Programming) format,
following the pattern established in ASPEN.lp.

Usage:
    converter = SleecToClingoConverter()
    clingo_code = converter.convert_file("example.sleec")
    
    # Or convert from string
    clingo_code = converter.convert_sleec_string(sleec_content)
"""

import re
import textwrap
from typing import List, Dict, Tuple, Optional, Set
from dataclasses import dataclass
from enum import Enum

class MeasureType(Enum):
    BOOLEAN = "boolean"
    NUMERIC = "numeric"
    SCALE = "scale"

@dataclass
class Measure:
    name: str
    type: MeasureType
    scale_values: Optional[List[str]] = None
    
@dataclass
class Event:
    name: str

@dataclass
class Constant:
    name: str
    value: str

@dataclass
class Rule:
    id: str
    condition: str
    action: str
    otherwise_action: Optional[str] = None

class SleecToClingoConverter:
    """Converts SLEEC rules to Clingo format"""
    
    def __init__(self, max_time: int = 10):
        self.max_time = max_time
        self.events: List[Event] = []
        self.measures: List[Measure] = []
        self.constants: List[Constant] = []
        self.rules: List[Rule] = []
        
    def convert_file(self, filename: str) -> str:
        """Convert a SLEEC file to Clingo format"""
        with open(filename, 'r') as f:
            content = f.read()
        return self.convert_sleec_string(content)
    
    def convert_sleec_string(self, content: str) -> str:
        """Convert SLEEC content string to Clingo format"""
        self._reset()
        self._parse_sleec(content)
        return self._generate_clingo()
    
    def _reset(self):
        """Reset internal state for new conversion"""
        self.events.clear()
        self.measures.clear()
        self.constants.clear()
        self.rules.clear()
    
    def _parse_sleec(self, content: str):
        """Parse SLEEC content and extract definitions and rules"""
        # Remove comments and normalize whitespace
        content = re.sub(r'//.*$', '', content, flags=re.MULTILINE)
        content = re.sub(r'\s+', ' ', content).strip()
        
        # Extract definitions section
        def_match = re.search(r'def_start(.*?)def_end', content, re.DOTALL)
        if def_match:
            self._parse_definitions(def_match.group(1))
        
        # Extract rules section
        rule_match = re.search(r'rule_start(.*?)rule_end', content, re.DOTALL)
        if rule_match:
            self._parse_rules(rule_match.group(1))
    
    def _parse_definitions(self, def_content: str):
        """Parse the definitions section"""
        lines = [line.strip() for line in def_content.split('\n') if line.strip()]
        
        for line in lines:
            # Parse events
            event_match = re.match(r'event\s+(\w+)', line)
            if event_match:
                self.events.append(Event(event_match.group(1)))
                continue
            
            # Parse measures
            measure_match = re.match(r'measure\s+(\w+):\s*(.+)', line)
            if measure_match:
                name, type_def = measure_match.groups()
                self._parse_measure(name, type_def)
                continue
            
            # Parse constants
            constant_match = re.match(r'constant\s+(\w+)\s*=\s*(.+)', line)
            if constant_match:
                name, value = constant_match.groups()
                self.constants.append(Constant(name, value.strip()))
    
    def _parse_measure(self, name: str, type_def: str):
        """Parse a measure definition"""
        type_def = type_def.strip()
        
        if type_def == "boolean":
            self.measures.append(Measure(name, MeasureType.BOOLEAN))
        elif type_def == "numeric":
            self.measures.append(Measure(name, MeasureType.NUMERIC))
        elif type_def.startswith("scale(") and type_def.endswith(")"):
            # Extract scale values
            scale_content = type_def[6:-1]  # Remove "scale(" and ")"
            values = [v.strip() for v in scale_content.split(',')]
            self.measures.append(Measure(name, MeasureType.SCALE, values))
        else:
            # Default to boolean if type unclear
            self.measures.append(Measure(name, MeasureType.BOOLEAN))
    
    def _parse_rules(self, rules_content: str):
        """Parse the rules section"""
        # Split by rule boundaries (R1, R2, etc.)
        rule_pattern = r'(R\d+)\s+when\s+(.*?)then\s+(.*?)(?=R\d+|$)'
        matches = re.findall(rule_pattern, rules_content, re.DOTALL)
        
        for rule_id, condition, action_part in matches:
            # Handle otherwise clause
            otherwise_match = re.search(r'(.*?)\s+otherwise\s+(.*)', action_part, re.DOTALL)
            if otherwise_match:
                action = otherwise_match.group(1).strip()
                otherwise_action = otherwise_match.group(2).strip()
            else:
                action = action_part.strip()
                otherwise_action = None
            
            self.rules.append(Rule(rule_id, condition.strip(), action, otherwise_action))
    
    def _extract_implicit_definitions(self):
        """Extract events and measures mentioned in rules but not explicitly defined"""
        existing_events = {event.name for event in self.events}
        existing_measures = {measure.name for measure in self.measures}
        
        for rule in self.rules:
            # Extract events from actions
            for action in [rule.action, rule.otherwise_action]:
                if action:
                    action_clean = action.strip()
                    if action_clean.startswith("not "):
                        action_clean = action_clean[4:].strip()
                    if action_clean not in existing_events:
                        self.events.append(Event(action_clean))
                        existing_events.add(action_clean)
            
            # Extract measures from conditions
            measure_matches = re.findall(r'\{(\w+)\}', rule.condition)
            for measure_name in measure_matches:
                if measure_name not in existing_measures:
                    # Default to boolean type for implicit measures
                    self.measures.append(Measure(measure_name, MeasureType.BOOLEAN))
                    existing_measures.add(measure_name)
    
    def _generate_clingo(self) -> str:
        """Generate the complete Clingo program"""
        # Extract additional events and measures from rules
        self._extract_implicit_definitions()
        
        sections = [
            self._generate_header(),
            self._generate_time_domain(),
            self._generate_event_definitions(),
            self._generate_measure_definitions(),
            self._generate_constants() if self.constants else "",
            self._generate_measure_instantiation(),
            self._generate_triggering_events(),
            self._generate_rule_implementations(),
            self._generate_output_specification()
        ]
        
        return '\n\n'.join(filter(None, sections))
    
    def _generate_header(self) -> str:
        """Generate the file header"""
        return textwrap.dedent("""
        % =============================================================================
        % SLEEC to Clingo Conversion
        % =============================================================================
        % 
        % This file was automatically generated from SLEEC rules using the
        % SLEEC to Clingo converter.
        %
        % Generated rules implement the logic using Answer Set Programming (ASP)
        % with Clingo syntax.
        % =============================================================================
        """).strip()
    
    def _generate_time_domain(self) -> str:
        """Generate time domain definition"""
        return textwrap.dedent(f"""
        % =============================================================================
        % TIME DOMAIN DEFINITION
        % =============================================================================
        % Define the time steps for the simulation
        time(0..{self.max_time}).
        """).strip()
    
    def _generate_event_definitions(self) -> str:
        """Generate event definitions"""
        if not self.events:
            return ""
        
        header = textwrap.dedent("""
        % =============================================================================
        % EVENT DEFINITIONS
        % =============================================================================
        % Define all possible events that can occur in the system
        """).strip()
        
        events = '\n'.join(f"event({event.name.lower()})." for event in self.events)
        return f"{header}\n{events}"
    
    def _generate_measure_definitions(self) -> str:
        """Generate measure definitions"""
        if not self.measures:
            return ""
        
        header = textwrap.dedent("""
        % =============================================================================
        % MEASURE DEFINITIONS
        % =============================================================================
        % Define all measures that can be evaluated
        """).strip()
        
        measures = '\n'.join(f"measure({measure.name.lower()})." for measure in self.measures)
        return f"{header}\n{measures}"
    
    def _generate_constants(self) -> str:
        """Generate constant definitions"""
        header = textwrap.dedent("""
        % =============================================================================
        % CONSTANT DEFINITIONS
        % =============================================================================
        % Define system constants
        """).strip()
        
        constants = '\n'.join(f"#const {const.name} = {const.value}." for const in self.constants)
        return f"{header}\n{constants}"
    
    def _generate_measure_instantiation(self) -> str:
        """Generate measure instantiation rules"""
        if not self.measures:
            return ""
        
        header = textwrap.dedent("""
        % =============================================================================
        % MEASURE INSTANTIATION
        % =============================================================================
        % Boolean measures: at each timestep, each measure can be true or false
        % Scale measures: must have exactly one value at each time
        """).strip()
        
        instantiations = []
        
        for measure in self.measures:
            if measure.type in [MeasureType.BOOLEAN, MeasureType.NUMERIC]:
                instantiations.append(f"{{ holds({measure.name.lower()}, T) }} :- time(T).")
            elif measure.type == MeasureType.SCALE and measure.scale_values:
                values_str = ' ; '.join(f"holds({measure.name.lower()}, {val}, T)" for val in measure.scale_values)
                instantiations.append(f"1 {{ {values_str} }} 1 :- time(T).")
        
        return f"{header}\n" + '\n'.join(instantiations)
    
    def _generate_triggering_events(self) -> str:
        """Generate triggering event instantiation"""
        # Identify which events are triggering events (appear in 'when' clauses)
        triggering_events = set()
        for rule in self.rules:
            # Simple heuristic: extract event names from conditions
            for event in self.events:
                if event.name in rule.condition:
                    triggering_events.add(event.name)
        
        if not triggering_events:
            return ""
        
        header = textwrap.dedent("""
        % =============================================================================
        % TRIGGERING EVENT INSTANTIATION
        % =============================================================================
        % These events can occur independently at each timestep
        % The solver will choose when these triggering events happen
        """).strip()
        
        instantiations = '\n'.join(f"{{ happens({event.lower()}, T) }} :- time(T)." 
                                 for event in sorted(triggering_events))
        return f"{header}\n{instantiations}"
    
    def _generate_rule_implementations(self) -> str:
        """Generate rule implementations"""
        if not self.rules:
            return ""
        
        header = textwrap.dedent("""
        % =============================================================================
        % RULE IMPLEMENTATIONS
        % =============================================================================
        """).strip()
        
        implementations = []
        for rule in self.rules:
            implementations.append(f"% {rule.id}: {rule.condition} -> {rule.action}")
            
            # Convert condition to Clingo format
            clingo_condition = self._convert_condition_to_clingo(rule.condition)
            
            # Handle negative actions (not X)
            if rule.action.strip().startswith("not "):
                action_name = rule.action.strip()[4:].strip()
                implementations.append(f"nothappens({action_name.lower()}, T) :- {clingo_condition}, time(T).")
            else:
                implementations.append(f"happens({rule.action.strip().lower()}, T) :- {clingo_condition}, time(T).")
            
            # Handle otherwise clause
            if rule.otherwise_action:
                # Create negated condition for otherwise
                negated_condition = self._negate_condition(rule.condition)
                clingo_neg_condition = self._convert_condition_to_clingo(negated_condition)
                
                if rule.otherwise_action.strip().startswith("not "):
                    otherwise_action_name = rule.otherwise_action.strip()[4:].strip()
                    implementations.append(f"nothappens({otherwise_action_name.lower()}, T) :- {clingo_neg_condition}, time(T).")
                else:
                    implementations.append(f"happens({rule.otherwise_action.strip().lower()}, T) :- {clingo_neg_condition}, time(T).")
            
            implementations.append("")  # Add blank line between rules
        
        return f"{header}\n" + '\n'.join(implementations)
    
    def _convert_condition_to_clingo(self, condition: str) -> str:
        """Convert a SLEEC condition to Clingo format"""
        # First, convert measure references {measure} to holds(measure, T)
        # Handle comparisons like {measure} = value
        condition = re.sub(r'\{(\w+)\}\s*=\s*(\w+)', lambda m: f'holds({m.group(1).lower()}, {m.group(2)}, T)', condition)
        condition = re.sub(r'\{(\w+)\}\s*<\s*(\w+)', lambda m: f'holds({m.group(1).lower()}, V, T), measure_less_than({m.group(1).lower()}, V, {m.group(2)})', condition)
        condition = re.sub(r'\{(\w+)\}\s*>\s*(\w+)', lambda m: f'holds({m.group(1).lower()}, V, T), measure_greater_than({m.group(1).lower()}, V, {m.group(2)})', condition)
        
        # Convert simple boolean measures {measure} to holds(measure, T)
        condition = re.sub(r'\{(\w+)\}', lambda m: f'holds({m.group(1).lower()}, T)', condition)
        
        # Convert event references to happens(event, T)
        for event in self.events:
            condition = re.sub(rf'\b{event.name}\b', f'happens({event.name.lower()}, T)', condition)
        
        # Remove unnecessary parentheses that cause syntax errors in Clingo
        # Only remove parentheses that are used for logical grouping, not function arguments
        # Pattern: ( ... and ... ) or ( ... or ... ) -> ... and ... / ... or ...
        condition = re.sub(r'\(([^()]*(?:\band\b|\bor\b)[^()]*)\)', r'\1', condition)
        
        # Now replace logical operators (after event/measure conversion)
        condition = condition.replace(' and ', ', ')
        condition = condition.replace(' or ', ' ; ')
        
        # Remove specific logical grouping parentheses that still remain
        # This pattern matches outer parentheses around multiple holds() calls
        condition = re.sub(r'\((\s*holds\([^)]+\),\s*holds\([^)]+\)\s*)\)', r'\1', condition)
        
        # Handle negation
        condition = re.sub(r'not\s+happens\((\w+),\s*T\)', r'not happens(\1, T)', condition)
        condition = re.sub(r'not\s+holds\((\w+),\s*T\)', r'not holds(\1, T)', condition)
        condition = re.sub(r'not\s+holds\((\w+),\s*(\w+),\s*T\)', r'not holds(\1, \2, T)', condition)
        
        return condition
    
    def _negate_condition(self, condition: str) -> str:
        """Create a negated version of a condition for otherwise clauses"""
        # This is a simplified negation - in practice, you might want more sophisticated logic
        return f"not ({condition})"
    
    def _generate_output_specification(self) -> str:
        """Generate output specification"""
        return textwrap.dedent("""
        % =============================================================================
        % CONTRADICTION DETECTION
        % =============================================================================
        % Detect when an event both happens and doesn't happen (contradiction)
        contradiction(E, T) :- happens(E, T), nothappens(E, T), event(E), time(T).

        % =============================================================================
        % OUTPUT SPECIFICATION
        % =============================================================================
        % Specify what information to show in the answer sets
        #show happens/2.          % Show all events that happen
        #show holds/2.            % Show boolean measures
        #show holds/3.            % Show scale/numeric measures
        #show contradiction/2.    % Show contradictions if any
        """).strip()

# Example usage and testing
if __name__ == "__main__":
    # Test with a simple SLEEC rule
    test_sleec = """
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
    """
    
    converter = SleecToClingoConverter()
    result = converter.convert_sleec_string(test_sleec)
    print(result) 