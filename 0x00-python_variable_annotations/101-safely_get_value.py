#!/usr/bin/python3
"""
Importing functions from the typing module
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')

"""
Function 
"""


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, Any]:
    """
    Function that takes three argument
    """
    if key in dct:
        return dct[key]
    else:
        return default
