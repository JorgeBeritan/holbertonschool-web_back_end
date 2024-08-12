#!/usr/bin/env python3
"""
    Made By Me
"""


from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Parameters:
    lst(Iterable[Sequence]): first argument

    Return:
    List[Tuple[Sequence, int]]: length
    """
    return [(i, len(i)) for i in lst]
