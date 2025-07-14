"""
SLEEC to Clingo Converters Package
=================================

This package contains SLEEC to Clingo converters and shared parsing utilities.

Available converters:
- SleecToClingoConverter: Original converter (direct rule translation)
- CorrectSleecConverter: Dalal's converter (antecedent/consequent structure)

Shared utilities:
- SleecParser: Shared SLEEC parsing functionality
- Data classes: Event, Measure, Constant, Rule, MeasureType
"""

from .parser import SleecParser, MeasureType, Measure, Event, Constant, Rule
from .original import SleecToClingoConverter
from .dalal import CorrectSleecConverter

__all__ = [
    'SleecParser',
    'MeasureType', 
    'Measure',
    'Event', 
    'Constant',
    'Rule',
    'SleecToClingoConverter',
    'CorrectSleecConverter'
] 