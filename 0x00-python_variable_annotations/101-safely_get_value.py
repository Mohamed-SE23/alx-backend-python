#!/usr/bin/env python3
"""
This module contains a function that safely
retreve a value from a dectionary.
"""


from typing import Any, TypeVar, Mapping, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary. If the key is not found,
    it returns the default value.

    Args:
        dct (Mapping[Any, T]): The dictionary from which to get the value.
        key (Any): The key to look up in the dictionary.
        default (Optional[T]): The default value to return if the key
        is not found. Defaults to None.

    Returns:
        Optional[T]: The value from the dictionary or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
