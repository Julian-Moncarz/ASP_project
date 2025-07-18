#!/usr/bin/env python3
"""
SLEEC to Clingo Converter Configuration
======================================

This module contains configuration settings for the SLEEC to Clingo converter,
centralizing all configuration values in one place for better maintainability.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ConverterConfig:
    """Configuration settings for the SLEEC to Clingo converter"""
    
    # Time domain configuration
    max_time: int = 10
    """Maximum time value for the time domain (generates time(0..max_time))"""
    
    # Numeric measure configuration  
    numeric_min: int = 0
    numeric_max: int = 10
    """Range for numeric measures (generates V = numeric_min..numeric_max)"""
    
    # Clingo execution configuration
    default_models: int = 3
    """Default number of models to suggest when running clingo"""
    
    test_models: int = 1  
    """Number of models to use for syntax validation testing"""
    
    test_time_limit: int = 5
    """Time limit in seconds for clingo syntax validation"""
    
    test_timeout: int = 10
    """Timeout in seconds for Python subprocess calls to clingo"""
    
    utility_test_models: int = 5
    """Default number of models for test utility functions"""
    
    # Output formatting configuration
    show_predicates: Optional[List[str]] = None
    """List of predicates to show in clingo output"""
    
    # Template configuration
    section_separator: str = "\n\n"
    """Separator between generated code sections"""
    
    def __post_init__(self):
        """Initialize default values that can't be set in field defaults"""
        if self.show_predicates is None:
            self.show_predicates = ["holds_at/2", "happens/3"]
    
    @property
    def time_domain(self) -> str:
        """Generate the time domain string"""
        return f"time(0..{self.max_time})."
    
    @property 
    def numeric_range(self) -> str:
        """Generate the numeric range string for measures"""
        return f"V = {self.numeric_min}..{self.numeric_max}"
    
    @property
    def clingo_suggestion(self) -> str:
        """Generate the clingo command suggestion string"""
        return f"--models={self.default_models}"
    
    @classmethod
    def create_default(cls) -> "ConverterConfig":
        """Create a default configuration instance"""
        return cls()
    
    @classmethod
    def create_test_config(cls) -> "ConverterConfig":
        """Create a configuration optimized for testing"""
        return cls(
            max_time=5,  # Smaller time domain for faster tests
            numeric_max=5,  # Smaller numeric range for faster tests
            test_time_limit=3,  # Faster timeout for tests
            test_timeout=5  # Faster subprocess timeout
        )
    
    def validate(self) -> None:
        """Validate configuration values"""
        if self.max_time < 0:
            raise ValueError("max_time must be non-negative")
        
        if self.numeric_min > self.numeric_max:
            raise ValueError("numeric_min must be <= numeric_max")
        
        if self.default_models < 0:
            raise ValueError("default_models must be non-negative")
        
        if self.test_time_limit <= 0:
            raise ValueError("test_time_limit must be positive")
        
        if self.test_timeout <= 0:
            raise ValueError("test_timeout must be positive")


# Global default configuration instance
DEFAULT_CONFIG = ConverterConfig.create_default() 