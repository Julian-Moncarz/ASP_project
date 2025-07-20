"""
Test suite for SLEEC to Clingo Converter (Dalal's Format)
=========================================================

Comprehensive tests covering:
1. Unit tests for individual converter methods
2. Integration tests for complete conversion pipeline
3. Behavioral tests for rule compliance and logical correctness
4. Regression tests for known working cases
5. Unless statement support tests
"""

import pytest
import os
import re
import tempfile
import subprocess
from pathlib import Path
from unittest.mock import patch, MagicMock

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from converter.sleec_converter import SleecToClingoConverter
from converter.parser import SleecParser, Event, Measure, Rule, MeasureType
from converter.config import ConverterConfig, DEFAULT_CONFIG


class TestSleecToClingoConverter:
    """Test class for SleecToClingoConverter"""
    
    def setup_method(self):
        """Set up test fixtures"""
        self.converter = SleecToClingoConverter()
        self.test_events = [
            Event("ButtonPress", 1),
            Event("LightOn", 2), 
            Event("AlarmActivate", 3)
        ]
        self.test_measures = [
            Measure("isNight", MeasureType.BOOLEAN, 1),
            Measure("brightness", MeasureType.NUMERIC, 2),
            Measure("mode", MeasureType.SCALE, 3, scale_values=["low", "medium", "high"])
        ]

    # ========================================================================
    # UNIT TESTS - Individual Method Testing
    # ========================================================================

    def test_convert_condition_to_antecedent_simple_event(self):
        """Test conversion of simple event conditions"""
        self.converter.events = [Event("ButtonPress", 1)]

        condition = "ButtonPress"
        result = self.converter._convert_condition_to_antecedent(condition)
        expected = "happens(buttonpress, T, T), time(T)"

        assert result == expected

    def test_convert_condition_to_antecedent_simple_measure(self):
        """Test conversion of simple measure conditions"""
        condition = "{isNight}"
        result = self.converter._convert_condition_to_antecedent(condition)
        expected = "holds_at(isnight, T), time(T)"
        
        assert result == expected

    def test_convert_condition_to_antecedent_and_condition(self):
        """Test conversion of AND conditions"""
        self.converter.events = [Event("ButtonPress", 1)]

        condition = "ButtonPress and {isNight}"
        result = self.converter._convert_condition_to_antecedent(condition)
        expected = "happens(buttonpress, T, T), holds_at(isnight, T), time(T)"

        assert result == expected

    def test_convert_condition_to_antecedent_complex_and(self):
        """Test conversion of complex AND conditions with parentheses"""
        condition = "{sameLanguage} and {humanUnderstands}"
        result = self.converter._convert_condition_to_antecedent(condition)
        expected = "holds_at(samelanguage, T), holds_at(humanunderstands, T), time(T)"
        
        assert result == expected

    def test_convert_condition_to_antecedent_not_condition(self):
        """Test conversion of NOT conditions"""
        condition = "not {isLocked}"
        result = self.converter._convert_condition_to_antecedent(condition)
        expected = "not holds_at(islocked, T), time(T)"
        
        assert result == expected

    def test_convert_condition_to_antecedent_parenthesized_not(self):
        """Test conversion of parenthesized NOT conditions"""
        self.converter.events = [Event("DoorOpen", 1)]

        condition = "DoorOpen and (not {isLocked})"
        result = self.converter._convert_condition_to_antecedent(condition)
        expected = "happens(dooropen, T, T), not holds_at(islocked, T), time(T)"

        assert result == expected

    def test_remove_logical_grouping_parentheses(self):
        """Test removal of logical grouping parentheses"""
        test_cases = [
            # Simple case
            ("(holds_at(a, T), holds_at(b, T))", "holds_at(a, T), holds_at(b, T)"),
            # With spaces
            ("(holds_at(same, T),  holds_at(human, T))", "holds_at(same, T),  holds_at(human, T)"),
            # Should preserve function parentheses
            ("holds_at(test, T)", "holds_at(test, T)"),
            # Mixed case
            ("happens(event, T), (holds_at(a, T), holds_at(b, T)), time(T)",
             "happens(event, T), holds_at(a, T), holds_at(b, T), time(T)")
        ]
        
        for input_str, expected in test_cases:
            result = self.converter._remove_logical_grouping_parentheses(input_str)
            assert result == expected, f"Failed for input: {input_str}"

    def test_get_triggering_events(self):
        """Test identification of triggering events"""
        self.converter.events = [Event("ButtonPress", 1), Event("LightOn", 2), Event("AlarmActivate", 3)]
        self.converter.rules = [
            Rule("R1", "ButtonPress", "LightOn", 1),
            Rule("R2", "LightOn and {isNight}", "AlarmActivate", 2)
        ]
        
        triggering = self.converter._get_triggering_events()
        expected = {"buttonpress"}  # ButtonPress appears in conditions but not as consequence
        
        assert triggering == expected

    def test_get_action_events(self):
        """Test identification of action events"""
        self.converter.rules = [
            Rule("R1", "ButtonPress", "LightOn", 1),
            Rule("R2", "LightOn", "AlarmActivate", 2, otherwise_action="TurnOff")
        ]
        
        actions = self.converter._get_action_events()
        expected = {"lighton", "alarmactivate", "turnoff"}
        
        assert actions == expected

    # ========================================================================
    # INTEGRATION TESTS - Complete Conversion Pipeline
    # ========================================================================

    def test_convert_sleec_string_simple(self):
        """Test complete conversion of simple SLEEC string"""
        sleec_content = """
def_start
    event ButtonPress
    event LightOn
def_end

rule_start
    R1 when ButtonPress then LightOn
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Check for required sections
        assert "% DOMAIN DEFINITIONS" in result
        assert "% SLEEC RULE DEFINITIONS" in result
        assert "% RULE SATISFACTION LOGIC" in result
        assert "% ACTION GENERATION AND CONSTRAINTS" in result
        
        # Check for specific content
        assert "event(buttonpress)" in result
        assert "event(lighton)" in result
        assert "antecedent(r1, T)" in result
        assert "consequent(r1, T)" in result

    def test_convert_sleec_string_with_measures(self):
        """Test conversion with measures"""
        sleec_content = """
