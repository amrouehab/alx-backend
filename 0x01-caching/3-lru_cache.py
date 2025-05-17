#!/usr/bin/env python3
"""LRUCache module - implements LRU caching system"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUCache class uses Least Recently Used eviction policy"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add item to cache with LRU eviction"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", lru_key)

    def get(self, key):
        """Retrieve item from cache and update its usage"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None

