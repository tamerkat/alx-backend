#!/usr/bin/python3
""" BaseCaching module"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class"""
    def __init__(self):
        """Constructor."""
        super().__init__()

    def put(self, key, item):
        """function"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
    """function"""
    if key in self.cache_data:
        return self.cache_data[key]
    return None
