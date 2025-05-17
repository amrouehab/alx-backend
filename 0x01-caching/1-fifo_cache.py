#!/usr/bin/env python3
"""FIFOCache module - implements FIFO caching system"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class uses FIFO eviction policy"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add item to cache with FIFO eviction"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest = self.order.pop(0)
            del self.cache_data[oldest]
            print("DISCARD:", oldest)

    def get(self, key):
        """Retrieve item from cache"""
        return self.cache_data.get(key, None)

