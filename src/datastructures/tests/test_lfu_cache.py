import pytest
from datastructures.lfu_cache import *


class TestLfuCache:
    def test_when_capacity_is_less_than_1_then_raise_error(self):
        with pytest.raises(ValueError):
            LfuCache(capacity=0)

    def test_get_and_put(self):
        cache = LfuCache(capacity=10)
        cache.put("k1", "v1")
        cache.put("k2", "v2")
        assert cache.get("k1") == "v1"
        assert cache.get("k2") == "v2"
        assert cache.get("k3") is None

    def test_when_cache_is_full_then_evict_least_frequently_used(self):
        cache = LfuCache(capacity=2)
        cache.put("k1", "v1")
        cache.put("k2", "v2")
        cache.get("k1")
        cache.get("k2")
        cache.get("k1")  # least frequently used is 'k2'
        cache.put("k3", "v3")
        assert cache.get("k1") == "v1"
        assert cache.get("k2") is None
        assert cache.get("k3") == "v3"
        cache.put("k2", "v2")
        assert cache.get("k1") == "v1"
        assert cache.get("k2") == "v2"
        assert cache.get("k3") is None

    def test_when_cache_is_full_and_multiple_ties_for_lfu_then_evict_least_recently_used(
        self,
    ):
        cache = LfuCache(capacity=2)
        cache.put("k1", "v1")
        cache.put("k2", "v2")
        cache.get("k1")
        cache.get("k2")
        # k1 and k2 tie for LFU but least recently used is k1
        cache.put("k3", "v3")
        assert cache.get("k1") is None
        assert cache.get("k2") == "v2"
        assert cache.get("k3") == "v3"
