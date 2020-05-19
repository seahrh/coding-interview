import unittest
from sequences.lru_cache import *


class TestLruCache(unittest.TestCase):
    def test_when_capacity_is_less_than_1_then_raise_error(self):
        self.assertRaises(ValueError, LruCache, 0)

    def test_read_and_write_of_many_items(self):
        cache = LruCache(capacity=10)
        cache.put('k1', 'v1')
        cache.put('k2', 'v2')
        self.assertEqual(cache.get('k1'), 'v1')
        self.assertEqual(cache.get('k2'), 'v2')
        self.assertEqual(cache.get('k3'), None)

    def test_eviction_policy(self):
        cache = LruCache(capacity=2)
        cache.put('k1', 'v1')
        cache.put('k2', 'v2')
        cache.get('k1')
        cache.get('k2')
        cache.get('k1')  # least recently used is 'k2'
        cache.put('k3', 'v3')
        self.assertEqual(cache.get('k1'), 'v1')
        self.assertEqual(cache.get('k2'), None)
        self.assertEqual(cache.get('k3'), 'v3')


if __name__ == '__main__':
    unittest.main()
