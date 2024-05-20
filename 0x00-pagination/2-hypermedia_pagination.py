#!/usr/bin/env python3
"""Simple pagination."""
import csv
from typing import List, Tuple, Dict
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing start and end indices for pagination.
    """
    begin = (page - 1) * page_size
    finish = begin + page_size
    return (begin, finish)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset based on pagination parameters."""
        assert type(page) == int and type(page_size) == int
        assert page_size > 0 and page > 0

        dataset = self.dataset()
        begin, finish = index_range(page, page_size)
        if begin > len(dataset):
            return []
        return dataset[begin:finish]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return hypermedia pagination details."""

        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        begin, finish = index_range(page, page_size)
        data_page = dataset[begin:finish]

        next_page = page + 1 if finish < len(dataset) else None
        prev_page = page - 1 if begin > 0 else None

        return {
            "page_size": len(data_page),
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
