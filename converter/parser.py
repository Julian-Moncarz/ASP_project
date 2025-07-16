#!/usr/bin/env python3
"""
Shared SLEEC Parser
==================

This module provides common SLEEC parsing functionality used by both
the original and Dalal converters.

Classes:
    MeasureType: Enumeration of measure types (boolean, numeric, scale)
    Measure: Data class for measure definitions
    Event: Data class for event definitions  
    Constant: Data class for constant definitions
    Rule: Data class for rule definitions
    SleecParser: Parser for SLEEC files
"""

import re
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
class UnlessClause:
    condition: str
    action: str

@dataclass
class Rule:
    id: str
    condition: str
    action: str
    line_number: int
    otherwise_action: Optional[str] = None
    unless_clauses: Optional[List[UnlessClause]] = None

class SleecParser:
    """Shared SLEEC parser for extracting definitions and rules"""
    
    def __init__(self):
        self.events: List[Event] = []
        self.measures: List[Measure] = []
        self.constants: List[Constant] = []
        self.rules: List[Rule] = []
    
    def parse_file(self, filename: str) -> Tuple[List[Event], List[Measure], List[Constant], List[Rule]]:
        """Parse a SLEEC file and return all definitions and rules"""
        with open(filename, 'r') as f:
            content = f.read()
        return self.parse_sleec_string(content)
    
    def parse_sleec_string(self, content: str) -> Tuple[List[Event], List[Measure], List[Constant], List[Rule]]:
        """Parse SLEEC content string and return all definitions and rules"""
        self._reset()
        self._parse_sleec(content)
        return self.events, self.measures, self.constants, self.rules
    
    def _reset(self):
        """Reset internal state for new parsing"""
        self.events.clear()
        self.measures.clear()
        self.constants.clear()
        self.rules.clear()
    
    def _parse_sleec(self, content: str):
        """Parse SLEEC content and extract definitions and rules"""
        # Keep original content for line number tracking
        original_lines = content.split('\n')
        
        # Remove comments only (don't normalize whitespace yet)
        content_no_comments = re.sub(r'//.*$', '', content, flags=re.MULTILINE)
        
        # Extract definitions section
        def_match = re.search(r'def_start(.*?)def_end', content_no_comments, re.DOTALL)
        if def_match:
            def_section = def_match.group(1)
            def_section = re.sub(r'\s+$', '', def_section, flags=re.MULTILINE)  # Remove trailing whitespace
            self._parse_definitions(def_section, original_lines)
        
        # Extract rules section
        rule_match = re.search(r'rule_start(.*?)rule_end', content_no_comments, re.DOTALL)
        if rule_match:
            rule_section = rule_match.group(1)
            rule_section = re.sub(r'\s+$', '', rule_section, flags=re.MULTILINE)  # Remove trailing whitespace
            self._parse_rules(rule_section, original_lines)
    
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
                continue
            
            # If we get here, the line wasn't recognized
            line_num = self._find_line_number(line, original_lines)
            raise ValueError(f"❌ Syntax Error at line {line_num}: Unrecognized definition '{line}'\n\n"
                           f"Expected format:\n"
                           f"  event <name>\n"
                           f"  measure <name>: <type>\n"
                           f"  constant <name> = <value>\n\n"
                           f"Valid measure types: boolean, numeric, scale(value1, value2, ...)")
    
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
            # Parse unless clauses first (they take precedence over otherwise)
            unless_clauses = []
            remaining_action = action_part.strip()
            
            # Extract all unless clauses using regex
            unless_pattern = r'\s+unless\s+\(([^)]+)\)\s+then\s+(.*?)(?=\s+unless|$)'
            unless_matches = re.findall(unless_pattern, remaining_action)
            
            if unless_matches:
                # Extract primary action (everything before first unless)
                primary_action_match = re.match(r'(.*?)\s+unless', remaining_action)
                if primary_action_match:
                    action = primary_action_match.group(1).strip()
                else:
                    action = remaining_action.strip()
                
                # Process unless clauses
                for unless_condition, unless_action in unless_matches:
                    unless_clauses.append(UnlessClause(
                        condition=unless_condition.strip(),
                        action=unless_action.strip()
                    ))
                
                otherwise_action = None  # unless takes precedence over otherwise
                
            else:
                # Handle otherwise clause (only if no unless clauses)
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
            
            self.rules.append(Rule(
                rule_id, 
                condition.strip(), 
                action, 
                line_num, 
                otherwise_action,
                unless_clauses if unless_clauses else None
            ))

    @staticmethod
    def validate_definitions(events: List[Event], measures: List[Measure], rules: List[Rule]) -> None:
        """Validate that all referenced events and measures are defined"""
        errors = []
        
        # Get defined names
        defined_events = {event.name for event in events}
        defined_measures = {measure.name for measure in measures}
        
        for rule in rules:
            # Check events in actions (including unless actions)
            actions_to_check = [rule.action, rule.otherwise_action]
            
            # Add unless clause actions
            if rule.unless_clauses:
                for unless_clause in rule.unless_clauses:
                    actions_to_check.append(unless_clause.action)
            
            for action in actions_to_check:
                if action:
                    action_clean = action.strip()
                    if action_clean.startswith("not "):
                        action_clean = action_clean[4:].strip()
                    if action_clean not in defined_events:
                        errors.append(f"Error: Undefined event '{action_clean}' referenced in rule {rule.id} at line {rule.line_number}")
            
            # Check measures in conditions (including unless conditions)
            conditions_to_check = [rule.condition]
            
            # Add unless clause conditions
            if rule.unless_clauses:
                for unless_clause in rule.unless_clauses:
                    conditions_to_check.append(unless_clause.condition)
            
            for condition in conditions_to_check:
                measure_matches = re.findall(r'\{(\w+)\}', condition)
                for measure_name in measure_matches:
                    if measure_name not in defined_measures:
                        errors.append(f"Error: Undefined measure '{measure_name}' referenced in rule {rule.id} at line {rule.line_number}")
        
        if errors:
            error_msg = "❌ Validation failed:\n" + "\n".join(errors) + "\n\nPlease add these definitions to your SLEEC file:"
            
            # Suggest missing definitions
            missing_events = set()
            missing_measures = set()
            
            for rule in rules:
                # Check main actions and otherwise actions
                actions_to_check = [rule.action, rule.otherwise_action]
                
                # Add unless clause actions
                if rule.unless_clauses:
                    for unless_clause in rule.unless_clauses:
                        actions_to_check.append(unless_clause.action)
                
                for action in actions_to_check:
                    if action:
                        action_clean = action.strip()
                        if action_clean.startswith("not "):
                            action_clean = action_clean[4:].strip()
                        if action_clean not in defined_events:
                            missing_events.add(action_clean)
                
                # Check main condition and unless conditions
                conditions_to_check = [rule.condition]
                
                if rule.unless_clauses:
                    for unless_clause in rule.unless_clauses:
                        conditions_to_check.append(unless_clause.condition)
                
                for condition in conditions_to_check:
                    measure_matches = re.findall(r'\{(\w+)\}', condition)
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