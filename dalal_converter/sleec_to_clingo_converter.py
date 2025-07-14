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
import sys
import os
from typing import List, Dict, Tuple, Optional, Set

# Add parent directory to path to import shared parser
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
try:
    from parser import SleecParser, MeasureType, Measure, Event, Constant, Rule
except ImportError:
    # If import fails, try relative import
    import sys
    sys.path.append('..')
    from parser import SleecParser, MeasureType, Measure, Event, Constant, Rule

class CorrectSleecConverter:
    """Converts SLEEC rules to Clingo format using Dalal's approach"""
    
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
        
        # Generate triggering events instead of all events
        triggering_events = self._get_triggering_events()
        if triggering_events:
            triggering_rules = []
            for event in triggering_events:
                triggering_rules.append(f"{{ happens({event}, T) }} :- time(T).")
            sections.append("% Triggering event instantiation\n" + "\n".join(triggering_rules))
        
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
    
    def _get_triggering_events(self) -> Set[str]:
        """Get events that appear in conditions but not in actions (triggering events)"""
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
        return condition_events - action_events
    
    def _generate_output_specification(self) -> str:
        """Generate output specification"""
        sections = []
        
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