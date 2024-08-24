#!/usr/bin/env python3
"""
    Made By Me
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """
    Yield a random number between 1 and 10,
    in this function we learn how to use yield in async function
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
