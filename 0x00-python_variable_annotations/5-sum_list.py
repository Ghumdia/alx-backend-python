#!/usr/bin/env python3
"""
Imports list type from typing module
"""
from typing import List
"""
Functions returns a float of all added float numbers in a list
"""


def sum_list(input_list: List) -> float:
    """
    Takes one argument which is a list and returns a float
    """
    k = 0
    for i in input_list:
        k += i
    return k
