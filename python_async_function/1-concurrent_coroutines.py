#!/usr/bin/env python3
"""
    Made By Me
"""


from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Parameters:
    n(int): First argument
    max_delay(int): Second argument

    Return:
    List[float]: a list of a float-point number
    """
    delays = []

    async def append_wait():
        delay = await wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*(append_wait() for _ in range(n)))
    return sorted(delays)
