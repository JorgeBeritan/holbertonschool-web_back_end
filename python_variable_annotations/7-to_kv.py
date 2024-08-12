#!/usr/bin/env python3
"""
    Made By Me
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Parameters:
    k(str): The first argument
    v(List[Union[int, float]]): The second argument

    Return:
    tuple: return a representation of a tuple
    """
    return (str(k), float(v ** 2))
