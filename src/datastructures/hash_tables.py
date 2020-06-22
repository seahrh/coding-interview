"""
Implement hash table to store N items with fixed capacity M.
What happens if N > M ?
You are not allowed to use Dict and Set.
Increase capacity (decrease load factor) to reduce risk of collision.
"""
from typing import TypeVar, Generic, List, NamedTuple, Optional, Hashable

# Declare type variables
K = TypeVar("K", bound=Hashable)
V = TypeVar("V")


def string_hash(key: K, capacity: int) -> int:
    """Return hash value of given key.
    Cast key to string representation.
    Treat string as a sequence of ordinal values; weighted sum with position as weight.
    """
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
        # If Set is allowed, use List of Sets (contains tuples of K, Entry)
        # Initialize empty collection in each slot
        self._table: List[List[Entry]] = [[] for _ in range(self._capacity)]

    def put(self, key: K, value: V) -> None:
        """Insert takes O(N) time if risk of collision is high. Else O(1) time.
        Speed up reads at the expense of writes;
        Sort the entries array when the array grows. Insert now takes O(N lg N) time.
        """
        i = self._hash(key, self._capacity)
        e = Entry(key, value)
        entries = self._table[i]
        # overwrite key if it already exists
        exists: bool = False
        for j, entry in enumerate(entries):
            if key == entry.key:
                entries[j] = e
                exists = True
                break
        if not exists:
            entries.append(e)

    def get(self, key: K) -> Optional[V]:
        """Search takes O(N) time if risk of collision is high. Else O(1) time.
        Search takes O(lg N) time if entries array is sorted.
        But this means we need to sort the array each time it is updated.
        """
        i = self._hash(key, self._capacity)
        for entry in self._table[i]:
            if key == entry.key:
                v: V = entry.value
                return v
        return None
