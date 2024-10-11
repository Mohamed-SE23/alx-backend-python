#!/usr/bin/env python3
"""
This module contains a function that 'zooms in'
on elements of a tuple by repeating them.
"""


from typing import List, Tuple, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms in on elements of a tuple by repeating them a number of times.

    Args:
        lst (Tuple[int, ...]): The input tuple.
        factor (int, optional): The number of times each
        element is repeated. Defaults to 2.

    Returns:
        List[int]: A list with elements repeated according to the factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)


zoom_2x = zoom_array(array)


zoom_3x = zoom_array(array, 3)
