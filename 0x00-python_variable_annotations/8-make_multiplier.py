#!/usr/bin/env python3
"""
This module contains a function for handling
a float number and returns a multiplier for it.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Multipling a given float number.

    Args:
        multiplier (float): A float number to be multiplied.

    Returns:
        Callable[[float], float]: A float multiplied number.
    """
    return lambda x: x * multiplier
