"""
739. Daily Temperatures https://leetcode.com/problems/daily-temperatures/description/

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait
after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
Constraints:
1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100

SOLUTION
Stack holds indices of days where we have not seen a higher temp (next greater number).
Iterate over the temperatures array.
- While the stack is not empty and curr temp > top of the stack:
- Pop the top index from the stack.
- Update ans array with the difference between the current index and the popped index.
Time O(N): each element is pushed and popped exactly once from the stack.
Space O(1): not counting the ans array
References
- https://leetcode.com/problems/daily-temperatures/solutions/4343757/go-solution-great-explanation-and-full-description/
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st: List[int] = []
        ans: List[int] = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(st) != 0 and temperatures[st[-1]] < temperatures[i]:
                j = st.pop()
                ans[j] = i - j
            st.append(i)
        return ans
