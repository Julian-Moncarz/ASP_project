#!/usr/bin/env python3
"""
SLEEC to Clingo Converter (Dalal's Format)
=========================================

This module converts SLEEC rules into Clingo format following Dalal's approach,
which uses antecedent/consequent structure and rule satisfaction logic.

Usage:
    converter = CorrectSleecConverter()
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
    line_number: int
    scale_values: Optional[List[str]] = None
    
@dataclass
class Event:
    name: str
    line_number: int

@dataclass
class Constant:
    name: str
    value: str
    line_number: int

@dataclass
class Rule:
    id: str
    condition: str
    action: str
    line_number: int
    otherwise_action: Optional[str] = None

class CorrectSleecConverter:
    """Converts SLEEC rules to Clingo format using Dalal's approach"""
    
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
        self._validate_definitions()
        return self._generate_clingo()
    
    def _reset(self):
        """Reset internal state for new conversion"""
        self.events.clear()
        self.measures.clear()
        self.constants.clear()
        self.rules.clear()
    
    def _parse_sleec(self, content: str):
        """Parse SLEEC content and extract definitions and rules"""
        # Keep original content for line number tracking
        original_lines = content.split('\n')
        
        # Remove comments and normalize whitespace for parsing
        content = re.sub(r'//.*$', '', content, flags=re.MULTILINE)
        content = re.sub(r'\s+', ' ', content).strip()
        
        # Extract definitions section
        def_match = re.search(r'def_start(.*?)def_end', content, re.DOTALL)
        if def_match:
            self._parse_definitions(def_match.group(1), original_lines)
        
        # Extract rules section
        rule_match = re.search(r'rule_start(.*?)rule_end', content, re.DOTALL)
        if rule_match:
            self._parse_rules(rule_match.group(1), original_lines)
    
    def _find_line_number(self, text: str, original_lines: List[str]) -> int:
        """Find the line number where text appears in original content"""
        text_clean = text.strip()
        for i, line in enumerate(original_lines, 1):
            if text_clean in line and line.strip():
                return i
        return 1  # Fallback to line 1 if not found
    
    def _parse_definitions(self, def_content: str, original_lines: List[str]):
        """Parse the definitions section"""
        lines = [line.strip() for line in def_content.split('\n') if line.strip()]
        
        for line in lines:
            # Parse events
            event_match = re.match(r'event\s+(\w+)', line)
            if event_match:
                line_num = self._find_line_number(line, original_lines)
                self.events.append(Event(event_match.group(1), line_num))
                continue
            
            # Parse measures
            measure_match = re.match(r'measure\s+(\w+):\s*(.+)', line)
            if measure_match:
                name, type_def = measure_match.groups()
                line_num = self._find_line_number(line, original_lines)
                self._parse_measure(name, type_def, line_num)
                continue
            
            # Parse constants
            constant_match = re.match(r'constant\s+(\w+)\s*=\s*(.+)', line)
            if constant_match:
                name, value = constant_match.groups()
                line_num = self._find_line_number(line, original_lines)
                self.constants.append(Constant(name, value.strip(), line_num))
    
    def _parse_measure(self, name: str, type_def: str, line_number: int):
        """Parse a measure definition"""
        type_def = type_def.strip()
        
        if type_def == "boolean":
            self.measures.append(Measure(name, MeasureType.BOOLEAN, line_number))
        elif type_def == "numeric":
            self.measures.append(Measure(name, MeasureType.NUMERIC, line_number))
        elif type_def.startswith("scale(") and type_def.endswith(")"):
            # Extract scale values
            scale_content = type_def[6:-1]  # Remove "scale(" and ")"
            values = [v.strip() for v in scale_content.split(',')]
            self.measures.append(Measure(name, MeasureType.SCALE, line_number, values))
        else:
            # Default to boolean if type unclear
            self.measures.append(Measure(name, MeasureType.BOOLEAN, line_number))
    
    def _parse_rules(self, rules_content: str, original_lines: List[str]):
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
            
            # Find line number for this rule
            rule_text = f"{rule_id} when {condition} then {action}"
            line_num = self._find_line_number(rule_text, original_lines)
            
            self.rules.append(Rule(rule_id, condition.strip(), action, line_num, otherwise_action))
    
    def _validate_definitions(self):
        """Validate that all referenced events and measures are defined"""
        errors = []
        
        # Get defined names
        defined_events = {event.name for event in self.events}
        defined_measures = {measure.name for measure in self.measures}
        
        for rule in self.rules:
            # Check events in actions
            for action in [rule.action, rule.otherwise_action]:
                if action:
                    action_clean = action.strip()
                    if action_clean.startswith("not "):
                        action_clean = action_clean[4:].strip()
                    if action_clean not in defined_events:
                        errors.append(f"Error: Undefined event '{action_clean}' referenced in rule {rule.id} at line {rule.line_number}")
            
            # Check measures in conditions
            measure_matches = re.findall(r'\{(\w+)\}', rule.condition)
            for measure_name in measure_matches:
                if measure_name not in defined_measures:
                    errors.append(f"Error: Undefined measure '{measure_name}' referenced in rule {rule.id} at line {rule.line_number}")
        
        if errors:
            error_msg = "❌ Validation failed:\n" + "\n".join(errors) + "\n\nPlease add these definitions to your SLEEC file:"
            
            # Suggest missing definitions
            missing_events = set()
            missing_measures = set()
            
            for rule in self.rules:
                for action in [rule.action, rule.otherwise_action]:
                    if action:
                        action_clean = action.strip()
                        if action_clean.startswith("not "):
                            action_clean = action_clean[4:].strip()
                        if action_clean not in defined_events:
                            missing_events.add(action_clean)
                
                measure_matches = re.findall(r'\{(\w+)\}', rule.condition)
                for measure_name in measure_matches:
                    if measure_name not in defined_measures:
                        missing_measures.add(measure_name)
            
            if missing_events:
                error_msg += "\n\nEvents:"
                for event in sorted(missing_events):
                    error_msg += f"\nevent {event}"
            
            if missing_measures:
                error_msg += "\n\nMeasures:"
                for measure in sorted(missing_measures):
                    error_msg += f"\nmeasure {measure}: boolean"
            
            raise ValueError(error_msg)
    
    def _generate_clingo(self) -> str:
        """Generate the complete Clingo program"""
        sections = [
            self._generate_header(),
            self._generate_domain_definitions(),
            self._generate_sleec_rule_definitions(),
            self._generate_rule_satisfaction_logic(),
            self._generate_action_generation_and_constraints(),
            self._generate_output_specification()
        ]
        
        return '\n\n'.join(filter(None, sections))
    
    def _generate_header(self) -> str:
        """Generate the file header"""
        rule_desc = ""
        for rule in self.rules:
            rule_desc += f"% {rule.id}: {rule.condition} -> {rule.action}\n"
            if rule.otherwise_action:
                rule_desc += f"%   otherwise -> {rule.otherwise_action}\n"
        
        return textwrap.dedent(f"""
        % =============================================================================
        % SLEEC to Clingo Conversion (Dalal's Format)
        % =============================================================================
        % 
        % This file was automatically generated from SLEEC rules.
        % Format: Antecedent/consequent structure with rule satisfaction logic
        % 
        % Generated Rules:
        {rule_desc}
        """).strip()
    
    def _generate_domain_definitions(self) -> str:
        """Generate domain definitions (events, measures, time)"""
        sections = []
        
        # Time domain
        sections.append(f"time(0..{self.max_time}).")
        
        # Events - use event() when measures are present, action() for simple cases
        if self.measures:
            event_lines = [f"event({event.name.lower()})." for event in self.events]
            sections.append("% Events\n" + "\n".join(event_lines))
        else:
            action_lines = [f"action({event.name.lower()})." for event in self.events]
            sections.append("% Actions\n" + "\n".join(action_lines))
        
        # Measures
        if self.measures:
            measure_lines = [f"measure({measure.name.lower()})." for measure in self.measures]
            sections.append("% Measures\n" + "\n".join(measure_lines))
        
        return textwrap.dedent("""
        % =============================================================================
        % DOMAIN DEFINITIONS
        % =============================================================================
        """).strip() + "\n\n" + "\n\n".join(sections)
    
    def _generate_sleec_rule_definitions(self) -> str:
        """Generate SLEEC rule definitions with antecedent/consequent structure"""
        if not self.rules:
            return ""
        
        rule_definitions = []
        
        for rule in self.rules:
            rule_id = rule.id.lower()
            
            # Rule identifier
            rule_definitions.append(f"exp({rule_id}).")
            
            # Antecedent logic
            antecedent_condition = self._convert_condition_to_antecedent(rule.condition)
            rule_definitions.append(f"antecedent({rule_id}, T) :- {antecedent_condition}.")
            
            # Consequent logic
            if self.measures:
                consequent_action = f"happens({rule.action.lower()}, T)"
            else:
                consequent_action = f"happens({rule.action.lower()}, T)"
            rule_definitions.append(f"consequent({rule_id}, T) :- time(T), {consequent_action}.")
            
            # Otherwise clause if present
            if rule.otherwise_action:
                otherwise_id = f"{rule_id}_otherwise"
                rule_definitions.append(f"exp({otherwise_id}).")
                
                # Negated antecedent
                negated_antecedent = self._negate_antecedent(rule.condition)
                rule_definitions.append(f"antecedent({otherwise_id}, T) :- {negated_antecedent}.")
                
                # Otherwise consequent
                if self.measures:
                    otherwise_consequent = f"happens({rule.otherwise_action.lower()}, T)"
                else:
                    otherwise_consequent = f"happens({rule.otherwise_action.lower()}, T)"
                rule_definitions.append(f"consequent({otherwise_id}, T) :- time(T), {otherwise_consequent}.")
        
        return textwrap.dedent("""
        % =============================================================================
        % SLEEC RULE DEFINITIONS
        % =============================================================================
        """).strip() + "\n\n" + "\n\n".join(rule_definitions)
    
    def _convert_condition_to_antecedent(self, condition: str) -> str:
        """Convert a SLEEC condition to antecedent format"""
        # Convert to lowercase
        condition = condition.lower()
        
        # Replace measure references {measureName} with holds_at(measureName, T)
        condition = re.sub(r'\{(\w+)\}', r'holds_at(\1, T)', condition)
        
        # Replace measure comparisons {measureName} = value with holds_at(measureName, value, T)
        condition = re.sub(r'holds_at\((\w+), T\)\s*=\s*(\w+)', r'holds_at(\1, \2, T)', condition)
        
        # Replace logical operators
        condition = condition.replace(' and ', ', ')
        condition = condition.replace(' or ', '; ')
        condition = condition.replace(' not ', 'not ')
        
        # Replace event references with happens(eventName, T)
        for event in self.events:
            event_name = event.name.lower()
            # Use word boundaries to avoid partial matches
            condition = re.sub(rf'\b{event_name}\b', f'happens({event_name}, T)', condition)
        
        # Add time constraint
        condition += ", time(T)"
        
        return condition
    
    def _negate_antecedent(self, condition: str) -> str:
        """Negate an antecedent condition for otherwise clauses"""
        # Simple negation - wrap in not()
        return f"not ({self._convert_condition_to_antecedent(condition)})"
    
    def _to_lower_camel_case(self, name: str) -> str:
        """Convert to lower camel case for consistency"""
        return name[0].lower() + name[1:] if name else name
    
    def _remove_logical_grouping_parentheses(self, condition: str) -> str:
        """Remove unnecessary logical grouping parentheses"""
        # This is a simplified version - in practice you might want more sophisticated parsing
        return condition.replace('(', '').replace(')', '')
    
    def _generate_rule_satisfaction_logic(self) -> str:
        """Generate rule satisfaction logic with holds_nv and holds_v"""
        if not self.rules:
            return ""
        
        satisfaction_logic = []
        
        # General holds logic
        satisfaction_logic.append(textwrap.dedent("""
        % General holds logic
        holds(G, T):-
            time(T), 
            exp(G),
            holds_nv(G, T).

        holds(G, T):-
            time(T), 
            exp(G),
            holds_v(G, T).
        """).strip())
        
        # Specific holds logic for each rule
        for rule in self.rules:
            rule_id = rule.id.lower()
            
            # Non-vacuous satisfaction: antecedent true AND consequent met
            satisfaction_logic.append(f"""
% Non-vacuous satisfaction for {rule_id}
holds_nv({rule_id}, T):-
    time(T),
    antecedent({rule_id}, T),
    consequent({rule_id}, T).""")
            
            # Vacuous satisfaction: antecedent not true AND consequent does not happen
            satisfaction_logic.append(f"""
% Vacuous satisfaction for {rule_id}
holds_v({rule_id}, T):-
    time(T),
    not antecedent({rule_id}, T),
    not consequent({rule_id}, T).""")
            
            # Handle otherwise clause if present
            if rule.otherwise_action:
                otherwise_id = f"{rule_id}_otherwise"
                satisfaction_logic.append(f"""
% Non-vacuous satisfaction for {otherwise_id}
holds_nv({otherwise_id}, T):-
    time(T),
    antecedent({otherwise_id}, T),
    consequent({otherwise_id}, T).""")
                
                satisfaction_logic.append(f"""
% Vacuous satisfaction for {otherwise_id}
holds_v({otherwise_id}, T):-
    time(T),
    not antecedent({otherwise_id}, T),
    not consequent({otherwise_id}, T).""")
        
        # Hard constraint: every rule must be satisfied at every time point
        satisfaction_logic.append("""
% Hard constraint: every rule must be satisfied at every time point
:- exp(R), time(T), not holds(R,T).""")
        
        return textwrap.dedent("""
        % =============================================================================
        % RULE SATISFACTION LOGIC
        % =============================================================================
        """).strip() + "\n\n" + "\n\n".join(satisfaction_logic)
    
    def _generate_action_generation_and_constraints(self) -> str:
        """Generate action generation and constraints"""
        sections = []
        
        # Generate 0 or more events: ASP chooses which events to perform when
        if self.measures:
            sections.append("0{happens(A,T):event(A), time(T)}.")
        else:
            sections.append("0{happens(A,T):action(A), time(T)}.")
        
        # Add measure instantiation if measures exist
        if self.measures:
            measure_rules = []
            for measure in self.measures:
                if measure.type == MeasureType.BOOLEAN:
                    measure_rules.append(f"{{ holds_at({measure.name.lower()}, T) }} :- time(T).")
                elif measure.type == MeasureType.NUMERIC:
                    measure_rules.append(f"{{ holds_at({measure.name.lower()}, V, T) : V = 0..10 }} :- time(T).")
                elif measure.type == MeasureType.SCALE and measure.scale_values:
                    scale_options = " ; ".join([f"holds_at({measure.name.lower()}, {value.lower()}, T)" for value in measure.scale_values])
                    measure_rules.append(f"1 {{ {scale_options} }} 1 :- time(T).")
            
            sections.append("% Measure instantiation\n" + "\n".join(measure_rules))
        
        return textwrap.dedent("""
        % =============================================================================
        % ACTION GENERATION AND CONSTRAINTS
        % =============================================================================
        """).strip() + "\n\n" + "\n\n".join(sections)
    
    def _generate_output_specification(self) -> str:
        """Generate output specification"""
        sections = []
        
        # Sample measure values for testing
        if self.measures:
            sample_measures = []
            for measure in self.measures:
                if measure.type == MeasureType.BOOLEAN:
                    sample_measures.append(f"holds_at({measure.name.lower()}, 0).")
                    sample_measures.append(f"holds_at({measure.name.lower()}, 1).")
                elif measure.type == MeasureType.SCALE and measure.scale_values:
                    sample_measures.append(f"holds_at({measure.name.lower()}, {measure.scale_values[0].lower()}, 0).")
                    sample_measures.append(f"holds_at({measure.name.lower()}, {measure.scale_values[0].lower()}, 1).")
            
            if sample_measures:
                sections.append("% Sample measure values for testing\n" + "\n".join(sample_measures))
        
        # Show statements
        sections.append("#show holds_at/2.")
        sections.append("#show happens/2.")
        
        return textwrap.dedent("""
        % =============================================================================
        % OUTPUT SPECIFICATION
        % =============================================================================
        """).strip() + "\n\n" + "\n\n".join(sections)
    
    def _generate_measure_comparisons(self) -> str:
        """Generate measure comparison logic for scale measures"""
        if not self.measures:
            return ""
        
        comparison_rules = []
        
        for measure in self.measures:
            if measure.type == MeasureType.SCALE and measure.scale_values:
                # Generate comparison predicates for scale measures
                for i, value in enumerate(measure.scale_values):
                    comparison_rules.append(f"measure_equals({measure.name.lower()}, {value.lower()}, T) :- holds_at({measure.name.lower()}, {value.lower()}, T).")
                    comparison_rules.append(f"measure_greater_than({measure.name.lower()}, {value.lower()}, T) :- holds_at({measure.name.lower()}, V, T), V > {i}.")
                    comparison_rules.append(f"measure_less_than({measure.name.lower()}, {value.lower()}, T) :- holds_at({measure.name.lower()}, V, T), V < {i}.")
        
        if comparison_rules:
            return textwrap.dedent("""
            % =============================================================================
            % MEASURE COMPARISONS
            % =============================================================================
            """).strip() + "\n\n" + "\n\n".join(comparison_rules)
        
        return "" 