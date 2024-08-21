#!/usr/bin/python3
""" BaseCaching module"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache class"""
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.cache_data[key] = item
                discard = self.order[0]
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        if key in self.cache_data:
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    my_cache = FIFOCache()
