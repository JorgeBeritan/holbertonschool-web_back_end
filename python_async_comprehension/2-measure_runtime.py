#!/usr/bin/env python3
"""
    Made By Me
"""


from asyncio import gather
import time
from typing import List
ac = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Return:
    float: returns the amount of time waited for the execution
    to complete
    """
    start: float = time.time()
    await gather(ac(), ac(), ac(), ac())
    end: float = time.time()
    total: float = end - start
    return total
