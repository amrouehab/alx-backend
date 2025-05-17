#!/usr/bin/env python3
"""LFUCache module - implements LFU caching system with LRU tie-breaker"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """LFUCache class uses Least Frequently Used eviction policy"""

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.freq = defaultdict(int)
        self.use_order = []

    def put(self, key, item):
        """Add item to cache with LFU + LRU eviction"""
        if key is None or item is None:
            return

        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.freq.values())
            lfu_keys = [k for k in self.use_order if self.freq[k] == min_freq]
            lru_lfu_key = lfu_keys[0]
            self.use_order.remove(lru_lfu_key)
            del self.cache_data[lru_lfu_key]
            del self.freq[lfu_lfu_key]
            print("DISCARD:", lru_lfu_key)

        self.cache_data[key] = item
        self.freq[key] += 1
        if key in self.use_order:
            self.use_order.remove(key)
        self.use_order.append(key)

    def get(self, key):
        """Retrieve item and update frequency/usage"""
        if key in self.cache_data:
            self.freq[key] += 1
            self.use_order.remove(key)
            self.use_order.append(key)
            return self.cache_data[key]
        return None

