#!/usr/bin/env python3
"""
Module for simple pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing start and end indices for pagination.
    """
    begin = (page - 1) * page_size
    finish = begin + page_size
    return begin, finish
