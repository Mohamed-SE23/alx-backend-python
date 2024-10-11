#!/usr/bin/env python3
"""
This module contains a function for handling
a mixed list of floats and integers
numbers and return there sum.
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns the sum of float and integer numbers.

    Args:
        mxd_list (list[Union[int, float]]): List of float and int.

    Returns:
        float: The sum of mxd_list.
    """
    return sum(mxd_list)
