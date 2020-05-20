"""
LRU Cache: Design and build a "least recently used" cache, which evicts the least recently used item.
The cache should map from keys to values (allowing you to insert and retrieve a value associated
with a particular key) and be initialized with a max size. When it is full, it should evict the least
recently used item. You can assume the keys are integers and the values are strings.

(16.25, p533)
Solution: Use hash table to point into the nodes of a linked list, which represents last-use ordering.

Do the following in average case O(1) time:

Inserting Key, Value Pair:
    Create a linked list node with key, value.
    Insert into head of linked list.
    Insert key -> node mapping into hash table.

Retrieving Value by Key:
    Look up node in hash table and return value. Update most recently used item

Finding Least Recently Used:
    Least recently used item will be found at the end of the linked list.

Updating Most Recently Used:
    Move node to front of linked list. Hash table does not need to be updated.

Eviction:
    Remove tail of linked list. Get key from linked list node and remove key from hash table.
"""
from collections import namedtuple
from datastructures.linked_list import *


CacheItem = namedtuple("CacheItem", "key value")


class LruCache:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("capacity must be a positive integer")
        self.capacity = capacity
        self.map = {}
        self.use_ordering = LinkedList()

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.use_ordering.remove(node)
            self.use_ordering.append_left(node)
            return node.data.value
        return None

    def put(self, key, value):
        if len(self.map) == self.capacity and key not in self.map:
            node = self.use_ordering.pop()
            del self.map[node.data.key]
        node = LinkedListNode(data=CacheItem(key, value))
        self.map[key] = node
        self.use_ordering.append_left(node)
