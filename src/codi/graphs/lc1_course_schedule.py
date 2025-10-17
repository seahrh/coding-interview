"""
207. Course Schedule https://leetcode.com/problems/course-schedule/description/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where
prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

SOLUTION
Approach
Adjacency List: Each course points to the courses depending on it.
State Tracking:
0 = unvisited
1 = visiting (on current recursion stack)
2 = visited (fully explored, no cycles downstream)
DFS (Depth-First Search):
If visiting a node already on the recursion stack (vis == 1), a cycle exists.
If fully processed (vis == 2), skip—safe branch.
How It Works
Detects any cycle during DFS in the dependency graph.
If a cycle is found, returns False. Otherwise, True.
Time Complexity
Adjacency List Construction: O(prerequisites.length)
DFS Search: Each node is visited once, and each edge is traversed once.
Total: O(numCourses + prerequisites.length)
Space Complexity
Adjacency List: O(numCourses + prerequisites.length)
State Array (vis): O(numCourses)
Recursion Stack: O(numCourses) in worst case
"""

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list for dependency graph
        adj: List[List[int]] = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            if a == b:
                return False  # Self-loop (not allowed), causes cycle immediately
            adj[b].append(a)

        # States: 0=unvisited, 1=visiting, 2=visited
        vis: List[int] = [0] * numCourses

        def cycle(s: int) -> bool:
            vis[s] = 1
            for i in adj[s]:
                if vis[i] == 0 and cycle(i):  # cycle is found downstream
                    return True
                if vis[i] == 1:  # return to a visited node; cycle found
                    return True
            vis[s] = 2
            return False

        for i in range(numCourses):
            if cycle(i):
                return False
        return True
