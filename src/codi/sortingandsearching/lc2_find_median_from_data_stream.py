"""
295. Find Median from Data Stream https://leetcode.com/problems/find-median-from-data-stream/description/

The median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
Constraints:
-10^5 <= num <= 10^5
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
Follow up:
If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

SOLUTION
2 heaps: a max heap for the values below the median and a min heap for the values above the median.
When a new value arrives, it is placed in the maxHeap if the value is less than or equal to the median,
otherwise it is placed into the minHeap.
**The heap sizes can be equal, or the maxHeap may have one extra element.
Maintain this invariant by shifting an element from one heap to the other.
Find median takes O(1) time, by looking at the top element(s).
Updates take O(lg n) time.
The heaps take O(n) space.
"""

# heapq.heapreplace(heap, item)
# Pop and return the smallest item from the heap, and also push the new item.
# The heap size doesn’t change. If the heap is empty, IndexError is raised.
# This one step operation is more efficient than a heappop() followed by heappush()
# and can be more appropriate when using a fixed-size heap.
# The pop/push combination always returns an element from the heap and replaces it with item.
from heapq import heappush, heapreplace, nlargest, nsmallest
from typing import List


class MedianFinder:

    def __init__(self):
        self.mxh: List[int] = []
        self.mnh: List[int] = []

    def addNum(self, num: int) -> None:
        if len(self.mnh) == len(self.mxh):
            # If new element needs to go into minHeap, then transfer min-element to maxHeap.
            if len(self.mnh) != 0 and num > self.mnh[0]:
                heappush(self.mxh, -heapreplace(self.mnh, num))
            else:
                heappush(self.mxh, -num)
        else:
            # maxHeap is one element larger than minHeap
            # If new element needs to go into maxHeap, then transfer max-element to minHeap.
            if num <= -self.mxh[0]:
                heappush(self.mnh, -heapreplace(self.mxh, -num))
            else:
                heappush(self.mnh, num)

    def findMedian(self) -> float:
        if len(self.mxh) == len(self.mnh):
            return float(-self.mxh[0] / 2) + float(self.mnh[0] / 2)
        return -self.mxh[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class MedianFinderFollowUp1:
    """
    Follow-up 1: If all integers are in the range [0, 100], how would you optimize your solution?
    This means bounded input domain (only 101 possible values). We can ditch the heaps and use a counting array.
    To find the median, “walk through” this array, accumulating counts
    until we reach the middle position(s) in the sorted order.
    Time complexity: addNum: O(1), findMedian: O(100) = constant time
    Space complexity: O(100) = constant space
    """

    def __init__(self):
        self.counts: List[int] = [0] * 101
        self.size: int = 0

    def addNum(self, num: int) -> None:
        self.counts[num] += 1
        self.size += 1

    def findMedian(self) -> float:
        mid1 = (self.size + 1) // 2
        mid2 = (self.size + 2) // 2  # handles even/odd
        count = 0
        m1 = m2 = None
        for i in range(101):
            count += self.counts[i]
            if not m1 and count >= mid1:
                m1 = i
            if not m2 and count >= mid2:
                m2 = i
            if m1 and m2:
                break
        return (m1 + m2) / 2.0  # type: ignore[operator]


class MedianFinderFollowUp2:
    """
    Follow-up 2: If 99% of numbers are in [0, 100], how would you optimize?
    This means: Most values fall in [0, 100], but some are outliers (very large or small).
    We can’t assume everything is within [0,100], so pure counting array no longer works alone.
    👉 Hybrid Approach: Counting Array + Heaps
    Use the counting array for numbers within [0, 100].
    Use two heaps for outliers:
    small_heap: for numbers < 0
    large_heap: for numbers > 100
    We track counts and sizes:
    Total numbers in heaps + counts array = total size.
    When finding median:
    Compare how many numbers are in each region (small_heap, counts array, large_heap).
    If median falls inside [0,100], find it via cumulative count in the array.
    Otherwise, pull from heaps.

    Time complexity:
    addNum: O(log n)` (only for outliers, O(1) for [0,100])
    findMedian: O(100 + log n) worst-case, typically ≈ O(100) since 99% are within [0,100]
    Space complexity: O(100 + n_outliers)
    """

    def __init__(self):
        self.counts: List[int] = [0] * 101
        self.mxh: List[int] = []  # max-heap for <0 (invert sign)
        self.mnh: List[int] = []  # min-heap for >100
        self.size: int = 0

    def addNum(self, num: int) -> None:
        if num < 0:
            heappush(self.mxh, -num)
        elif num > 100:
            heappush(self.mnh, num)
        else:
            self.counts[num] += 1
        self.size += 1

    def findMedian(self) -> float:
        # Get total counts below 0, within [0,100], above 100
        left_size = len(self.mxh)
        mid_size = sum(self.counts)
        # right_size = len(self.mnh)
        # Determine median positions
        mid1 = (self.size + 1) // 2
        mid2 = (self.size + 2) // 2

        def get_value_at_rank(rank: int) -> int:
            if rank <= left_size:
                return -nlargest(rank, self.mxh)[-1]
            if rank <= left_size + mid_size:
                rank -= left_size
                count = 0
                for i in range(101):
                    count += self.counts[i]
                    if count >= rank:
                        return i
            # right side
            rank -= left_size + mid_size
            return nsmallest(rank, self.mnh)[-1]

        return (get_value_at_rank(mid1) + get_value_at_rank(mid2)) / 2.0
