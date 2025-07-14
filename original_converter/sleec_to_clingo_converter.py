#!/usr/bin/env python3
"""
SLEEC to Clingo Converter (Original)
===================================

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
        % SLEEC to Clingo Conversion (Original Format)
        % =============================================================================
        % 
        % This file was automatically generated from SLEEC rules.
        % Format: Direct rule translation following ASPEN.lp patterns
        % 
        % Generated Rules:
        """).strip() + '\n' + '\n'.join([f'% {rule.id}: {rule.condition} -> {rule.action}' for rule in self.rules]) + '\n'
    
    def _generate_time_domain(self) -> str:
        """Generate the time domain definition"""
        return textwrap.dedent(f"""
        % =============================================================================
        % TIME DOMAIN DEFINITION
        % =============================================================================
        time(0..{self.max_time}).
        """).strip()
    
    def _generate_event_definitions(self) -> str:
        """Generate event definitions"""
        if not self.events:
            return ""
        
        event_lines = []
        for event in self.events:
            event_lines.append(f"event({event.name.lower()}).")
        
        return textwrap.dedent("""
        % =============================================================================
        % EVENT DEFINITIONS
        % =============================================================================
        """).strip() + '\n' + '\n'.join(event_lines)
    
    def _generate_measure_definitions(self) -> str:
        """Generate measure definitions"""
        if not self.measures:
            return ""
        
        measure_lines = []
        for measure in self.measures:
            measure_lines.append(f"measure({measure.name.lower()}).")
        
        return textwrap.dedent("""
        % =============================================================================
        % MEASURE DEFINITIONS
        % =============================================================================
        """).strip() + '\n' + '\n'.join(measure_lines)
    
    def _generate_constants(self) -> str:
        """Generate constant definitions"""
        if not self.constants:
            return ""
        
        constant_lines = []
        for constant in self.constants:
            constant_lines.append(f"constant({constant.name.lower()}, {constant.value}).")
        
        return textwrap.dedent("""
        % =============================================================================
        % CONSTANT DEFINITIONS
        % =============================================================================
        """).strip() + '\n' + '\n'.join(constant_lines)
    
    def _generate_measure_instantiation(self) -> str:
        """Generate measure instantiation rules"""
        if not self.measures:
            return ""
        
        instantiation_rules = []
        
        for measure in self.measures:
            if measure.type == MeasureType.BOOLEAN:
                instantiation_rules.append(f"{{ holds({measure.name.lower()}, T) }} :- time(T).")
            elif measure.type == MeasureType.NUMERIC:
                instantiation_rules.append(f"{{ holds({measure.name.lower()}, V, T) : V = 0..10 }} :- time(T).")
            elif measure.type == MeasureType.SCALE and measure.scale_values:
                scale_options = " ; ".join([f"holds({measure.name.lower()}, {value.lower()}, T)" for value in measure.scale_values])
                instantiation_rules.append(f"1 {{ {scale_options} }} 1 :- time(T).")
        
        return textwrap.dedent("""
        % =============================================================================
        % MEASURE INSTANTIATION
        % =============================================================================
        """).strip() + '\n' + '\n'.join(instantiation_rules)
    
    def _generate_triggering_events(self) -> str:
        """Generate triggering event choice rules"""
        # Find events that appear in conditions but not in actions
        condition_events = set()
        action_events = set()
        
        for rule in self.rules:
            # Extract events from conditions (simple pattern matching)
            condition_lower = rule.condition.lower()
            for event in self.events:
                if event.name.lower() in condition_lower:
                    condition_events.add(event.name.lower())
            
            # Extract events from actions
            if rule.action:
                action_events.add(rule.action.lower())
            if rule.otherwise_action:
                action_events.add(rule.otherwise_action.lower())
        
        # Triggering events are those in conditions but not in actions
        triggering_events = condition_events - action_events
        
        if not triggering_events:
            return ""
        
        triggering_rules = []
        for event in triggering_events:
            triggering_rules.append(f"{{ happens({event}, T) }} :- time(T).")
        
        return textwrap.dedent("""
        % =============================================================================
        % TRIGGERING EVENT INSTANTIATION
        % =============================================================================
        """).strip() + '\n' + '\n'.join(triggering_rules)
    
    def _generate_rule_implementations(self) -> str:
        """Generate the actual rule implementations"""
        if not self.rules:
            return ""
        
        rule_implementations = []
        
        for rule in self.rules:
            condition_clingo = self._convert_condition_to_clingo(rule.condition)
            action_clingo = rule.action.lower()
            
            # Main rule
            rule_impl = f"happens({action_clingo}, T) :- {condition_clingo}, time(T)."
            rule_implementations.append(rule_impl)
            
            # Otherwise clause
            if rule.otherwise_action:
                negated_condition = self._negate_condition(rule.condition)
                otherwise_clingo = rule.otherwise_action.lower()
                otherwise_impl = f"happens({otherwise_clingo}, T) :- {negated_condition}, time(T)."
                rule_implementations.append(otherwise_impl)
        
        return textwrap.dedent("""
        % =============================================================================
        % RULE IMPLEMENTATIONS
        % =============================================================================
        """).strip() + '\n' + '\n'.join(rule_implementations)
    
    def _convert_condition_to_clingo(self, condition: str) -> str:
        """Convert a SLEEC condition to Clingo format"""
        # Convert to lowercase
        condition = condition.lower()
        
        # Replace measure references {measureName} with holds(measureName, T)
        condition = re.sub(r'\{(\w+)\}', r'holds(\1, T)', condition)
        
        # Replace measure comparisons {measureName} = value with holds(measureName, value, T)
        condition = re.sub(r'holds\((\w+), T\)\s*=\s*(\w+)', r'holds(\1, \2, T)', condition)
        
        # Replace logical operators
        condition = condition.replace(' and ', ', ')
        condition = condition.replace(' or ', '; ')
        condition = condition.replace(' not ', 'not ')
        
        # Replace event references with happens(eventName, T)
        for event in self.events:
            event_name = event.name.lower()
            # Use word boundaries to avoid partial matches
            condition = re.sub(rf'\b{event_name}\b', f'happens({event_name}, T)', condition)
        
        return condition
    
    def _negate_condition(self, condition: str) -> str:
        """Negate a condition for otherwise clauses"""
        # Simple negation - wrap in not()
        return f"not ({self._convert_condition_to_clingo(condition)})"
    
    def _generate_output_specification(self) -> str:
        """Generate output specification"""
        return textwrap.dedent("""
        % =============================================================================
        % OUTPUT SPECIFICATION
        % =============================================================================
        #show happens/2.
        #show holds/2.
        #show holds/3.
        """).strip() 