def_start
    event DoorOpen
    event AlarmActivate
    measure isLocked: boolean
def_end

rule_start
    R1 when DoorOpen and (not {isLocked}) then AlarmActivate
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Check measure handling
        assert "measure(islocked)" in result
        assert "holds_at(islocked, T)" in result
        assert "not holds_at(islocked, T)" in result

    def test_syntax_validation(self):
        """Test that generated Clingo has valid syntax"""
        sleec_content = """
def_start
    event EncounterHuman
    event InformHuman
    event IdentifyActivity
    measure sameLanguage: boolean
    measure humanUnderstands: boolean
def_end

rule_start
    R1 when EncounterHuman and ({sameLanguage} and {humanUnderstands}) then InformHuman
    R2 when EncounterHuman then IdentifyActivity
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Write to temp file and test with clingo
        with tempfile.NamedTemporaryFile(mode='w', suffix='.lp', delete=False) as f:
            f.write(result)
            temp_file = f.name
        
        try:
            # Test syntax by running clingo --help on the file (syntax check only)
            process = subprocess.run(['clingo', '--help'], 
                                   input=result, text=True, capture_output=True)
            # If clingo is available, test parsing with timeout
            if process.returncode == 0:
                # Use test configuration for syntax validation
                syntax_check = subprocess.run(['clingo', temp_file, f'--models={DEFAULT_CONFIG.test_models}', f'--time-limit={DEFAULT_CONFIG.test_time_limit}'], 
                                            capture_output=True, text=True, timeout=DEFAULT_CONFIG.test_timeout)
                # Should not have parsing errors
                assert "error:" not in syntax_check.stderr.lower()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            # Clingo not available or timeout, skip syntax check
            pytest.skip("Clingo not available or timeout for syntax validation")
        finally:
            os.unlink(temp_file)

    # ========================================================================
    # BEHAVIORAL TESTS - Rule Compliance and Logic
    # ========================================================================

    def test_rule_compliance_simple(self):
        """Test that generated models comply with rules"""
        sleec_content = """
