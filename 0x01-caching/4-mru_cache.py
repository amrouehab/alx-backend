#!/usr/bin/env python3
"""MRUCache module - implements MRU caching system"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class uses Most Recently Used eviction policy"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """Add item to cache with MRU eviction"""
        if key is None or item is None:
            return

        if key in self.usage:
            self.usage.remove(key)
        self.usage.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.usage.pop(-2 if self.usage[-1] == key else -1)
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

    def get(self, key):
        """Retrieve item from cache and update its usage"""
        if key in self.cache_data:
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache_data[key]
        return None

