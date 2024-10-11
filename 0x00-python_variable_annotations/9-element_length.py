#!/usr/bin/env python3
"""
This module contains a function that returns a list
of tuples with elements and their lengths.
"""


from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains
    a sequence and its length.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences
        (e.g., list of strings, lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with
        each sequence and its length.
    """
    return [(i, len(i)) for i in lst]
