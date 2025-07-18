#!/usr/bin/env python3
"""
SLEEC to Clingo Converter (Dalal's Format)
=========================================

This module converts SLEEC rules into Clingo format following Dalal's approach,
which uses antecedent/consequent structure and rule satisfaction logic.

Usage:
    converter = SleecToClingoConverter()
    clingo_code = converter.convert_file("example.sleec")
    
    # Or convert from string
    clingo_code = converter.convert_sleec_string(sleec_content)
"""

import re
import textwrap
from typing import List, Dict, Tuple, Optional, Set

from converter.parser import SleecParser, MeasureType, Measure, Event, Constant, Rule
from converter.config import ConverterConfig, DEFAULT_CONFIG

class SleecToClingoConverter:
    """Converts SLEEC rules to Clingo format using an antecedent/consequent approach"""
    
    def __init__(self, config: Optional[ConverterConfig] = None):
        """Initialize converter with configuration
        
        Args:
            config: Configuration object. If None, uses default configuration.
        """
        if config is None:
            config = ConverterConfig.create_default()
        
        config.validate()
        self.config = config
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
        sections.append(self.config.time_domain)
        
        # Events - always use event() predicates
        event_lines = [f"event({event.name.lower()})." for event in self.events]
        sections.append("% Events\n" + "\n".join(event_lines))
        
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
            
            if rule.unless_clauses:
                # Handle unless clauses with cascading priority
                self._generate_unless_rules(rule, rule_definitions)
            else:
                # Handle regular rules (with possible otherwise clause)
                self._generate_regular_rule(rule, rule_definitions)
        
        return textwrap.dedent("""
        % =============================================================================
        % SLEEC RULE DEFINITIONS
        % =============================================================================
        """).strip() + "\n\n" + "\n\n".join(rule_definitions)
    
    def _generate_unless_rules(self, rule, rule_definitions):
        """Generate multiple rules for unless statements with cascading priority"""
        rule_id = rule.id.lower()
        base_condition = rule.condition
        
        # Build cascading conditions for each unless clause
        unless_conditions = []
        for unless_clause in rule.unless_clauses:
            unless_conditions.append(unless_clause.condition)
        
        # Primary rule: original condition AND NOT all unless conditions
        primary_id = f"{rule_id}_primary"
        rule_definitions.append(f"exp({primary_id}).")
        
        # Build primary antecedent: base condition AND NOT unless1 AND NOT unless2 ...
        primary_antecedent = self._convert_condition_to_antecedent(base_condition)
        for unless_condition in unless_conditions:
            unless_antecedent = self._convert_condition_to_antecedent(unless_condition)
            # Remove "time(T)" from unless condition to avoid duplication
            unless_antecedent_clean = unless_antecedent.replace(", time(T)", "")
            primary_antecedent = primary_antecedent.replace(", time(T)", f", not {unless_antecedent_clean}, time(T)")
        
        rule_definitions.append(f"antecedent({primary_id}, T) :- {primary_antecedent}.")
        
        # Primary action (skip if it's a negated action)
        if not rule.action.strip().startswith("not "):
            consequent_action = f"happens({rule.action.lower()}, T)"
            rule_definitions.append(f"consequent({primary_id}, T) :- time(T), {consequent_action}.")
        
        # Unless rules: each unless clause gets higher priority
        for i, unless_clause in enumerate(rule.unless_clauses, 1):
            # Skip unless rule entirely if it's a negated action
            if unless_clause.action.strip().startswith("not "):
                continue
                
            unless_id = f"{rule_id}_unless{i}"
            rule_definitions.append(f"exp({unless_id}).")
            
            # Build unless antecedent: base condition AND this unless condition AND NOT higher priority unless conditions
            unless_antecedent = self._convert_condition_to_antecedent(base_condition)
            
            # Add this unless condition
            this_unless_condition = self._convert_condition_to_antecedent(unless_clause.condition)
            this_unless_clean = this_unless_condition.replace(", time(T)", "")
            unless_antecedent = unless_antecedent.replace(", time(T)", f", {this_unless_clean}, time(T)")
            
            # Add negation of higher priority unless conditions (later in the list)
            for j in range(i, len(rule.unless_clauses)):
                higher_unless_condition = self._convert_condition_to_antecedent(rule.unless_clauses[j].condition)
                higher_unless_clean = higher_unless_condition.replace(", time(T)", "")
                unless_antecedent = unless_antecedent.replace(", time(T)", f", not {higher_unless_clean}, time(T)")
            
            rule_definitions.append(f"antecedent({unless_id}, T) :- {unless_antecedent}.")
            
            # Unless action
            unless_consequent_action = f"happens({unless_clause.action.lower()}, T)"
            rule_definitions.append(f"consequent({unless_id}, T) :- time(T), {unless_consequent_action}.")
    
    def _generate_regular_rule(self, rule, rule_definitions):
        """Generate regular rule (possibly with otherwise clause)"""
        rule_id = rule.id.lower()
        
        # Rule identifier
        rule_definitions.append(f"exp({rule_id}).")
        
        # Antecedent logic
        antecedent_condition = self._convert_condition_to_antecedent(rule.condition)
        rule_definitions.append(f"antecedent({rule_id}, T) :- {antecedent_condition}.")
        
        # Consequent logic
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
            otherwise_consequent = f"happens({rule.otherwise_action.lower()}, T)"
            rule_definitions.append(f"consequent({otherwise_id}, T) :- time(T), {otherwise_consequent}.")
    
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
        
        # Remove parentheses around 'not' expressions - fix for Clingo syntax
        condition = re.sub(r'\(\s*not\s+([^)]+)\)', r'not \1', condition)
        
        # Remove unnecessary parentheses around comma-separated expressions
        # This handles cases like (holds_at(x,T), holds_at(y,T)) -> holds_at(x,T), holds_at(y,T)
        condition = self._remove_logical_grouping_parentheses(condition)
        
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
        """Remove unnecessary logical grouping parentheses around comma-separated expressions"""
        # Handle multiple patterns:
        # 1. Remove outer parentheses around complete expressions like (a, b)
        # 2. Remove inner parentheses around sub-expressions like a, (b, c), d
        
        # Pattern 1: Remove outer parentheses if entire expression is wrapped
        if condition.startswith('(') and condition.endswith(')') and ';' not in condition:
            # Check if removing outer parentheses leaves a valid comma-separated expression
            inner = condition[1:-1]
            if ',' in inner and not inner.startswith('('):
                condition = inner
        
        # Pattern 2: Remove parentheses around specific sub-patterns
        # (holds_at(...), holds_at(...)) -> holds_at(...), holds_at(...)
        pattern = r'\((holds_at\([^)]+\),\s*holds_at\([^)]+\))\)'
        condition = re.sub(pattern, r'\1', condition)
        
        # Pattern 3: Mixed patterns like a, (b, c), d
        # Look for patterns like ", (expr, expr)," and remove the parentheses
        pattern = r',\s*\(([^()]+,\s*[^()]+)\)\s*,'
        condition = re.sub(pattern, r', \1,', condition)
        
        return condition
    
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
            
            if rule.unless_clauses:
                # Handle unless rules - generate satisfaction logic for all generated rules
                self._generate_unless_satisfaction_logic(rule, satisfaction_logic)
            else:
                # Handle regular rules
                self._generate_regular_satisfaction_logic(rule, satisfaction_logic)
        
        # Hard constraint: every rule must be satisfied at every time point
        satisfaction_logic.append("""
% Hard constraint: every rule must be satisfied at every time point
:- exp(R), time(T), not holds(R,T).""")
        
        return textwrap.dedent("""
        % =============================================================================
        % RULE SATISFACTION LOGIC
        % =============================================================================
        """).strip() + "\n\n" + "\n\n".join(satisfaction_logic)
    
    def _generate_unless_satisfaction_logic(self, rule, satisfaction_logic):
        """Generate satisfaction logic for unless rules"""
        rule_id = rule.id.lower()
        
        # Primary rule satisfaction logic
        primary_id = f"{rule_id}_primary"
        satisfaction_logic.append(f"""
% Non-vacuous satisfaction for {primary_id}
holds_nv({primary_id}, T):-
    time(T),
    antecedent({primary_id}, T),
    consequent({primary_id}, T).""")
        
        satisfaction_logic.append(f"""
% Vacuous satisfaction for {primary_id}
holds_v({primary_id}, T):-
    time(T),
    not antecedent({primary_id}, T),
    not consequent({primary_id}, T).""")
        
        # Unless clause satisfaction logic
        for i, unless_clause in enumerate(rule.unless_clauses, 1):
            # Skip satisfaction logic for negated actions
            if unless_clause.action.strip().startswith("not "):
                continue
                
            unless_id = f"{rule_id}_unless{i}"
            satisfaction_logic.append(f"""
% Non-vacuous satisfaction for {unless_id}
holds_nv({unless_id}, T):-
    time(T),
    antecedent({unless_id}, T),
    consequent({unless_id}, T).""")
            
            satisfaction_logic.append(f"""
% Vacuous satisfaction for {unless_id}
holds_v({unless_id}, T):-
    time(T),
    not antecedent({unless_id}, T),
    not consequent({unless_id}, T).""")
    
    def _generate_regular_satisfaction_logic(self, rule, satisfaction_logic):
        """Generate satisfaction logic for regular rules"""
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
    
    def _generate_action_generation_and_constraints(self) -> str:
        """Generate action generation and constraints"""
        sections = []
        
        # Generate triggering events (events in conditions but not in actions)
        triggering_events = self._get_triggering_events()
        if triggering_events:
            triggering_rules = []
            for event in triggering_events:
                triggering_rules.append(f"{{ happens({event}, T) }} :- time(T).")
            sections.append("% Triggering event instantiation\n" + "\n".join(triggering_rules))
        
        # Generate action events (events that appear as consequences)
        action_events = self._get_action_events()
        if action_events:
            action_rules = []
            for event in action_events:
                action_rules.append(f"{{ happens({event}, T) }} :- time(T).")
            sections.append("% Action event instantiation\n" + "\n".join(action_rules))
        
        # Add measure instantiation if measures exist
        if self.measures:
            measure_rules = []
            for measure in self.measures:
                if measure.type == MeasureType.BOOLEAN:
                    measure_rules.append(f"{{ holds_at({measure.name.lower()}, T) }} :- time(T).")
                elif measure.type == MeasureType.NUMERIC:
                    measure_rules.append(f"{{ holds_at({measure.name.lower()}, V, T) : {self.config.numeric_range} }} :- time(T).")
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
    
    def _get_action_events(self) -> Set[str]:
        """Get events that appear in rule actions (consequence events)"""
        action_events = set()
        
        for rule in self.rules:
            # Extract events from actions
            if rule.action:
                action_events.add(rule.action.lower())
            if rule.otherwise_action:
                action_events.add(rule.otherwise_action.lower())
        
        return action_events
    
    def _generate_output_specification(self) -> str:
        """Generate output specification"""
        sections = []
        
        # Show statements from config
        if self.config.show_predicates:
            for predicate in self.config.show_predicates:
                sections.append(f"#show {predicate}.")
        
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