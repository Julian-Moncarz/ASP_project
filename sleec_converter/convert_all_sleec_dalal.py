#!/usr/bin/env python3
"""
Convert All SLEEC Files to Clingo (Dalal's Format)
=================================================

This script finds all .sleec files in the project and converts them to 
Clingo format using Dalal's approach with antecedent/consequent structure
and rule satisfaction logic.

Usage:
    python convert_all_sleec_dalal.py

This will:
1. Find all .sleec files in the project directories
2. Convert each to Clingo format using CorrectSleecConverter
3. Save the output as {filename}_dalal.lp
4. Create a summary report

The script looks for SLEEC files in:
- sleec_test_examples/
- conflicting SLEEC examples/
- Simple conflict detection/
- Dalal's_way-implimentations/
- small_example/
- Any other directories with .sleec files
"""

import os
import sys
from pathlib import Path
from correct_sleec_converter import CorrectSleecConverter

def find_sleec_files(base_dir: str = "..") -> list:
    """Find all .sleec files in the project"""
    base_path = Path(base_dir)
    sleec_files = []
    
    # Search for .sleec files recursively
    for sleec_file in base_path.rglob("*.sleec"):
        sleec_files.append(sleec_file)
    
    return sorted(sleec_files)

def convert_sleec_file(sleec_path: Path, converter: CorrectSleecConverter) -> tuple:
    """Convert a single SLEEC file and return (success, output_path, error_msg)"""
    try:
        print(f"Converting {sleec_path}...")
        
        # Generate output filename
        output_path = sleec_path.parent / (sleec_path.stem + '_dalal.lp')
        
        # Convert the file
        clingo_code = converter.convert_file(str(sleec_path))
        
        # Write the output
        with open(output_path, 'w') as f:
            f.write(clingo_code)
        
        print(f"  → {output_path}")
        return True, output_path, None
        
    except Exception as e:
        error_msg = f"Error converting {sleec_path}: {str(e)}"
        print(f"  ✗ {error_msg}")
        return False, None, error_msg

def main():
    """Main conversion function"""
    print("SLEEC to Clingo Converter (Dalal's Format)")
    print("=" * 50)
    
    # Initialize converter
    converter = CorrectSleecConverter(max_time=10)
    
    # Find all SLEEC files
    sleec_files = find_sleec_files()
    
    if not sleec_files:
        print("No .sleec files found in the project.")
        return
    
    print(f"Found {len(sleec_files)} SLEEC files:")
    for f in sleec_files:
        print(f"  - {f}")
    print()
    
    # Convert each file
    successful_conversions = []
    failed_conversions = []
    
    for sleec_file in sleec_files:
        success, output_path, error = convert_sleec_file(sleec_file, converter)
        
        if success:
            successful_conversions.append((sleec_file, output_path))
        else:
            failed_conversions.append((sleec_file, error))
    
    # Print summary
    print("\n" + "=" * 50)
    print("CONVERSION SUMMARY")
    print("=" * 50)
    
    print(f"✓ Successfully converted: {len(successful_conversions)} files")
    for sleec_file, output_path in successful_conversions:
        print(f"  {sleec_file.name} → {output_path.name}")
    
    if failed_conversions:
        print(f"\n✗ Failed conversions: {len(failed_conversions)} files")
        for sleec_file, error in failed_conversions:
            print(f"  {sleec_file.name}: {error}")
    
    print(f"\nTotal files processed: {len(sleec_files)}")
    print(f"Success rate: {len(successful_conversions)}/{len(sleec_files)} ({len(successful_conversions)/len(sleec_files)*100:.1f}%)")

if __name__ == "__main__":
    main() 