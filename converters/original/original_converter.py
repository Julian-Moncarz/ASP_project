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

from ..parser import SleecParser, MeasureType, Measure, Event, Constant, Rule

class SleecToClingoConverter:
    """Converts SLEEC rules to Clingo format"""
    
    def __init__(self, max_time: int = 10):
        self.max_time = max_time
        self.events: List[Event] = []
        self.measures: List[Measure] = []
        self.constants: List[Constant] = []
        self.rules: List[Rule] = []
        self.parser = SleecParser()
        
    def convert_file(self, filename: str) -> str:
        """Convert a SLEEC file to Clingo format"""
        self.events, self.measures, self.constants, self.rules = self.parser.parse_file(filename)
        SleecParser.validate_definitions(self.events, self.measures, self.rules)
        return self._generate_clingo()
    
    def convert_sleec_string(self, content: str) -> str:
        """Convert SLEEC content string to Clingo format"""
        self.events, self.measures, self.constants, self.rules = self.parser.parse_sleec_string(content)
        SleecParser.validate_definitions(self.events, self.measures, self.rules)
        return self._generate_clingo()
    

    

    
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