"""
Shortest Supersequence: You are given two arrays, one shorter (with all distinct elements) and one
longer. Find the shortest subarray in the longer array that contains **all** the elements in the shorter
array. The items can appear in any order.
EXAMPLE
Input:
{1, 5, 9}
{7, 5,9,8,2,1,3, 5,7,9,1,1,5,8,8,9, 7}
Output: {5,7,9,1} so indexes in the range [7, 10]

(17.18, p595)
SOLUTION: Heaps
- Each include has a queue that stores its positions in the array.
- The heads of the queues provide a candidate seq (min_index, max_index)
- Use a min-heap to find the smallest head of the queues.
- Remove the smallest head from its respective queue.
- Repeat until a queue is empty i.e. no more seqs can be found

B is the length of the array and S is the size of the includes.
Time O((B + S) lg S)
Space O(B + S)
"""
import heapq
import sys
from collections import deque
from typing import Deque, Dict, List, NamedTuple, Optional, Set


class Node(NamedTuple):
    """Item to be inserted into the heap. Break ties on second field `key` which must be distinct."""

    position: int
    key: int


class Range(NamedTuple):
    lo: int
    hi: int


def _location_map(arr: List[int], includes: Set[int]) -> Dict[int, Deque[int]]:
    res: Dict[int, Deque[int]] = {}  # O(B) space
    # initialize empty linked list, in case include not found in array
    for i in includes:  # O(S) time
        res[i] = deque()
    for i, a in enumerate(arr):  # O(B) time
        if a in includes:
            res[a].append(i)
    return res


def _shortest_closure(location_map: Dict[int, Deque[int]]) -> Optional[Range]:
    min_heap: List[Node] = []  # O(S) space
    hi = -sys.maxsize
    for key, indices in location_map.items():  # O(S lg S) time
        if len(indices) == 0:
            return None
        index = indices.popleft()
        heapq.heappush(min_heap, Node(position=index, key=key))  # O(lg S) time
        hi = max(hi, index)
    lo = min_heap[0].position
    best_lo = lo
    best_hi = hi
    while True:  # O(B lg S) time
        min_node = heapq.heappop(min_heap)  # O(lg S) time
        lo = min_node.position
        if hi - lo < best_hi - best_lo:  # found shorter seq
            best_lo = lo
            best_hi = hi
        indices = location_map[min_node.key]
        if len(indices) == 0:  # no more items, hence no more subseqs
            break
        index = indices.popleft()
        hi = max(hi, index)
        heapq.heappush(min_heap, Node(position=index, key=min_node.key))  # O(lg S) time
    return Range(best_lo, best_hi)


def shortest_supersequence(arr: List[int], includes: Set[int]) -> Optional[Range]:
    return _shortest_closure(_location_map(arr, includes))
