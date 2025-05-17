#!/usr/bin/env python3
"""BasicCache module - implements a basic caching system with no limit"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching and implements a basic dictionary cache"""

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache"""
        return self.cache_data.get(key, None)

