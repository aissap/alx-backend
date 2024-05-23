#!/usr/bin/env python3
""" MRUCache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class, a caching system that uses MRU policy """

    def __init__(self):
        """Initializes the cache."""
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache using MRU policy """
        if key is None or item is None:
            return

        self.update_usage_order(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.usage_order.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """ Get an item by key """
        if key not in self.cache_data:
            return None

        self.update_usage_order(key)

        return self.cache_data[key]

    def update_usage_order(self, key):
        """ Update the usage order with the most recent usage """
        if key in self.usage_order:
            self.usage_order.remove(key)
        self.usage_order.append(key)
