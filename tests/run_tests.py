#!/usr/bin/env python3
"""
Test Runner for SLEEC to Clingo Converter
=========================================

This script provides a way to run tests with pytest.
It can run individual test categories or the full test suite.

Usage:
    python run_tests.py [category]
    
Categories:
    unit        - Unit tests only
    integration - Integration tests only  
    behavioral  - Behavioral tests only
    regression  - Regression tests only
    all         - All tests (default)
"""

import sys
import os
import subprocess
from pathlib import Path

def check_pytest_available():
    """Check if pytest is available"""
    try:
        import pytest
        return True
    except ImportError:
        return False

def run_pytest_command(test_filter="", verbose=True):
    """Run pytest with specified filter"""
    cmd = ["python", "-m", "pytest"]
    
    if verbose:
        cmd.append("-v")
    
    if test_filter:
        cmd.extend(["-k", test_filter])
    
    cmd.append("test_converter.py")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=Path(__file__).parent)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error running pytest: {e}")
        return False

def run_unit_tests():
    """Run unit tests"""
    print("🧪 Running Unit Tests...")
    
    # Unit test method names
    unit_test_filter = "test_convert_condition_to_antecedent or test_remove_logical_grouping_parentheses or test_get_triggering_events or test_get_action_events"
    return run_pytest_command(unit_test_filter)

def run_integration_tests():
    """Run integration tests"""
    print("🔗 Running Integration Tests...")
    
    integration_test_filter = "test_convert_sleec_string or test_syntax_validation"
    return run_pytest_command(integration_test_filter)

def run_behavioral_tests():
    """Run behavioral tests"""
    print("🎯 Running Behavioral Tests...")
    
    behavioral_test_filter = "test_rule_compliance or test_choice_rules or test_multiple_rules_interaction"
    return run_pytest_command(behavioral_test_filter)

def run_regression_tests():
    """Run regression tests"""
    print("🔄 Running Regression Tests...")
    
    regression_test_filter = "test_door_system_regression or test_lightswitch_system_regression or test_aspen_system_regression"
    return run_pytest_command(regression_test_filter)

def run_all_tests():
    """Run all test categories"""
    print("🚀 Running All Tests...")
    
    # Run all tests without filter
    return run_pytest_command("")

def main():
    """Main test runner"""
    category = sys.argv[1] if len(sys.argv) > 1 else 'all'
    
    print(f"SLEEC to Clingo Converter Test Suite")
    print(f"===================================")
    print(f"Running category: {category}")
    print()
    
    # Check if pytest is available
    if not check_pytest_available():
        print("❌ pytest not available. Install with: pip install pytest")
        print("💡 Try running: pip install -r tests/requirements.txt")
        sys.exit(1)
    
    if category == 'unit':
        success = run_unit_tests()
    elif category == 'integration':
        success = run_integration_tests()
    elif category == 'behavioral':
        success = run_behavioral_tests()
    elif category == 'regression':
        success = run_regression_tests()
    elif category == 'all':
        success = run_all_tests()
    else:
        print(f"❌ Unknown category: {category}")
        print("Available categories: unit, integration, behavioral, regression, all")
        sys.exit(1)
    
    if success:
        print("\n✅ All tests completed successfully!")
    else:
        print("\n❌ Some tests failed")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 