def_start
    event ButtonPress
    event LightOn
def_end

rule_start
    R1 when ButtonPress then LightOn
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Check rule satisfaction logic is present
        assert "holds_nv(r1, T)" in result
        assert "holds_v(r1, T)" in result
        assert ":- exp(R), time(T), not holds(R,T)" in result

    def test_choice_rules_generation(self):
        """Test that choice rules are generated for all event types"""
        sleec_content = """
def_start
    event TriggerEvent
    event ActionEvent
    measure testMeasure: boolean
def_end

rule_start
    R1 when TriggerEvent and {testMeasure} then ActionEvent
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Check that both triggering and action events get choice rules
        assert "{ happens(triggerevent, T, T) }" in result
        assert "{ happens(actionevent, T, T) }" in result
        assert "{ holds_at(testmeasure, T) }" in result

    def test_multiple_rules_interaction(self):
        """Test conversion of multiple interacting rules"""
        sleec_content = """
def_start
    event ButtonPress
    event LightOn
    event SetBrightness
    measure isNight: boolean
def_end

rule_start
    R1 when ButtonPress then LightOn
    R2 when LightOn and {isNight} then SetBrightness
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Check both rules are present
        assert "exp(r1)" in result
        assert "exp(r2)" in result
        assert "antecedent(r1, T)" in result
        assert "antecedent(r2, T)" in result

    # ========================================================================
    # REGRESSION TESTS - Known Working Cases
    # ========================================================================

    def test_door_system_regression(self):
        """Test the door system case that we know works"""
        sleec_content = """
def_start
    event DoorOpen
    event AlarmActivate
    measure isLocked: boolean
def_end

rule_start
    R1 when DoorOpen and (not {isLocked}) then AlarmActivate
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Check critical elements
        assert "antecedent(r1, T) :- happens(dooropen, T, T), not holds_at(islocked, T), time(T)" in result
        assert "consequent(r1, T) :- time(T), happens(alarmactivate, T, T)" in result

    def test_lightswitch_system_regression(self):
        """Test the lightswitch system case"""
        sleec_content = """
def_start
    event ButtonPress
    event LightOn
    event SetBrightnessToMax
    measure isNight: boolean
def_end

rule_start
    R1 when ButtonPress then LightOn
    R2 when LightOn and {isNight} then SetBrightnessToMax
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Check rule chain structure
        assert "antecedent(r1, T) :- happens(buttonpress, T, T), time(T)" in result
        assert "antecedent(r2, T) :- happens(lighton, T, T), holds_at(isnight, T), time(T)" in result

    def test_aspen_system_regression(self):
        """Test the ASPEN R1 R2 case with complex conditions"""
        sleec_content = """
def_start
    event EncounterHuman
    event InformHuman
    event IdentifyActivity
    measure sameLanguage: boolean
    measure humanUnderstands: boolean
def_end

rule_start
    R1 when EncounterHuman and ({sameLanguage} and {humanUnderstands}) then InformHuman
    R2 when EncounterHuman then IdentifyActivity
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Check complex condition handling
        expected_antecedent = "antecedent(r1, T) :- happens(encounterhuman, T, T), holds_at(samelanguage, T), holds_at(humanunderstands, T), time(T)"
        assert expected_antecedent in result

    # ========================================================================
    # ERROR HANDLING TESTS
    # ========================================================================

    def test_file_not_found(self):
        """Test handling of missing files"""
        with pytest.raises(FileNotFoundError):
            self.converter.convert_file("nonexistent.sleec")

    def test_invalid_sleec_syntax(self):
        """Test handling of invalid SLEEC syntax"""
        invalid_sleec = """
