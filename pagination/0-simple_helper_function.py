#!/usr/bin/env python3
"""
    Made By Me
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Parameters:
    page(int): How many page.
    page_size(int): number of elements into the page

    Return:
    tuple: start_index and end_index
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    return (start_index, end_index)
