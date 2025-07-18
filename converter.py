#!/usr/bin/env python3
"""
SLEEC to Clingo Converter Entry Script
=====================================

Converts SLEEC files to Clingo format using an antecedent/consequent approach.

Usage:
    python converter.py <input.sleec> [output.lp]

Example:
    python converter.py sleec_files/simple_rules/lightswitch.sleec
"""

import sys
import os
from pathlib import Path

from converter import SleecToClingoConverter, DEFAULT_CONFIG

def main():
    if len(sys.argv) < 2:
        print("❌ Error: Please provide a SLEEC file to convert")
        print()
        print("Usage:")
        print(f"  python {sys.argv[0]} <input.sleec> [output.lp]")
        print()
        print("Example:")
        print(f"  python {sys.argv[0]} sleec_files/simple_rules/lightswitch.sleec")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Generate output filename if not provided
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        # Replace .sleec with _converted.lp
        input_path = Path(input_file)
        output_file = str(input_path.with_name(input_path.stem + '_converted.lp'))
    
    try:
        # Convert the file
        converter = SleecToClingoConverter()
        clingo_code = converter.convert_file(input_file)
        
        # Write output
        with open(output_file, 'w') as f:
            f.write(clingo_code)
        
        print(f"✅ Successfully converted: {input_file} → {output_file}")
        print()
        print("To run the generated file:")
        print(f"  clingo {output_file} {DEFAULT_CONFIG.clingo_suggestion} or however many models you want")
        
    except FileNotFoundError:
        print(f"❌ Error: Input file '{input_file}' not found")
        sys.exit(1)
    except ValueError as e:
        print(f"❌ Conversion failed:")
        print(str(e))
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 