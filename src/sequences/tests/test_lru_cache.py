import pytest
from sequences.lru_cache import *


class TestLruCache:
    def test_when_capacity_is_less_than_1_then_raise_error(self):
        with pytest.raises(ValueError):
            LruCache(capacity=0)

    def test_read_and_write_of_many_items(self):
        cache = LruCache(capacity=10)
        cache.put('k1', 'v1')
        cache.put('k2', 'v2')
        assert cache.get('k1') == 'v1'
        assert cache.get('k2') == 'v2'
        assert cache.get('k3') is None

    def test_eviction_policy(self):
        cache = LruCache(capacity=2)
        cache.put('k1', 'v1')
        cache.put('k2', 'v2')
        cache.get('k1')
        cache.get('k2')
        cache.get('k1')  # least recently used is 'k2'
        cache.put('k3', 'v3')
        assert cache.get('k1') == 'v1'
        assert cache.get('k2') is None
        assert cache.get('k3') == 'v3'
