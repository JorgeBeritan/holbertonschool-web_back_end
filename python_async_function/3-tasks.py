#!/usr/bin/env python3
"""
    Made By Me
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Parameters:
    max_delay(int): The first argument

    Returns:
    asyncio.Task: return a asyncio task
    """

    return asyncio.create_task(wait_random(max_delay))
