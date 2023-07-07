#!/usr/bin/env python3
"""
Imports multiple functions from the typing module
"""
from typing import Iterable, Sequence, List, Tuple
"""
Function that returns a List
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes on argument and returns a list
    """
    return [(i, len(i)) for i in lst]
