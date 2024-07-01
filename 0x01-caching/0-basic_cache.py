#!/usr/bin/env python3
"""Basic Caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching and
        implements a basic caching system without a limit
    """
    def put(self, key, item):
        """Add an item to a cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from a cache"""
        if key is None:
            return None

        return self.cache_data.get(key)
