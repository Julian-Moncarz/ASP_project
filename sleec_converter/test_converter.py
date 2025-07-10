#!/usr/bin/env python3
"""
Test script for the SLEEC to Clingo converter
"""

from .sleec_to_clingo_converter import SleecToClingoConverter
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python test_converter.py <sleec_file>")
        print("\nAvailable SLEEC files:")
        print("- sleec_test_examples/access_control_rules.sleec")
        print("- sleec_test_examples/light_switch_rules.sleec")
        print("- sleec_test_examples/conflicting_rules_heater.sleec")
        print("- Simple conflict detection/access_control.sleec")
        return
    
    sleec_file = sys.argv[1]
    
    try:
        converter = SleecToClingoConverter()
        clingo_code = converter.convert_file(sleec_file)
        
        # Output to a .lp file
        output_file = sleec_file.replace('.sleec', '_generated.lp')
        with open(output_file, 'w') as f:
            f.write(clingo_code)
        
        print(f"Successfully converted {sleec_file} to {output_file}")
        print("\n" + "="*50)
        print("Generated Clingo code:")
        print("="*50)
        print(clingo_code)
        
    except Exception as e:
        print(f"Error converting {sleec_file}: {e}")
        return 1

if __name__ == "__main__":
    main() 