def_start
    invalid syntax here
def_end
"""
        
        with pytest.raises(Exception):  # Should raise some parsing exception
            self.converter.convert_sleec_string(invalid_sleec)

    # ========================================================================
    # EDGE CASE TESTS  
    # ========================================================================

    def test_empty_rule_set(self):
        """Test conversion of SLEEC with no rules"""
        sleec_content = """
def_start
    event TestEvent
def_end

rule_start
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Should still generate basic structure
        assert "% DOMAIN DEFINITIONS" in result
        assert "event(testevent)" in result

    def test_single_event_no_measures(self):
        """Test minimal SLEEC file"""
        sleec_content = """
def_start
    event SingleEvent
def_end

rule_start
    R1 when SingleEvent then SingleEvent
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Should handle self-reference correctly
        assert "happens(singleevent, T, T)" in result

    def test_measure_types(self):
        """Test different measure types"""
        sleec_content = """
def_start
    event TestEvent
    measure boolMeasure: boolean
    measure numMeasure: numeric
    measure scaleMeasure: scale(low, medium, high)
def_end

rule_start
    R1 when TestEvent then TestEvent
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Check measure instantiation
        assert "{ holds_at(boolmeasure, T) }" in result
        assert f"{{ holds_at(nummeasure, V, T) : {DEFAULT_CONFIG.numeric_range} }}" in result
        assert "holds_at(scalemeasure, low, T)" in result

    # ========================================================================
    # UNLESS STATEMENT TESTS - TDD Implementation
    # ========================================================================

    def test_parse_simple_unless_statement(self):
        """Test parsing of simple unless statement"""
        sleec_content = """
def_start
    event MotionDetected
    event TurnOnLight
    event PlayJingle
    measure isDaytime: boolean
def_end

rule_start
    R1 when MotionDetected then TurnOnLight unless ({isDaytime}) then PlayJingle
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Should generate two separate rules with proper naming
        # Primary rule: R1_primary
        assert "exp(r1_primary)." in result
        assert "antecedent(r1_primary, T) :- happens(motiondetected, T, T), not holds_at(isdaytime, T), time(T)." in result
        assert "consequent(r1_primary, T) :- time(T), happens(turnonlight, T, T)." in result
        
        # Exception rule: R1_unless1
        assert "exp(r1_unless1)." in result
        assert "antecedent(r1_unless1, T) :- happens(motiondetected, T, T), holds_at(isdaytime, T), time(T)." in result
        assert "consequent(r1_unless1, T) :- time(T), happens(playjingle, T, T)." in result

    def test_parse_unless_with_negated_action(self):
        """Test parsing unless with 'not' action"""
        sleec_content = """
def_start
    event MotionDetected
    event TurnOnLight
    measure isDaytime: boolean
def_end

