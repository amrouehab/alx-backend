#!/usr/bin/env python3
"""LIFOCache module - implements LIFO caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class uses LIFO eviction policy"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add item to cache with LIFO eviction"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.stack.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.stack.pop(-2 if self.stack[-1] == key else -1)
            del self.cache_data[last]
            print("DISCARD:", last)

    def get(self, key):
        """Retrieve item from cache"""
        return self.cache_data.get(key, None)

