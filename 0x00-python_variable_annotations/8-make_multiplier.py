#!/usr/bin/env python3
"""
Importing a function from the typing module
"""
from typing import Callable
"""
Function that takes a function and returns a float
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function
    """
    def mul_func(num: float) -> float:
        """
        Multiplies a number by anothe float num ber
        """
        return num * multiplier
    return mul_func
