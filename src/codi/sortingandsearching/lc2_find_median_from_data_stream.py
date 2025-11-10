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
from heapq import heappush, heapreplace
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
