#!/usr/bin/env python3
"""
    Made By Me
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Parameters:
    max_delay(int): The first argument

    Return:
    float: a random number between 0 an max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
