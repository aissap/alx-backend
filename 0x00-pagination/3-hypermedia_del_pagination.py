#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""


import csv
from typing import List, Dict, Any


class Server:
    """Server class for paginating a dataset of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Returns the loaded dataset from the file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Creates and returns a dataset indexed by position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                    i: dataset[i]
                    for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
            self, index: int = None, page_size: int = 10
    ) -> Dict[str, Any]:
        """Provides a paginated dataset starting from a specific index."""
        assert index is not None and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.indexed_dataset()
        dataset_size = len(data)
        assert index < dataset_size

        items = []
        current_index = index
        count = 0

        while count < page_size and current_index < dataset_size:
            if current_index in data:
                items.append(data[current_index])
                count += 1
            current_index += 1

        next_index = current_index if current_index < dataset_size else None

        return {
            "index": index,
            "data": items,
            "page_size": len(items),
            "next_index": next_index
        }