rule_start
    R1 when MotionDetected then TurnOnLight unless ({isDaytime}) then not TurnOnLight
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Primary rule: R1_primary
        assert "exp(r1_primary)." in result
        assert "antecedent(r1_primary, T) :- happens(motiondetected, T, T), not holds_at(isdaytime, T), time(T)." in result
        assert "consequent(r1_primary, T) :- time(T), happens(turnonlight, T, T)." in result
        
        # Exception rule should NOT exist for negated action
        assert "r1_unless1" not in result
        # Should not have any consequent that generates TurnOnLight when isDaytime is true
        lines = result.split('\n')
        invalid_consequent = any(
            "consequent(" in line and "happens(turnonlight, T)" in line and "holds_at(isdaytime, T)" in line 
            for line in lines
        )
        assert not invalid_consequent, "Should not generate consequent for 'not' unless clause"

    def test_parse_multiple_unless_statements(self):
        """Test parsing multiple unless statements (cascading priority)"""
        sleec_content = """
def_start
    event ButtonPress
    event TurnOnLight
    event PlaySound
    event ShowMessage
    measure powerSave: boolean
    measure emergencyMode: boolean
def_end

rule_start
    R1 when ButtonPress then TurnOnLight unless ({powerSave}) then PlaySound unless ({emergencyMode}) then ShowMessage
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Primary rule: ButtonPress AND NOT powerSave AND NOT emergencyMode -> TurnOnLight
        assert "exp(r1_primary)." in result
        assert "antecedent(r1_primary, T) :- happens(buttonpress, T, T), not holds_at(powersave, T), not holds_at(emergencymode, T), time(T)." in result
        assert "consequent(r1_primary, T) :- time(T), happens(turnonlight, T, T)." in result
        
        # First exception: ButtonPress AND powerSave AND NOT emergencyMode -> PlaySound  
        assert "exp(r1_unless1)." in result
        assert "antecedent(r1_unless1, T) :- happens(buttonpress, T, T), holds_at(powersave, T), not holds_at(emergencymode, T), time(T)." in result
        assert "consequent(r1_unless1, T) :- time(T), happens(playsound, T, T)." in result
        
        # Second exception: ButtonPress AND emergencyMode -> ShowMessage (highest priority)
        assert "exp(r1_unless2)." in result  
        assert "antecedent(r1_unless2, T) :- happens(buttonpress, T, T), holds_at(emergencymode, T), time(T)." in result
        assert "consequent(r1_unless2, T) :- time(T), happens(showmessage, T, T)." in result

    def test_unless_with_complex_conditions(self):
        """Test unless with complex boolean conditions"""
        sleec_content = """
def_start
    event DoorOpen
    event SoundAlarm
    event LogEntry
    measure isNight: boolean
    measure guestMode: boolean
def_end

rule_start
    R1 when (DoorOpen and {isNight}) then SoundAlarm unless ({guestMode}) then LogEntry
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Primary rule: DoorOpen AND isNight AND NOT guestMode -> SoundAlarm
        assert "exp(r1_primary)." in result
        assert "antecedent(r1_primary, T) :- happens(dooropen, T, T), holds_at(isnight, T), not holds_at(guestmode, T), time(T)." in result
        assert "consequent(r1_primary, T) :- time(T), happens(soundalarm, T, T)." in result
        
        # Exception rule: DoorOpen AND isNight AND guestMode -> LogEntry
        assert "exp(r1_unless1)." in result
        assert "antecedent(r1_unless1, T) :- happens(dooropen, T, T), holds_at(isnight, T), holds_at(guestmode, T), time(T)." in result
        assert "consequent(r1_unless1, T) :- time(T), happens(logentry, T, T)." in result

    def test_unless_conversion_simple(self):
        """Test conversion of simple unless to Clingo rules"""
        sleec_content = """
def_start
    event MotionDetected
    event TurnOnLight
    event PlayJingle
    measure isDaytime: boolean
def_end

rule_start
    R1 when MotionDetected then TurnOnLight unless ({isDaytime}) then PlayJingle
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Check domain definitions are present
        assert "event(motiondetected)" in result
        assert "event(turnonlight)" in result
        assert "event(playjingle)" in result
        assert "measure(isdaytime)" in result
        
        # Check rule structure exists
        assert "exp(r1_primary)" in result
        assert "exp(r1_unless1)" in result
        assert "antecedent(r1_primary, T)" in result
        assert "antecedent(r1_unless1, T)" in result
        assert "consequent(r1_primary, T)" in result
        assert "consequent(r1_unless1, T)" in result

    def test_unless_conversion_negated_action(self):
        """Test conversion of unless with negated action (no action generated)"""
        sleec_content = """
