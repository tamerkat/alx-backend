#!/usr/bin/python3
""" BaseCaching module"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class"""
    def put(self, key, item):
        """function"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """function"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
