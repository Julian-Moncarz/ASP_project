#!/usr/bin/env python3
"""
Batch SLEEC to Clingo converter
Converts all SLEEC files in specified directories
"""

import os
import glob
from .sleec_to_clingo_converter import SleecToClingoConverter

def convert_all_in_directory(directory):
    """Convert all .sleec files in a directory"""
    sleec_files = glob.glob(os.path.join(directory, "*.sleec"))
    
    if not sleec_files:
        print(f"No .sleec files found in {directory}")
        return
    
    print(f"Found {len(sleec_files)} SLEEC files in {directory}")
    
    converter = SleecToClingoConverter()
    
    for sleec_file in sleec_files:
        try:
            print(f"\nConverting {sleec_file}...")
            clingo_code = converter.convert_file(sleec_file)
            
            # Generate output filename
            output_file = sleec_file.replace('.sleec', '_auto_generated.lp')
            
            with open(output_file, 'w') as f:
                f.write(clingo_code)
            
            print(f"✓ Generated: {output_file}")
            
        except Exception as e:
            print(f"✗ Error converting {sleec_file}: {e}")

def main():
    """Convert all SLEEC files in the project"""
    directories = [
        "sleec_test_examples",
        "Simple conflict detection",
        "conflicting SLEEC examples"
    ]
    
    print("SLEEC to Clingo Batch Converter")
    print("=" * 40)
    
    total_converted = 0
    
    for directory in directories:
        if os.path.exists(directory):
            print(f"\n📁 Processing directory: {directory}")
            sleec_files = glob.glob(os.path.join(directory, "*.sleec"))
            
            if sleec_files:
                converter = SleecToClingoConverter()
                
                for sleec_file in sleec_files:
                    try:
                        print(f"  Converting {os.path.basename(sleec_file)}...", end=" ")
                        clingo_code = converter.convert_file(sleec_file)
                        
                        output_file = sleec_file.replace('.sleec', '_auto_generated.lp')
                        
                        with open(output_file, 'w') as f:
                            f.write(clingo_code)
                        
                        print("✓")
                        total_converted += 1
                        
                    except Exception as e:
                        print(f"✗ ({e})")
            else:
                print(f"  No .sleec files found")
        else:
            print(f"\n⚠️  Directory not found: {directory}")
    
    print(f"\n🎉 Conversion complete! {total_converted} files converted.")
    print(f"\nGenerated files have the suffix '_auto_generated.lp'")
    
    # Show example usage
    if total_converted > 0:
        print(f"\nTo test the generated files with Clingo:")
        print(f"  clingo <generated_file>.lp")
        print(f"  clingo <generated_file>.lp --models=0  # Show all models")

if __name__ == "__main__":
    main() 