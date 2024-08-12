#!/usr/bin/env python3
"""
    Make By Me
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Parameters:
    multiplier(float): the first argument

    Returns:
    float: a multiplication
    """
    def multiplier_function(x: float) -> float:
        """
        Parameters:
        x(float): the first argument

        Return:
        float: return a multiplier
        """
        return x * multiplier
    return multiplier_function
