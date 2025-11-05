"""
621. Task Scheduler https://leetcode.com/problems/task-scheduler/description/

Given a characters array tasks, representing the tasks a CPU needs to do,
where each letter represents a different task. Tasks could be done in any order.
Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.
Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation:
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation:
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
Constraints:
1 <= task.length <= 10^4
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].

SOLUTION
Heap/Greedy Simulation
A heap-based solution simulates the actual scheduling process, always choosing the next most frequent available task.

Algorithm Outline
Build max-heap: Push all (-frequency, task) pairs to simulate a max heap.
Schedule tasks in batches of up to n+1 each round:
Try to pop and execute up to n+1 tasks, then push back remaining instances.
Count idle slots if insufficient tasks are left to fill the cooldown.
Repeat until all tasks are executed.

Heap Solution Complexity
Time: O(N log K). Each of N tasks scheduled with heap insertion/removal (K = number of unique tasks).
Space: O(K)
**Since K is fixed at 26, then time complexity O(N) and space O1)!
When is heap better?
For simulating actual schedule (not just calculating minimal length).
Useful if you need the exact order or deal with variable cooldowns per task.
But the arithmetic formula is faster and more space-efficient for this specific problem.
Time O(N)
Space O(1) - constant space because K is fixed at 26
"""

import heapq
from collections import Counter
from typing import List


class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        """Optimal solution using math."""
        if n == 0:
            return len(tasks)
        freq = Counter(tasks)
        max_freq = max(freq.values())
        # Number of tasks with max frequency
        max_count = sum(1 for v in freq.values() if v == max_freq)
        # Formula explanation:
        # (max_freq - 1) rounds where we need full cooldown between most frequent tasks.
        # Each round has (n + 1) slots: the max_freq task and n cooldowns/other tasks.
        # For tasks with equal most frequency, they fill the final slot of the last cycle: + max_count
        # Not all slots may end up idle — other tasks may fill them.
        intervals = (max_freq - 1) * (n + 1) + max_count
        # The schedule is at least as long as the number of tasks
        return max(len(tasks), intervals)

    def leastIntervalHeap(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq = Counter(tasks)
        heap = [(-cnt, task) for task, cnt in freq.items()]
        heapq.heapify(heap)
        time = 0
        while heap:
            temp = []
            # In each "round", you can schedule up to n + 1 tasks (one per time unit).
            # For each task actually picked and scheduled in this round, you increment slots.
            # If you run out of tasks before filling n + 1 slots, slots can be less than n + 1.
            slots = 0
            # Try to execute n+1 most frequent tasks
            for _ in range(n + 1):
                if heap:
                    cnt, task = heapq.heappop(heap)
                    if cnt + 1 < 0:  # Still tasks pending
                        temp.append((cnt + 1, task))
                    slots += 1
            # Add back remaining tasks
            for item in temp:
                heapq.heappush(heap, item)
            # If heap is empty, last round may be partial
            time += slots if not heap else n + 1
        return time
