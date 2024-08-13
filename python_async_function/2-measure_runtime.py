#!/usr/bin/env python3
"""
    Made By Me
"""


import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Parameters:
    n(int): The first argument
    max_delay(int): The second argument

    Return:
    float: the total time of the execution
    """

    start = time.time()
    await wait_n(n, max_delay)
    end = time.time()

    total_time = end - start
    return total_time
