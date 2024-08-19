#!/usr/bin/env python3
"""
    Made By Me
"""


from typing import AsyncGenerator
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[float, None]:
    """
    Return:
    float: a list of float-pointer number
    """
    result = [number async for number in async_generator()]
    return result
