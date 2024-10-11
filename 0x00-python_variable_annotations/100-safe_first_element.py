#!/usr/bin/env python3
"""
This module contains a function holding
a variable with syquence type and return
the first element in the list or None.
"""


from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of the list if it exists, otherwise None.

    Args:
        lst (Sequence[Any]): A sequence (e.g., list, tuple) that can
        contain elements of any type.

    Returns:
        Optional[Any]: The first element of the sequence or None
        if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
