#!/usr/bin/env python3
"""
Importing a datatype from the typing module
"""
from typing import Union
from typing import List
"""
Function returns a float
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes one argument which is a list
    Returns a float
    """
    k = 0
    for i in mxd_lst:
        k += i
    return k
