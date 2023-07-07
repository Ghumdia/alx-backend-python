#!/usr/bin/env python3
"""
Importing functions from the typing module
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')

"""
Function
"""


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    Function that takes three argument
    """
    if key in dct:
        return dct[key]
    else:
        return default
