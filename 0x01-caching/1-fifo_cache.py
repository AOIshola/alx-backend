#!/usr/bin/env python3
"""FIFO Cache"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO cache class"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Put an item in cache and deletes the earliest
        added item when cache is at max capacity"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order.pop(0)
                print(f"DISCARD: {oldest_key}")
                del self.cache_data[oldest_key]
        else:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an in=tem from cache"""
        return self.cache_data.get(key, None)
