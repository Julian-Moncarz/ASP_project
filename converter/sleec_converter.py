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
        
        return '\n\n'.join(filter(None, sections)) + ' '
    
    def _generate_header(self) -> str:
        """Generate the file header"""
        rule_desc = ""
        for rule in self.rules:
            if rule.within_constraint:
                rule_desc += f"% {rule.id}: {rule.condition} -> {rule.action} within {rule.within_constraint}\n"
            else:
                rule_desc += f"% {rule.id}: {rule.condition} -> {rule.action}\n"
            if rule.otherwise_action:
                rule_desc += f"%   otherwise -> {rule.otherwise_action}\n"
        
        return f"""% =============================================================================
% SLEEC to Clingo Conversion (Dalal's Format with Within Support)
% =============================================================================
% 
% This file was automatically generated from SLEEC rules.
% Format: Antecedent/consequent structure with temporal constraints
% 
% Rules Converted:
{rule_desc.rstrip()}"""
    
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
        
        # Extract unless conditions for easier processing
        unless_conditions = self._extract_unless_conditions(rule.unless_clauses)
        
        # Generate primary rule (original condition AND NOT all unless conditions)
        self._generate_primary_unless_rule(rule, rule_id, unless_conditions, rule_definitions)
        
        # Generate unless clause rules (each with cascading priority)
        self._generate_unless_clause_rules(rule, rule_id, unless_conditions, rule_definitions)
    
    def _extract_unless_conditions(self, unless_clauses):
        """Extract conditions from unless clauses for easier processing"""
        return [unless_clause.condition for unless_clause in unless_clauses]
    
    def _generate_primary_unless_rule(self, rule, rule_id, unless_conditions, rule_definitions):
        """Generate the primary rule with negated unless conditions"""
        primary_id = f"{rule_id}_primary"
        rule_definitions.append(f"exp({primary_id}).")
        
        # Build primary antecedent: base condition AND NOT unless1 AND NOT unless2 ...
        primary_antecedent = self._build_primary_unless_antecedent(rule.condition, unless_conditions)
        rule_definitions.append(f"antecedent({primary_id}, T) :- {primary_antecedent}.")
        
        # Generate primary consequent (skip if negated action)
        if not rule.action.strip().startswith("not "):
            consequent_action = self._build_consequent_action(rule.action, rule.within_constraint)
            rule_definitions.append(f"consequent({primary_id}, T) :- time(T), {consequent_action}.")
    
    def _build_primary_unless_antecedent(self, base_condition, unless_conditions):
        """Build antecedent for primary rule by negating all unless conditions"""
        primary_antecedent = self._convert_condition_to_antecedent(base_condition)
        
        for unless_condition in unless_conditions:
            unless_antecedent = self._convert_condition_to_antecedent(unless_condition)
            # Remove "time(T)" to avoid duplication
            unless_antecedent_clean = unless_antecedent.replace(", time(T)", "")
            primary_antecedent = primary_antecedent.replace(", time(T)", f", not {unless_antecedent_clean}, time(T)")
        
        return primary_antecedent
    
    def _generate_unless_clause_rules(self, rule, rule_id, unless_conditions, rule_definitions):
        """Generate rules for each unless clause with cascading priority"""
        for i, unless_clause in enumerate(rule.unless_clauses, 1):
            # Skip unless rule entirely if it's a negated action
            if unless_clause.action.strip().startswith("not "):
                continue
                
            unless_id = f"{rule_id}_unless{i}"
            rule_definitions.append(f"exp({unless_id}).")
            
            # Build unless antecedent with cascading priority
            unless_antecedent = self._build_unless_clause_antecedent(
                rule.condition, unless_clause, rule.unless_clauses, i
            )
            rule_definitions.append(f"antecedent({unless_id}, T) :- {unless_antecedent}.")
            
            # Generate unless consequent
            unless_consequent_action = f"happens({unless_clause.action.lower()}, T, T)"
            rule_definitions.append(f"consequent({unless_id}, T) :- time(T), {unless_consequent_action}.")
    
    def _build_unless_clause_antecedent(self, base_condition, unless_clause, all_unless_clauses, clause_index):
        """Build antecedent for unless clause with cascading priority logic"""
        unless_antecedent = self._convert_condition_to_antecedent(base_condition)
        
        # Add this unless condition
        this_unless_condition = self._convert_condition_to_antecedent(unless_clause.condition)
        this_unless_clean = this_unless_condition.replace(", time(T)", "")
        unless_antecedent = unless_antecedent.replace(", time(T)", f", {this_unless_clean}, time(T)")
        
        # Add negation of higher priority unless conditions (later in the list)
        for j in range(clause_index, len(all_unless_clauses)):
            higher_unless_condition = self._convert_condition_to_antecedent(all_unless_clauses[j].condition)
            higher_unless_clean = higher_unless_condition.replace(", time(T)", "")
            unless_antecedent = unless_antecedent.replace(", time(T)", f", not {higher_unless_clean}, time(T)")
        
        return unless_antecedent
    
    def _build_consequent_action(self, action, within_constraint):
        """Build consequent action with optional within constraint"""
        if within_constraint:
            # Parse constraint to get numeric value (e.g., "3 minutes" -> 3)
            constraint_parts = within_constraint.split()
            constraint_value = constraint_parts[0]
            return f"happens({action.lower()}, T, T2), T <= T2, T2 <= T+{constraint_value}, time(T2)"
        else:
            return f"happens({action.lower()}, T, T)"
    
    def _generate_regular_rule(self, rule, rule_definitions):
        """Generate regular rule (possibly with otherwise clause)"""
        rule_id = rule.id.lower()
        
        # Rule identifier
        rule_definitions.append(f"exp({rule_id}).")
        
        # Antecedent logic
        antecedent_condition = self._convert_condition_to_antecedent(rule.condition)
        
        # Determine if this rule involves temporal events
        within_events = self._get_within_events()
        uses_temporal_events = any(event.name.lower() in within_events for event in self.events 
                                   if event.name.lower() in rule.condition.lower())
        
        if uses_temporal_events:
            rule_definitions.append(f"antecedent({rule_id}, T2) :- {antecedent_condition}.")
        else:
            rule_definitions.append(f"antecedent({rule_id}, T) :- {antecedent_condition}.")
        
        # Consequent logic
        if rule.within_constraint:
            # Parse constraint to get numeric value (e.g., "3 minutes" -> 3)
            constraint_parts = rule.within_constraint.split()
            constraint_value = constraint_parts[0]
            consequent_action = f"happens({rule.action.lower()}, T, T2), T <= T2, T2 <= T+{constraint_value}, time(T2)"
        else:
            consequent_action = f"happens({rule.action.lower()}, T, T)"
        rule_definitions.append(f"consequent({rule_id}, T) :- time(T), {consequent_action}.")
        
        # Otherwise clause if present
        if rule.otherwise_action:
            otherwise_id = f"{rule_id}_otherwise"
            rule_definitions.append(f"exp({otherwise_id}).")
            
            # Negated antecedent
            negated_antecedent = self._negate_antecedent(rule.condition)
            rule_definitions.append(f"antecedent({otherwise_id}, T) :- {negated_antecedent}.")
            
            # Otherwise consequent
            otherwise_consequent = f"happens({rule.otherwise_action.lower()}, T, T)"
            rule_definitions.append(f"consequent({otherwise_id}, T) :- time(T), {otherwise_consequent}.")
    
    def _convert_condition_to_antecedent(self, condition: str) -> str:
        """Convert a SLEEC condition to antecedent format"""
        # Apply transformations in logical order
        condition = self._normalize_condition_case(condition)
        condition = self._replace_measure_references(condition)
        condition = self._replace_logical_operators(condition)
        condition = self._clean_parentheses(condition)
        condition = self._replace_event_references(condition)
        condition = self._add_time_constraints(condition)
        
        return condition
    
    def _normalize_condition_case(self, condition: str) -> str:
        """Convert condition to lowercase for consistent processing"""
        return condition.lower()
    
    def _replace_measure_references(self, condition: str) -> str:
        """Replace measure references with Clingo holds_at predicates"""
        # Replace measure references {measureName} with holds_at(measureName, T)
        condition = re.sub(r'\{(\w+)\}', r'holds_at(\1, T)', condition)
        
        # Replace measure comparisons {measureName} = value with holds_at(measureName, value, T)
        condition = re.sub(r'holds_at\((\w+), T\)\s*=\s*(\w+)', r'holds_at(\1, \2, T)', condition)
        
        return condition
    
    def _replace_logical_operators(self, condition: str) -> str:
        """Replace SLEEC logical operators with Clingo equivalents"""
        # Replace logical operators
        condition = condition.replace(' and ', ', ')
        condition = condition.replace(' or ', '; ')
        condition = condition.replace(' not ', 'not ')
        
        return condition
    
    def _clean_parentheses(self, condition: str) -> str:
        """Clean up unnecessary parentheses for Clingo syntax"""
        # Remove parentheses around 'not' expressions - fix for Clingo syntax
        condition = re.sub(r'\(\s*not\s+([^)]+)\)', r'not \1', condition)
        
        # Remove unnecessary parentheses around comma-separated expressions
        condition = self._remove_logical_grouping_parentheses(condition)
        
        return condition
    
    def _replace_event_references(self, condition: str) -> str:
        """Replace event names with Clingo happens predicates"""
        within_events = self._get_within_events()
        
        # Replace event references
        for event in self.events:
            event_name = event.name.lower()
            if event_name in within_events:
                # Events with within constraints use temporal format
                condition = re.sub(rf'\b{event_name}\b', f'happens({event_name}, T, T2)', condition)
            else:
                # Regular events use standard format
                condition = re.sub(rf'\b{event_name}\b', f'happens({event_name}, T, T)', condition)
        
        return condition
    
    def _add_time_constraints(self, condition: str) -> str:
        """Add appropriate time constraints based on events used"""
        within_events = self._get_within_events()
        
        # Add time constraints
        if any(event.name.lower() in within_events for event in self.events if event.name.lower() in condition):
            condition += ", time(T), time(T2)"
        else:
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
        satisfaction_logic.append("""% Hard constraint: every rule must be satisfied at every time point
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
        satisfaction_logic.append(f"""% Non-vacuous satisfaction for {rule_id}
holds_nv({rule_id}, T):-
    time(T),
    antecedent({rule_id}, T),
    consequent({rule_id}, T).""")
        
        # Vacuous satisfaction: antecedent not true AND consequent does not happen
        satisfaction_logic.append(f"""% Vacuous satisfaction for {rule_id}
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
        
        # Generate each section with focused methods
        triggering_section = self._generate_triggering_events_section()
        if triggering_section:
            sections.append(triggering_section)
        
        action_section = self._generate_action_events_section()
        if action_section:
            sections.append(action_section)
        
        measure_section = self._generate_measure_instantiation_section()
        if measure_section:
            sections.append(measure_section)
        
        return self._assemble_action_generation_sections(sections)
    
    def _generate_triggering_events_section(self) -> str:
        """Generate triggering events with contextual comments"""
        triggering_events = self._get_triggering_events()
        if not triggering_events:
            return ""
        
        triggering_rules = [f"{{ happens({event}, T, T) }} :- time(T)." for event in triggering_events]
        comment = self._get_triggering_events_comment()
        
        return comment + "\n" + "\n".join(triggering_rules)
    
    def _get_triggering_events_comment(self) -> str:
        """Generate contextual comment for triggering events based on system characteristics"""
        action_events_with_within, action_events_without_within = self._get_action_events_with_constraints()
        
        # Choose comment based on event type patterns
        if action_events_with_within and action_events_without_within:
            # Mixed: both within and immediate events
            return "% Triggering event instantiation (TriggerTime = ActualTime for direct triggers)"
        elif action_events_with_within and self.measures:
            # Only within events, but has measures
            return "% Triggering event instantiation (TriggerTime = ActualTime for non-within events)"
        else:
            # Simple case: no measures or only immediate events
            return "% Triggering event instantiation"
    
    def _generate_action_events_section(self) -> str:
        """Generate action events with contextual comments and constraints"""
        action_events_with_within, action_events_without_within = self._get_action_events_with_constraints()
        
        if not action_events_with_within and not action_events_without_within:
            return ""
        
        action_rules = []
        
        # Add non-within events first
        action_rules.extend(self._generate_regular_action_rules(action_events_without_within))
        
        # Add within events
        action_rules.extend(self._generate_within_action_rules(action_events_with_within))
        
        comment = self._get_action_events_comment(action_events_with_within, action_events_without_within)
        
        return comment + "\n" + "\n".join(action_rules)
    
    def _generate_regular_action_rules(self, action_events_without_within) -> List[str]:
        """Generate rules for regular (non-within) action events"""
        return [f"{{ happens({event}, T, T) }} :- time(T)." for event in action_events_without_within]
    
    def _generate_within_action_rules(self, action_events_with_within) -> List[str]:
        """Generate rules for action events with within constraints"""
        within_rules = []
        for event, constraint in action_events_with_within:
            constraint_parts = constraint.split()
            constraint_value = constraint_parts[0]
            within_rules.append(f"{{ happens({event}, T1, T2) : T1 <= T2, T2 <= T1+{constraint_value} }} :- time(T1), time(T2).")
        return within_rules
    
    def _get_action_events_comment(self, action_events_with_within, action_events_without_within) -> str:
        """Generate contextual comment for action events based on constraint characteristics"""
        if action_events_without_within:
            return "% Action event instantiation "
        else:
            # Check if any constraint is large (might extend beyond time domain)
            has_large_constraint = any(int(constraint.split()[0]) > self.config.max_time 
                                      for _, constraint in action_events_with_within)
            if has_large_constraint:
                return "% Action event instantiation (window constrained by time domain)"
            else:
                return "% Action event instantiation (can be triggered at any time within temporal window)"
    
    def _generate_measure_instantiation_section(self) -> str:
        """Generate measure instantiation for all measure types"""
        if not self.measures:
            return ""
        
        measure_rules = []
        for measure in self.measures:
            measure_rules.append(self._generate_single_measure_rule(measure))
        
        return "% Measure instantiation\n" + "\n".join(measure_rules)
    
    def _generate_single_measure_rule(self, measure) -> str:
        """Generate instantiation rule for a single measure based on its type"""
        measure_name = measure.name.lower()
        
        if measure.type == MeasureType.BOOLEAN:
            return f"{{ holds_at({measure_name}, T) }} :- time(T)."
        elif measure.type == MeasureType.NUMERIC:
            return f"{{ holds_at({measure_name}, V, T) : {self.config.numeric_range} }} :- time(T)."
        elif measure.type == MeasureType.SCALE and measure.scale_values:
            scale_options = " ; ".join([f"holds_at({measure_name}, {value.lower()}, T)" for value in measure.scale_values])
            return f"1 {{ {scale_options} }} 1 :- time(T)."
        else:
            # Fallback for unknown types
            return f"{{ holds_at({measure_name}, T) }} :- time(T)."
    
    def _assemble_action_generation_sections(self, sections: List[str]) -> str:
        """Assemble all action generation sections with proper formatting"""
        if not sections:
            return ""
        
        header = textwrap.dedent("""
        % =============================================================================
        % ACTION GENERATION AND CONSTRAINTS
        % =============================================================================
        """).strip()
        
        return header + "\n\n" + "\n\n".join(sections)
    
    def _extract_valid_actions_from_rule(self, rule) -> List[str]:
        """Extract all valid action events from a rule (excluding negated actions)"""
        actions = []
        
        # Primary action
        if rule.action and not rule.action.strip().startswith("not "):
            actions.append(rule.action.lower())
        
        # Otherwise action  
        if rule.otherwise_action and not rule.otherwise_action.strip().startswith("not "):
            actions.append(rule.otherwise_action.lower())
        
        # Unless clause actions
        if rule.unless_clauses:
            for unless_clause in rule.unless_clauses:
                if unless_clause.action and not unless_clause.action.strip().startswith("not "):
                    actions.append(unless_clause.action.lower())
        
        return actions
    
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
            actions = self._extract_valid_actions_from_rule(rule)
            action_events.update(actions)
        
        # Triggering events are those in conditions but not in actions
        return condition_events - action_events
    
    def _get_action_events_with_constraints(self) -> Tuple[List[Tuple[str, str]], Set[str]]:
        """Get action events separated by whether they have within constraints"""
        action_events_with_within = []
        action_events_without_within = set()
        
        for rule in self.rules:
            # Handle primary action with possible within constraint
            if rule.action and not rule.action.strip().startswith("not "):
                if rule.within_constraint:
                    action_events_with_within.append((rule.action.lower(), rule.within_constraint))
                else:
                    action_events_without_within.add(rule.action.lower())
            
            # Handle otherwise and unless actions (no within constraints)
            if rule.otherwise_action and not rule.otherwise_action.strip().startswith("not "):
                action_events_without_within.add(rule.otherwise_action.lower())
            
            if rule.unless_clauses:
                for unless_clause in rule.unless_clauses:
                    if unless_clause.action and not unless_clause.action.strip().startswith("not "):
                        action_events_without_within.add(unless_clause.action.lower())
        
        return action_events_with_within, action_events_without_within
    
    def _get_action_events(self) -> Set[str]:
        """Get all action events as a simple set"""
        action_events = set()
        
        for rule in self.rules:
            actions = self._extract_valid_actions_from_rule(rule)
            action_events.update(actions)
        
        return action_events
    
    def _get_within_events(self) -> Set[str]:
        """Get events that are produced with within constraints"""
        within_events = set()
        
        for rule in self.rules:
            if rule.action and rule.within_constraint:
                within_events.add(rule.action.lower())
        
        return within_events
    
    def _generate_output_specification(self) -> str:
        """Generate output specification"""
        sections = []
        
        # Show statements based on what's actually in the SLEEC file
        if self.measures:
            sections.append("#show holds_at/2.")
        
        sections.append("#show happens/3.")
        
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