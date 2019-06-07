"""
17.20 Continuous Median: Numbers are randomly generated and passed to a method.
Write a program to find and maintain the median value as new values are generated.
"""
import heapq


class RunningMedian:
    """Use two priority heaps: a max heap for the values below the median,
    and a min heap for the values above the median.

    When a new value arrives,
    it is placed in the maxHeap if the value is less than or equal to the median,
    otherwise it is placed into the minHeap.
    The heap sizes can be equal, or the maxHeap may have one extra element.
    This constraint can easily be restored by shifting an element from one heap to the other.
    The median takes O(1) time, by looking at the top element(s).
    Updates take O(lg n) time.
    The heaps take O(n) space.

    Max heap is implemented in Python by multiplying the value by -1
    before adding it to the heap ("taking the inverse").
    """

    min_heap = []
    max_heap = []

    def add(self, i):
        """Maintains invariant that len(max_heap) >= len(min_heap)"""
        if len(self.max_heap) == len(self.min_heap):
            if len(self.min_heap) and i > self.min_heap[0]:
                j = heapq.heappushpop(self.min_heap, i)
                heapq.heappush(self.max_heap, j * -1)
            else:
                heapq.heappush(self.max_heap, i * -1)
        else:
            if i < self.max_heap[0]:
                j = heapq.heappushpop(self.max_heap, i * -1) * -1
                heapq.heappush(self.min_heap, j)
            else:
                heapq.heappush(self.min_heap, i)

    def median(self):
        # maxHeap is always at least as big as minHeap.
        # So if maxHeap is empty, then minHeap is also empty.
        if len(self.max_heap) == 0:
            return 0
        if len(self.max_heap) == len(self.min_heap):
            return float(self.min_heap[0] / 2) + float(self.max_heap[0] * -1 / 2)
        # If maxHeap and minHeap are of different sizes,
        # then maxHeap must have one extra element. Return maxHeap's top element.
        return self.max_heap[0] * -1
