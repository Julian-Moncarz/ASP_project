#!/usr/bin/env python3
"""
SLEEC to Clingo Converter Exceptions
===================================

Custom exception hierarchy for better error handling and debugging.
"""

from typing import Optional, List, Any


class SleecError(Exception):
    """Base exception for all SLEEC-related errors"""
    
    def __init__(self, message: str, line_number: Optional[int] = None, 
                 context: Optional[str] = None):
        self.message = message
        self.line_number = line_number
        self.context = context
        super().__init__(self._format_message())
    
    def _format_message(self) -> str:
        """Format the error message with context"""
        msg = self.message
        if self.line_number:
            msg = f"Line {self.line_number}: {msg}"
        if self.context:
            msg = f"{msg}\nContext: {self.context}"
        return msg


class SleecParseError(SleecError):
    """Raised when SLEEC parsing fails"""
    
    def __init__(self, message: str, line_number: Optional[int] = None,
                 context: Optional[str] = None, expected: Optional[str] = None):
        self.expected = expected
        super().__init__(message, line_number, context)
    
    def _format_message(self) -> str:
        msg = super()._format_message()
        if self.expected:
            msg = f"{msg}\nExpected: {self.expected}"
        return msg


class SleecConversionError(SleecError):
    """Raised when SLEEC to Clingo conversion fails"""
    
    def __init__(self, message: str, rule_id: Optional[str] = None,
                 line_number: Optional[int] = None, context: Optional[str] = None):
        self.rule_id = rule_id
        super().__init__(message, line_number, context)
    
    def _format_message(self) -> str:
        msg = super()._format_message()
        if self.rule_id:
            msg = f"Rule {self.rule_id}: {msg}"
        return msg


class SleecValidationError(SleecError):
    """Raised when SLEEC validation fails"""
    
    def __init__(self, message: str, violations: Optional[List[str]] = None,
                 line_number: Optional[int] = None, context: Optional[str] = None):
        self.violations = violations or []
        super().__init__(message, line_number, context)
    
    def _format_message(self) -> str:
        msg = super()._format_message()
        if self.violations:
            violations_str = "\n".join(f"  - {v}" for v in self.violations)
            msg = f"{msg}\nValidation violations:\n{violations_str}"
        return msg


class ConfigurationError(SleecError):
    """Raised when configuration is invalid"""
    
    def __init__(self, message: str, parameter: Optional[str] = None,
                 value: Optional[Any] = None):
        self.parameter = parameter
        self.value = value
        super().__init__(message)
    
    def _format_message(self) -> str:
        msg = self.message
        if self.parameter:
            msg = f"Configuration parameter '{self.parameter}': {msg}"
        if self.value is not None:
            msg = f"{msg} (value: {self.value})"
        return msg


class ClingoExecutionError(SleecError):
    """Raised when Clingo execution fails"""
    
    def __init__(self, message: str, clingo_output: Optional[str] = None,
                 return_code: Optional[int] = None):
        self.clingo_output = clingo_output
        self.return_code = return_code
        super().__init__(message)
    
    def _format_message(self) -> str:
        msg = self.message
        if self.return_code is not None:
            msg = f"{msg} (exit code: {self.return_code})"
        if self.clingo_output:
            msg = f"{msg}\nClingo output:\n{self.clingo_output}"
        return msg 