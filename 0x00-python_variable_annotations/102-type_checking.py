#!/usr/bin/env python3
"""
Importing functions from typing module
"""
from typing import Tuple, List
"""
Function returns a list
"""


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Takes two positional arguments
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