def_start
    event MotionDetected
    event TurnOnLight
    measure isDaytime: boolean
def_end

rule_start
    R1 when MotionDetected then TurnOnLight unless ({isDaytime}) then not TurnOnLight
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Primary rule should exist
        assert "exp(r1_primary)." in result
        assert "antecedent(r1_primary, T) :- happens(motiondetected, T, T), not holds_at(isdaytime, T), time(T)." in result
        assert "consequent(r1_primary, T) :- time(T), happens(turnonlight, T, T)." in result
        
        # Should NOT have r1_unless1 rule for negated action
        assert "exp(r1_unless1)" not in result

    def test_unless_conversion_cascading_priority(self):
        """Test conversion of multiple unless statements with cascading priority"""
        sleec_content = """
def_start
    event ButtonPress
    event TurnOnLight
    event PlaySound  
    event ShowMessage
    measure powerSave: boolean
    measure emergencyMode: boolean
def_end

rule_start
    R1 when ButtonPress then TurnOnLight unless ({powerSave}) then PlaySound unless ({emergencyMode}) then ShowMessage
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Check all three cascading rules exist with proper priority logic
        expected_rules = [
            "exp(r1_primary).",
            "antecedent(r1_primary, T) :- happens(buttonpress, T, T), not holds_at(powersave, T), not holds_at(emergencymode, T), time(T).",
            "consequent(r1_primary, T) :- time(T), happens(turnonlight, T, T).",
            "exp(r1_unless1).",
            "antecedent(r1_unless1, T) :- happens(buttonpress, T, T), holds_at(powersave, T), not holds_at(emergencymode, T), time(T).",
            "consequent(r1_unless1, T) :- time(T), happens(playsound, T, T).",
            "exp(r1_unless2).",
            "antecedent(r1_unless2, T) :- happens(buttonpress, T, T), holds_at(emergencymode, T), time(T).",
            "consequent(r1_unless2, T) :- time(T), happens(showmessage, T, T)."
        ]
        
        for expected_rule in expected_rules:
            assert expected_rule in result, f"Missing expected rule: {expected_rule}"

    def test_unless_integration_mixed_rules(self):
        """Test integration with mixed rules (some with unless, some without)"""
        sleec_content = """
def_start
    event MotionDetected
    event DoorOpen
    event TurnOnLight
    event SoundAlarm
    event PlayJingle
    measure isDaytime: boolean
    measure isLocked: boolean
def_end

rule_start
    R1 when MotionDetected then TurnOnLight unless ({isDaytime}) then PlayJingle
    R2 when DoorOpen and {isLocked} then SoundAlarm
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Unless rule (R1) - should generate two rules
        assert "exp(r1_primary)." in result
        assert "exp(r1_unless1)." in result
        assert "antecedent(r1_primary, T) :- happens(motiondetected, T, T), not holds_at(isdaytime, T), time(T)." in result
        assert "antecedent(r1_unless1, T) :- happens(motiondetected, T, T), holds_at(isdaytime, T), time(T)." in result
        
        # Regular rule (R2) - should generate one rule
        assert "exp(r2)." in result
        assert "antecedent(r2, T) :- happens(dooropen, T, T), holds_at(islocked, T), time(T)." in result
        assert "consequent(r2, T) :- time(T), happens(soundalarm, T, T)." in result

    def test_unless_regression_light_system(self):
        """Test unless with real-world light system example"""
        sleec_content = """
def_start
    event MotionDetected
    event TurnOnLight
    event PlayJingle
    measure isOccupied: boolean
    measure isDaytime: boolean
def_end

rule_start
    R1 when MotionDetected then TurnOnLight unless ({isDaytime}) then PlayJingle
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Based on sleec_files/uses_unless/light.sleec
        assert "exp(r1_primary)." in result
        assert "exp(r1_unless1)." in result
        assert "antecedent(r1_primary, T) :- happens(motiondetected, T, T), not holds_at(isdaytime, T), time(T)." in result
        assert "antecedent(r1_unless1, T) :- happens(motiondetected, T, T), holds_at(isdaytime, T), time(T)." in result

    def test_unless_error_handling_invalid_syntax(self):
        """Test error handling for invalid unless syntax"""
        invalid_sleec = """
