from typing import TypeVar, Generic, List, NamedTuple, Optional

# Declare type variables
K = TypeVar("K")
V = TypeVar("V")


def string_hash(key: K, capacity: int) -> int:
    res = 0
    s = str(key)
    w = len(s)
    for c in s:
        res += w * ord(c)
        w -= 1
    return res % capacity


class Entry(NamedTuple, Generic[K, V]):
    key: K
    value: V


class MyHashTable(Generic[K, V]):
    def __init__(self, capacity: int = 10, hash_fn=string_hash):
        if capacity < 1:
            raise ValueError("capacity must not be less than 1")
        self._capacity = capacity
        self._hash = hash_fn
        # If Set is not allowed, use List of Lists
        # If Set is allowed, use List of Sets
        # Initialize empty collection in each slot
        self._table: List[List[Entry]] = [[] for _ in range(self._capacity)]

    def put(self, key: K, value: V) -> None:
        """Insert in O(N) time. (worst case: all keys are hashed to the same slot)"""
        i = self._hash(key, self._capacity)
        es = []
        for e in self._table[i]:
            if key != e.key:
                es.append(e)
        es.append(Entry(key, value))
        self._table[i] = es

    def get(self, key: K) -> Optional[V]:
        """Search in O(N) time. (worst case: all keys are hashed to the same slot)"""
        i = self._hash(key, self._capacity)
        for entry in self._table[i]:
            if key == entry.key:
                v: V = entry.value
                return v
        return None
