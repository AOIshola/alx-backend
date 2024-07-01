#!/usr/bin/python3
""" LFU caching module
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching and
        implements an LFU caching system
    """

    def __init__(self):
        """ Initialize the class with the parent class' initializer """
        super().__init__()
        self.freq = defaultdict(int)
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                candidates = [k for k, v in self.freq.items() if v == min_freq]
                if len(candidates) > 1:
                    lru_candidate = min(candidates,
                                        key=lambda k: self.order.index(k))
                else:
                    lru_candidate = candidates[0]
                del self.cache_data[lru_candidate]
                del self.freq[lru_candidate]
                self.order.remove(lru_candidate)
                print(f"DISCARD: {lru_candidate}")

            self.cache_data[key] = item
            self.freq[key] = 1
            self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
