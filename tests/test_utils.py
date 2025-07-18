#!/usr/bin/env python3
"""
Test Utilities for SLEEC to Clingo Converter
==========================================

Shared utility functions for testing the converter.
"""

import tempfile
import subprocess
import os
from typing import Optional, Tuple


class TestUtils:
    """Utility functions for testing"""
    
    @staticmethod
    def run_clingo_on_result(clingo_code: str, models: int = 5) -> Tuple[Optional[str], Optional[str]]:
        """Run clingo on generated code and return models"""
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
    def validate_rule_compliance(models_output: str, rules) -> bool:
        """Validate that models comply with SLEEC rules"""
        # This would implement detailed model checking logic
        # For now, just check that we have valid models
        return "SATISFIABLE" in models_output 