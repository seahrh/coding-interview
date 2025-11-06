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
Stack saves indices, not temperatures:
We use a stack to remember days we haven’t seen a warmer future for yet.
Loop over each day:
For every new temperature:
Compare with unresolved previous days:
While the stack isn’t empty and today’s temperature is higher than the temperature on the day at the top of the stack:
Pop that previous day off the stack (it’s now resolved).
Figure out how many days it took for a warmer temperature (today’s index minus previous day’s index).
Record that in the answer array.
Add today to the stack (it might need to wait for a future warmer day).
Answer array is returned: Any days left with zero didn’t see a warmer day in the future.

Time Complexity: O(N)
Each day is added and removed from the stack just once.
Space Complexity: O(N)
The stack could store up to all the days (in worst case, strictly decreasing temperatures).
This is a stack-based “next greater element” pattern, perfect for finding the first larger future value efficiently.

References
- https://leetcode.com/problems/daily-temperatures/solutions/4343757/go-solution-great-explanation-and-full-description/
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[int] = []  # Will store indices of temperatures array
        answer = [0] * len(temperatures)  # Default wait is 0 days

        for today, temp in enumerate(temperatures):
            # Check if today's temperature is warmer than previous unresolved days
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                answer[prev_day] = today - prev_day  # Waited this many days

            stack.append(today)  # Process today's temperature next time

        return answer