def_start
    event TestEvent
def_end

rule_start
    R1 when TestEvent then Action unless invalid syntax here
rule_end
"""
        
        # Should raise appropriate parsing error
        with pytest.raises(Exception):  # Will be more specific once implemented
            result = self.converter.convert_sleec_string(invalid_sleec)

    def test_unless_action_choice_rules_generation(self):
        """Test that unless clause actions get choice rules generated - BUG REPRODUCTION"""
        sleec_content = """
def_start
    event MotionDetected
    event TurnOnLight  
    event PlayJingle
    measure isDaytime: boolean
def_end

rule_start
    R1 when MotionDetected then TurnOnLight unless ({isDaytime}) then PlayJingle
rule_end
"""
        
        result = self.converter.convert_sleec_string(sleec_content)
        
        # Check that BOTH primary and unless actions get choice rules
        assert "{ happens(turnonlight, T, T) } :- time(T)." in result, "Primary action should have choice rule"
        assert "{ happens(playjingle, T, T) } :- time(T)." in result, "Unless action should have choice rule - THIS IS THE BUG!"
        
        # Also check that both events are declared
        assert "event(turnonlight)." in result
        assert "event(playjingle)." in result
        
        # And both rules are generated 
        assert "exp(r1_primary)." in result
        assert "exp(r1_unless1)." in result

    def test_generate_unless_rules_comprehensive(self):
        """Test unless rule generation behavior before refactoring - BEHAVIOR CAPTURE"""
        from converter.parser import UnlessClause
        
        # Setup converter with events and measures
        self.converter.events = [Event("MotionDetected", 1), Event("TurnOnLight", 2), Event("PlayJingle", 3)]
        self.converter.measures = [Measure("isDaytime", MeasureType.BOOLEAN, 1)]
        
        # Create a rule with unless clause
        unless_clause = UnlessClause(condition="isDaytime", action="PlayJingle")
        rule = Rule("R1", "MotionDetected", "TurnOnLight", 1, unless_clauses=[unless_clause])
        
        # Test the unless rule generation
        rule_definitions = []
        self.converter._generate_unless_rules(rule, rule_definitions)
        
        # Verify the expected structure
        assert len(rule_definitions) >= 6, f"Expected at least 6 rule definitions, got {len(rule_definitions)}"
        
        # Check primary rule parts
        assert "exp(r1_primary)." in rule_definitions
        assert any("antecedent(r1_primary, T)" in rule_def for rule_def in rule_definitions)
        assert any("consequent(r1_primary, T)" in rule_def for rule_def in rule_definitions)
        
        # Check unless rule parts  
        assert "exp(r1_unless1)." in rule_definitions
        assert any("antecedent(r1_unless1, T)" in rule_def for rule_def in rule_definitions)
        assert any("consequent(r1_unless1, T)" in rule_def for rule_def in rule_definitions)
        
        # Verify complex antecedent logic (primary rule should negate unless condition)
        primary_antecedent = next((rule_def for rule_def in rule_definitions 
                                  if "antecedent(r1_primary, T)" in rule_def), None)
        assert primary_antecedent is not None
        assert "not isdaytime" in primary_antecedent, f"Primary antecedent missing negation: {primary_antecedent}"
        
        # Verify unless rule includes the unless condition
        unless_antecedent = next((rule_def for rule_def in rule_definitions 
                                 if "antecedent(r1_unless1, T)" in rule_def), None)  
        assert unless_antecedent is not None
        assert "isdaytime" in unless_antecedent, f"Unless antecedent missing condition: {unless_antecedent}"

    def test_convert_condition_to_antecedent_comprehensive(self):
        """Test comprehensive condition conversion behavior before refactoring - BEHAVIOR CAPTURE"""
        self.converter.events = [
            Event("MotionDetected", 1),
            Event("DoorOpen", 2), 
            Event("WithinEvent", 3)
        ]
        self.converter.measures = [Measure("isDaytime", MeasureType.BOOLEAN, 1)]
        
        # Mock within events (WithinEvent has within constraints)
        self.converter.rules = [Rule("R1", "WithinEvent", "SomeAction", 1, within_constraint="5 minutes")]
        
        # Test 1: Simple event
        result = self.converter._convert_condition_to_antecedent("MotionDetected")
        expected = "happens(motiondetected, T, T), time(T)"
        assert result == expected, f"Simple event: expected {expected}, got {result}"
        
        # Test 2: Event with measure
        result = self.converter._convert_condition_to_antecedent("MotionDetected and {isDaytime}")
        expected = "happens(motiondetected, T, T), holds_at(isdaytime, T), time(T)"
        assert result == expected, f"Event with measure: expected {expected}, got {result}"
        
        # Test 3: Complex condition with NOT
        result = self.converter._convert_condition_to_antecedent("DoorOpen and (not {isDaytime})")
        expected = "happens(dooropen, T, T), not holds_at(isdaytime, T), time(T)"
        assert result == expected, f"Complex with NOT: expected {expected}, got {result}"
        
        # Test 4: Within event (temporal) - Fix based on actual behavior
        result = self.converter._convert_condition_to_antecedent("WithinEvent")
        expected = "happens(withinevent, T, T), time(T)"  # Within events in conditions are still T,T
        assert result == expected, f"Within event: expected {expected}, got {result}"
        
        # Test 5: Mixed case conversion
        result = self.converter._convert_condition_to_antecedent("MotionDetected AND {isDaytime}")
        expected = "happens(motiondetected, T, T), holds_at(isdaytime, T), time(T)"
        assert result == expected, f"Mixed case: expected {expected}, got {result}"


# ========================================================================
# TEST UTILITIES
# ========================================================================

class TestUtils:
    """Utility functions for testing"""
    
    @staticmethod
    def run_clingo_on_result(clingo_code, models=None):
        """Run clingo on generated code and return models"""
        if models is None:
            models = DEFAULT_CONFIG.utility_test_models
            
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.lp', delete=False) as f:
                f.write(clingo_code)
                temp_file = f.name
            
            result = subprocess.run(['clingo', temp_file, f'--models={models}'], 
                                  capture_output=True, text=True)
            
            os.unlink(temp_file)
            
            if result.returncode != 10:  # 10 is SAT in clingo
                return None, result.stderr
            
            return result.stdout, None
            
        except Exception as e:
            return None, str(e)
    
    @staticmethod
    def validate_rule_compliance(models_output, rules):
        """Validate that models comply with SLEEC rules"""
        # This would implement detailed model checking logic
        # For now, just check that we have valid models
        return "SATISFIABLE" in models_output


# ========================================================================
# PYTEST CONFIGURATION AND FIXTURES
# ========================================================================

@pytest.fixture
def sample_sleec_files():
    """Fixture providing sample SLEEC files for testing"""
    return {
        'simple': """
def_start
    event ButtonPress
    event LightOn
def_end

rule_start
    R1 when ButtonPress then LightOn
rule_end
""",
        'complex': """
def_start
    event EncounterHuman
    event InformHuman
    event IdentifyActivity
    measure sameLanguage: boolean
    measure humanUnderstands: boolean
def_end

rule_start
    R1 when EncounterHuman and ({sameLanguage} and {humanUnderstands}) then InformHuman
    R2 when EncounterHuman then IdentifyActivity
rule_end
"""
    }


if __name__ == "__main__":
    # Allow running tests directly
    pytest.main([__file__, "-v"]) 