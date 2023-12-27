"""
735. Asteroid Collision https://leetcode.com/problems/asteroid-collision/description/

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.
Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Constraints:
2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

SOLUTION
Using stack to store the asteroids moving right. When we encounter a leftward moving asteroid, resolve collision.
Time O(N): each rightward asteroid is pushed and popped from stack exactly once
Space O(N): stack
References
- https://leetcode.com/problems/asteroid-collision/solutions/3681775/easy-c-solution-using-stacks-simulation/
"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        rig: List[int] = []
        for i in range(len(asteroids)):
            if asteroids[i] > 0:
                rig.append(i)
                continue
            # resolve collision with leftward asteroid
            while len(rig) != 0:
                if asteroids[rig[-1]] > abs(asteroids[i]):
                    asteroids[i] = 0
                    break
                if asteroids[rig[-1]] == abs(asteroids[i]):
                    asteroids[rig[-1]] = 0
                    rig.pop()
                    asteroids[i] = 0
                    break
                asteroids[rig[-1]] = 0
                rig.pop()
        res: List[int] = [a for a in asteroids if a != 0]
        return res
