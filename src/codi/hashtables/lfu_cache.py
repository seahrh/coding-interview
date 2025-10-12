"""
Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put in O(1) time complexity.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return None.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.
For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency),
the least recently used key would be evicted.

Note that the number of times an item is used
is the number of calls to the get and put functions for that item since it was inserted.
This number is set to zero when the item is removed.

See https://leetcode.com/problems/lfu-cache/
"""

from typing import Dict, NamedTuple

from codi.hashtables.linked_list import *


class Item(NamedTuple):
    key: str
    value: str
    freq: int = 0


class LfuCache:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("capacity must be a positive integer")
        self.capacity: int = capacity
        self.map: Dict[str, DLinkedList.Node] = {}
        self.freq_map: Dict[int, DLinkedList] = {}
        self.freq_min = 1

    def _increment_frequency(self, node: DLinkedList.Node) -> None:
        data: Item = node.data
        # remove entry at old frequency
        if data.freq != 0:
            use_ordering = self.freq_map[data.freq]
            use_ordering.remove(node)
            if self.freq_min == data.freq and len(use_ordering) == 0:
                self.freq_min += 1
        # add entry at new frequency
        if data.freq + 1 not in self.freq_map:
            self.freq_map[data.freq + 1] = DLinkedList()
        use_ordering = self.freq_map[data.freq + 1]
        use_ordering.append_left(node)
        node.data = Item(key=data.key, value=data.value, freq=data.freq + 1)

    def get(self, key: str) -> Optional[str]:
        if key in self.map:
            node: DLinkedList.Node = self.map[key]
            self._increment_frequency(node)
            data: Item = node.data
            return data.value
        return None

    def put(self, key: str, value: str) -> None:
        # eviction if cache is full
        if len(self.map) == self.capacity and key not in self.map:
            use_ordering = self.freq_map[self.freq_min]
            node = use_ordering.pop()
            if node is not None:
                del self.map[node.data.key]
        node = DLinkedList.Node(data=Item(key=key, value=value))
        if key in self.map:
            node = self.map[key]
        self._increment_frequency(node)
        self.map[key] = node
