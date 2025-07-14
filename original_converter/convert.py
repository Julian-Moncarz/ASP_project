#!/usr/bin/env python3
"""
Original SLEEC to Clingo Converter
=================================

Usage:
    python3 convert.py <sleec_file>       
"""

import sys
import os
from sleec_to_clingo_converter import SleecToClingoConverter

def main():
    if len(sys.argv) != 2:
        print("Original SLEEC to Clingo Converter")
        print("=" * 40)
        print("Usage:")
        print("  python3 convert.py <sleec_file>")
        return
    
    sleec_file = sys.argv[1]
    
    if not os.path.exists(sleec_file):
        print(f"Error: File '{sleec_file}' not found")
        return 1
    
    try:
        converter = SleecToClingoConverter()
        clingo_code = converter.convert_file(sleec_file)
        
        # Output to a .lp file
        output_file = sleec_file.replace('.sleec', '_original.lp')
        with open(output_file, 'w') as f:
            f.write(clingo_code)
        
        print(f"✅ Successfully converted: {sleec_file} → {output_file}")
        print(f"\nTo run the generated file:")
        print(f"  clingo {output_file} --models=3  or however many models you want")
        
    except Exception as e:
        print(f"❌ Error converting {sleec_file}: {e}")
        return 1

if __name__ == "__main__":
    main() 