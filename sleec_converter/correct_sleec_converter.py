#!/usr/bin/env python3
"""
Correct SLEEC to Clingo Converter (Dalal's Way)
==============================================

This module converts SLEEC rules into Clingo format following Dalal's approach,
which uses antecedent/consequent structure and rule satisfaction logic.

Based on:
- Dalal_basic.lp (simple actions)
- with_measures.lp (actions with measures)

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
        if self.rules:
            conditions = []
            actions = []
            for rule in self.rules:
                conditions.append(rule.condition)
                actions.append(rule.action)
            rule_desc = f"When {' and '.join(conditions)} then {' and '.join(actions)}"
        
        return textwrap.dedent(f"""
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %                           SLEEC RULE IMPLEMENTATION
        %                              {rule_desc}
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """).strip()
    
    def _generate_domain_definitions(self) -> str:
        """Generate domain definitions section"""
        sections = []
        
        # Header
        sections.append(textwrap.dedent("""
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %                              1. DOMAIN DEFINITIONS
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """).strip())
        
        # Events - use 'action' if no measures, 'event' if there are measures
        if self.events:
            if self.measures:
                sections.append("% Events")
                sections.extend(f"event({event.name.lower()})." for event in self.events)
            else:
                sections.append("% Available actions the system can perform - these are Events")
                sections.extend(f"action({event.name.lower()}).   % actions" for event in self.events)
        
        # Measures
        if self.measures:
            sections.append("\n% Measures")
            sections.extend(f"measure({measure.name.lower()})." for measure in self.measures)
        
        # Time domain
        sections.append(f"\n% Time domain and priorities")
        sections.append(f"time(0..{self.max_time}).        % duration of the trace - time ranges from 0 to {self.max_time}")
        
        return '\n'.join(sections)
    
    def _generate_sleec_rule_definitions(self) -> str:
        """Generate SLEEC rule definitions section"""
        if not self.rules:
            return ""
        
        sections = []
        
        # Header
        sections.append(textwrap.dedent("""
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %                              2. SLEEC RULE DEFINITION
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """).strip())
        
        # Rule identifiers
        for rule in self.rules:
            sections.append(f"% Rule identifier")
            sections.append(f"exp({rule.id.lower()}).            % {rule.id.lower()} is the name of the SLEEC rule")
        
        # Antecedent and consequent logic for each rule
        for rule in self.rules:
            sections.append(f"\n% ----------------------------- ANTECEDENT LOGIC -----------------------------")
            sections.append(f"% The rule is triggered when {rule.condition}")
            
            # Convert condition to antecedent
            antecedent_body = self._convert_condition_to_antecedent(rule.condition)
            sections.append(f"antecedent({rule.id.lower()},T):-")
            sections.append(f"\ttime(T),")
            sections.append(f"\t{antecedent_body}.")
            
            sections.append(f"\n% ----------------------------- CONSEQUENT LOGIC -----------------------------")
            sections.append(f"% NOTE: LINA SAID ON THE CALL THE CONSEQUENTS HAPPEN AT THE SAME TIMESTEP AS THE ANTECEDENT")
            sections.append(f"% unless there is a within statement")
            
            # Convert action to consequent
            action_name = rule.action.strip().lower()
            if rule.action.strip().startswith("not "):
                action_name = rule.action.strip()[4:].strip().lower()
                # Handle negated actions if needed
            
            sections.append(f"consequent({rule.id.lower()},T):-")
            sections.append(f"\ttime(T),")
            sections.append(f"\thappens({action_name},T).")
            
        return '\n'.join(sections)
    
    def _convert_condition_to_antecedent(self, condition: str) -> str:
        """Convert a SLEEC condition to antecedent body format"""
        # Convert events to happens()
        for event in self.events:
            condition = re.sub(rf'\b{event.name}\b', f'happens({event.name.lower()},T)', condition)
        
        # Convert measures {measure} to holds_at(measure,T)
        condition = re.sub(r'\{(\w+)\}', r'holds_at(\1,T)', condition)
        
        # Handle logical operators
        condition = condition.replace(' and ', ',\n\t')
        condition = condition.replace(' or ', ' ; ')
        
        # Clean up extra whitespace and parentheses
        condition = re.sub(r'\s+', ' ', condition)
        condition = condition.strip()
        
        return condition
    
    def _generate_rule_satisfaction_logic(self) -> str:
        """Generate rule satisfaction logic section"""
        if not self.rules:
            return ""
        
        sections = []
        
        # Header
        sections.append(textwrap.dedent("""
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %                           3. RULE SATISFACTION LOGIC
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """).strip())
        
        # General holds logic
        sections.append("% ----------------------------- GENERAL HOLDS LOGIC -------------------------")
        sections.append("% Rule holds if it holds non-vacuously (antecedent true AND consequent met)")
        sections.append("holds(G, T):-")
        sections.append("\ttime(T),")
        sections.append("\texp(G),")
        sections.append("\tholds_nv(G, T).")
        
        sections.append("\n% Rule holds vacuously (antecedent never true)")
        sections.append("holds(G, T):-")
        sections.append("\ttime(T),")
        sections.append("\texp(G),")
        sections.append("\tholds_v(G, T).")
        
        # Specific holds logic for each rule
        sections.append("\n% ----------------------------- SPECIFIC HOLDS LOGIC ------------------------")
        sections.append("% WHAT IT MEANS FOR RULES TO HOLD:")
        sections.append("% simple rules without within statements happen at the same time as the antecedent -")
        sections.append("% therefore, they cannot hold at the end of time")
        
        for rule in self.rules:
            rule_id = rule.id.lower()
            
            sections.append(f"\n% Non-vacuous satisfaction: antecedent true AND consequent met")
            sections.append(f"holds_nv({rule_id},T):-")
            sections.append(f"\ttime(T),")
            sections.append(f"\tantecedent({rule_id},T),")
            sections.append(f"\tconsequent({rule_id},T).")
            
            sections.append(f"\n% Vacuous satisfaction: antecedent never true")
            sections.append(f"holds_v({rule_id},T):-")
            sections.append(f"\ttime(T),")
            sections.append(f"\tnot antecedent({rule_id},T),")
            sections.append(f"\tnot consequent({rule_id},T).")
        
        # Hard constraints
        sections.append("\n% ----------------------------- HARD CONSTRAINTS ----------------------------")
        sections.append("% Hard constraint: every rule must be satisfied at every time point")
        sections.append(":- exp(R), time(T), not holds(R,T).")
        
        return '\n'.join(sections)
    
    def _generate_action_generation_and_constraints(self) -> str:
        """Generate action generation and constraints section"""
        sections = []
        
        # Header
        sections.append(textwrap.dedent("""
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %                       4. ACTION GENERATION AND CONSTRAINTS
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """).strip())
        
        # Generate actions based on whether we have measures
        if self.measures:
            sections.append("% Generate 0 or more events: ASP chooses which events to perform when")
            sections.append("% here we are asking ASP to generate 0 or more events with particular goals to generate a plan")
            sections.append("0{happens(A,T):event(A), time(T)}.")
        else:
            sections.append("% Generate 0 or more actions: ASP chooses which actions to perform when")
            sections.append("% here we are asking ASP to generate 0 or more actions with particular goals to generate a plan")
            sections.append("0{happens(A,T):action(A), time(T)}.")
        
        # Optimization (commented out by default like in the examples)
        sections.append("\n% ----------------------------- OPTIMIZATION ---------------------------------")
        sections.append("% Plan length calculation")
        if self.measures:
            sections.append("%plan_length(N):-")
            sections.append("%\tN= #count {T: time(T), event(A), happens(A,T)}.")
            sections.append("\n% Minimize plan length (prefer fewer events overall)")
        else:
            sections.append("%plan_length(N):-")
            sections.append("%\tN= #count {T: time(T), action(A), happens(A,T)}.")
            sections.append("\n% Minimize plan length (prefer fewer actions overall)")
        sections.append("%#minimize {N@2: plan_length(N)}.")
        
        return '\n'.join(sections)
    
    def _generate_output_specification(self) -> str:
        """Generate output specification section"""
        sections = []
        
        # Header
        sections.append(textwrap.dedent("""
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %                            5. OUTPUT SPECIFICATION
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        """).strip())
        
        # Generate sample measure values if we have measures
        if self.measures:
            for measure in self.measures:
                if measure.type == MeasureType.BOOLEAN:
                    # Add some sample values
                    sections.append(f"holds_at({measure.name.lower()}, 0).")
                    sections.append(f"holds_at({measure.name.lower()}, 1).")
                    break  # Just show one example
        
        # Show statements
        if self.measures:
            sections.append(f"\n% Show which events happen when")
            sections.append("#show holds_at/2.")
            sections.append("#show happens/2.")
        else:
            sections.append(f"% Show which actions happen when")
            sections.append("#show happens/2.")
        
        return '\n'.join(sections)

# Example usage and testing
if __name__ == "__main__":
    # Test with a simple SLEEC rule
    test_sleec = """
    def_start
        event OpenDoor
        event PlaySound
        
        measure isDaytime: boolean
    def_end
    
    rule_start
        R1 when OpenDoor and {isDaytime} then PlaySound
    rule_end
    """
    
    converter = CorrectSleecConverter()
    result = converter.convert_sleec_string(test_sleec)
    print(result) 