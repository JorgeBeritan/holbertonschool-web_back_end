#!/usr/bin/env python3
"""
    Made By Me
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Return:
    float: a list of float-pointer number
    """
    result = [number async for number in async_generator()]
    return result
