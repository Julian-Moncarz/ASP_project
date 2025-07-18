#!/usr/bin/env python3
"""
Test Runner for SLEEC to Clingo Converter
==========================================

Runs test cases and compares output with expected results.
For TDD: should show RED (failing) tests before implementation.
"""

import sys
import os
import subprocess
from pathlib import Path

def run_converter_on_test(test_file):
    """Run converter on a test file and return the output"""
    try:
        result = subprocess.run([
            sys.executable, 'converter.py', str(test_file)
        ], capture_output=True, text=True, cwd='.')
        
        if result.returncode != 0:
            return None, result.stderr
        
        # Read the generated output file
        output_file = test_file.with_name(test_file.stem + '_converted.lp')
        if output_file.exists():
            with open(output_file, 'r') as f:
                return f.read(), None
        else:
            return None, "No output file generated"
            
    except Exception as e:
        return None, str(e)

def compare_with_expected(actual, expected_file):
    """Compare actual output with expected output"""
    if not expected_file.exists():
        return False, f"Expected output file {expected_file} does not exist"
    
    with open(expected_file, 'r') as f:
        expected = f.read()
    
    # Handle case where actual is None (converter failure)
    if actual is None:
        return False, "Converter failed to produce output"
    
    if actual.strip() == expected.strip():
        return True, "PASS"
    else:
        return False, f"Output differs from expected"

def run_tests():
    """Run all tests and report results"""
    test_dirs = [
        'tests/test_cases/simple',
        'tests/test_cases/regression', 
        'tests/test_cases/within'
    ]
    
    total_tests = 0
    passed_tests = 0
    failed_tests = 0
    
    print("🧪 Running SLEEC Converter Tests (TDD Mode)")
    print("=" * 50)
    
    for test_dir in test_dirs:
        test_path = Path(test_dir)
        if not test_path.exists():
            continue
            
        print(f"\n📁 {test_dir}")
        print("-" * 30)
        
        for test_file in test_path.glob("*.sleec"):
            total_tests += 1
            
            # Determine expected output file
            expected_path = Path(f"tests/expected_outputs/{test_path.name}/{test_file.stem}.lp")
            
            print(f"  🔍 {test_file.name}...", end=" ")
            
            # Run converter
            actual_output, error = run_converter_on_test(test_file)
            
            if error:
                print(f"❌ FAIL - Converter error: {error}")
                failed_tests += 1
                continue
            
            # Compare with expected
            matches, message = compare_with_expected(actual_output, expected_path)
            
            if matches:
                print(f"✅ PASS")
                passed_tests += 1
            else:
                print(f"❌ FAIL - {message}")
                failed_tests += 1
                
                # Show diff for output mismatches
                if actual_output and expected_path.exists() and "differs from expected" in message:
                    print(f"    Expected file: {expected_path}")
                    print(f"    Generated vs Expected (first 200 chars):")
                    with open(expected_path, 'r') as f:
                        expected_content = f.read()
                    print(f"    Generated: {actual_output[:200]}...")
                    print(f"    Expected:  {expected_content[:200]}...")
    
    print(f"\n🎯 Test Summary")
    print("=" * 50)
    print(f"Total tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    
    if failed_tests > 0:
        print(f"\n🔴 RED PHASE: {failed_tests} tests failing - ready to implement!")
        return 1
    else:
        print(f"\n🟢 GREEN PHASE: All tests passing!")
        return 0

if __name__ == "__main__":
    sys.exit(run_tests()) 