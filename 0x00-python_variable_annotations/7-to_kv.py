#!/usr/bin/env python3
"""
This module contains a function returns a tuple
of string and square of int/float number.
"""


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes two variables and return tuple of string and float.

    Args:
        k (str): Any string.
        v (Union[int, float]): Integer of float number.

    Returns:
        Tuple[str, float]: Tuple of string and float number.
    """
    x: Tuple[str, float] = (k, v ** 2)
    return x
