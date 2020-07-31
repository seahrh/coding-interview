# Heapsort
# In-place
# Worst case takes O(n lg n) time and O(1) space
from abc import ABCMeta, abstractmethod
from typing import List, TypeVar, Any


class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        ...


T = TypeVar("T", bound=Comparable)


def _parent(index_of_child: int) -> int:
    return int((index_of_child - 1) / 2)


def _left_child(index_of_parent: int) -> int:
    return 2 * index_of_parent + 1


def _sift_down(arr: List[T], lo: int, hi: int) -> None:
    # Repair the heap whose root element is at index 'lo',
    # assuming the heaps rooted at its children are valid.
    # Base case: empty array
    if lo >= hi:
        return
    root = lo
    child = _left_child(root)
    # keep track of child to swap with
    target = root
    while child <= hi:
        if arr[child] > arr[target]:
            target = child
        # if the right child is greater
        child += 1
        if child <= hi and arr[child] > arr[target]:
            target = child
        # Root holds the largest element.
        # Since heaps rooted at children are valid, we are done.
        if target == root:
            return
        # continue to sift down the child now
        arr[target], arr[root] = arr[root], arr[target]
        root = target
        child = _left_child(root)


def _heapify(arr: List[T]) -> None:
    # Put array elements in max heap order, in-place.
    # Build the heap bottom-up, so begin from the last parent node.
    # The last element in a 0-based array is at index len-1; find the parent of that element
    hi = len(arr) - 1
    lo = _parent(hi)
    while lo >= 0:
        _sift_down(arr, lo, hi)
        lo -= 1


def heapsort(arr: List[T]) -> None:
    # Base case: empty array or array of length 1 is already sorted.
    if len(arr) < 2:
        return
    _heapify(arr)
    # hi is the first index of the sorted subarray
    hi = len(arr) - 1
    while hi > 0:
        arr[0], arr[hi] = arr[hi], arr[0]
        # heap size is reduced by 1
        hi -= 1
        # swap ruined heap property, so restore it
        _sift_down(arr, 0, hi)
