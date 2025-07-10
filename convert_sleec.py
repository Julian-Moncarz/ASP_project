#!/usr/bin/env python3
"""
Main script to convert SLEEC files to Clingo format
Usage from project root directory
"""

import sys
import os
from sleec_converter import SleecToClingoConverter

def main():
    if len(sys.argv) < 2:
        print("SLEEC to Clingo Converter")
        print("=" * 40)
        print("Usage:")
        print("  python3 convert_sleec.py <sleec_file>           # Convert single file")
        print("  python3 convert_sleec.py --all                  # Convert all SLEEC files")
        print("")
        print("Available SLEEC files:")
        print("- sleec_test_examples/access_control_rules.sleec")
        print("- sleec_test_examples/light_switch_rules.sleec")  
        print("- sleec_test_examples/conflicting_rules_heater.sleec")
        print("- Simple conflict detection/access_control.sleec")
        print("- conflicting SLEEC examples/*.sleec")
        return
    
    if sys.argv[1] == "--all":
        # Batch convert all files
        from sleec_converter.convert_all_sleec import main as batch_main
        batch_main()
        return
    
    # Convert single file
    sleec_file = sys.argv[1]
    
    if not os.path.exists(sleec_file):
        print(f"Error: File '{sleec_file}' not found")
        return 1
    
    try:
        converter = SleecToClingoConverter()
        clingo_code = converter.convert_file(sleec_file)
        
        # Output to a .lp file
        output_file = sleec_file.replace('.sleec', '_converted.lp')
        with open(output_file, 'w') as f:
            f.write(clingo_code)
        
        print(f"✓ Successfully converted: {sleec_file} → {output_file}")
        print(f"\nTo test with Clingo:")
        print(f"  clingo {output_file} --models=3")
        
    except Exception as e:
        print(f"✗ Error converting {sleec_file}: {e}")
        return 1

if __name__ == "__main__":
    main() 