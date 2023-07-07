#!/usr/bin/env python3
"""
Importing functions from the typing module
"""
from typing import Sequence, Union, Any
"""
Function takes any type of data type
"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    takes one argument which is a list with unknown
    elements
    """
    if lst:
        return lst[0]
    else:
        return None
