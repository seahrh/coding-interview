"""
146. LRU Cache https://leetcode.com/problems/lru-cache/description/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache.
If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
Constraints:
1 <= capacity <= 3000
0 <= key <= 10^4
0 <= value <= 10^5
At most 2 * 10^5 calls will be made to get and put.

SOLUTION
Hash table with value pointing into the node of a Doubly linked list.
Access, add and remove in O(1) time.
head=Most Recently Used, tail=Least Recently Used
References
- https://flykiller.github.io/leetcode/0146
"""

from collections import OrderedDict
from dataclasses import dataclass
from typing import Dict, Optional


class LRUCacheWithOrderedDict:
    def __init__(self, capacity: int):
        self.cache: OrderedDict[int, int] = OrderedDict()
        self.capacity: int = capacity

    def get(self, key: int) -> int:
        # put last used item in the rightmost position
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # put last used item in the rightmost position
        if key in self.cache:
            self.cache.move_to_end(key, last=True)
        self.cache[key] = value
        # delete lru item in the leftmost position
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# Solution that requires implementation of Doubly linked list


@dataclass
class Node:
    k: int
    v: int
    prev: Optional["Node"] = None
    next: Optional["Node"] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic: Dict[int, Node] = {}
        self.head = Node(k=-1, v=-1)
        self.tail = Node(k=-1, v=-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        p = node.prev
        n = node.next
        p.next = n  # type: ignore[union-attr]
        n.prev = p  # type: ignore[union-attr]

    def appendleft(self, node: Node) -> None:
        h = self.head.next
        h.prev = node  # type: ignore[union-attr]
        self.head.next = node
        node.next = h
        node.prev = self.head

    def get(self, key: int):
        if key in self.dic:
            n = self.dic[key]
            self.remove(n)
            self.appendleft(n)
            return n.v
        return -1

    def put(self, key: int, value: int):
        if key in self.dic:
            self.remove(self.dic[key])
        n = Node(key, value)
        self.appendleft(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.tail.prev  # type: ignore[assignment]
            self.remove(n)
            del self.dic[n.k]
