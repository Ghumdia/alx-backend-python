#!/usr/bin/env python3
"""
Import Union from the typing module
"""
from typing import Union
from typing import Tuple
"""
Function returns a tuble consisting of two data types
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes two arguments and returns them in a tuple
    """
    return (k, v**2)
