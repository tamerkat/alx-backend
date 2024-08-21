#!/usr/bin/python3
"""FIFO caching."""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):

    def __init__(self):
        super().__init__()
        self.queue = []

    def put(self, key, item):
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.queue.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        if key in self.cache_data:
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    my_cache = LIFOCache()
