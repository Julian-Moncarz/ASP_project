# SLEEC Converter Package
"""
Package for converting SLEEC rules to different Clingo formats.

Available converters:
- SleecToClingoConverter: Original converter following ASPEN.lp style
- CorrectSleecConverter: Dalal's approach with antecedent/consequent structure
"""

from .sleec_to_clingo_converter import SleecToClingoConverter
from .correct_sleec_converter import CorrectSleecConverter

__all__ = ['SleecToClingoConverter', 'CorrectSleecConverter'] 