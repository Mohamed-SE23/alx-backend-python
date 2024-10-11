#!/usr/bin/env python3
"""
This module contains a function for handling
a list of float numbers and return there sum.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of float numbers.

    Args:
        input_list (list[float]): List of float numbers.

    Returns:
        float: The sum of input_list.
    """
    return sum(input_list)
