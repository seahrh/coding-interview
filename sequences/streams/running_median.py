"""
17.20 Continuous Median: Numbers are randomly generated and passed to a method.
Write a program to find and maintain the median value as new values are generated.
"""
import heapq


class RunningMedian:
    min_heap = []
    max_heap = []

    def add(self, i):
        pass

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
