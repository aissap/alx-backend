#!/usr/bin/env python3
from typing import Tuple
"""
Module for simple pagination helper function.
"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing start and end indices for pagination.
    """
    begin = (page - 1) * page_size
    finish = begin + page_size
    return (begin, finish)
