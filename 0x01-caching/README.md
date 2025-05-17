# Caching System Project

This project implements multiple caching algorithms in Python by subclassing a base caching class.

## 📁 Files

- `base_caching.py`: Defines the base class `BaseCaching` with shared logic and constants.
- `0-basic_cache.py`: Implements `BasicCache` with no eviction policy.
- `1-fifo_cache.py`: Implements `FIFOCache` using First-In, First-Out eviction.
- `2-lifo_cache.py`: Implements `LIFOCache` using Last-In, First-Out eviction.
- `3-lru_cache.py`: Implements `LRUCache` using Least Recently Used eviction.
- `4-mru_cache.py`: Implements `MRUCache` using Most Recently Used eviction.
- `100-lfu_cache.py`: Implements `LFUCache` using Least Frequently Used with LRU tie-breaking.

## 🧠 Caching Policies

| Cache Type | Eviction Policy |
|------------|------------------|
| Basic      | No eviction |
| FIFO       | Oldest item first |
| LIFO       | Most recently added item |
| LRU        | Least recently used |
| MRU        | Most recently used |
| LFU        | Least frequently used (ties broken by least recent use) |

## 📌 Usage

Each caching class inherits from `BaseCaching` and implements `put()` and `get()` methods.

```python
from 1-fifo_cache import FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Apple")
print(my_cache.get("A"))  # Output: Apple

