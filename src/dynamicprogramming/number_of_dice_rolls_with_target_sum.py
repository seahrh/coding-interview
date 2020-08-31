"""
You have d dice, and each die has f faces numbered 1, 2, ..., f.
Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7 to roll the dice
so the sum of the face up numbers equals target. All dice must be thrown together.
Example 1:
Input: d = 1, f = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces. There is only one way to get a sum of 3.
Constraints:
1 <= d, f <= 30
1 <= target <= 1000

SOLUTION
Bottom-up DP. The states are how many dice are remaining, and what sum total you have rolled so far.
Suppose we have 5 dice with 6 faces each. Determine how many ways to make 18.
Case 1: The last die is a 1. The remaining 4 dice must sum to 18-1=17 => dp(4, 6, 17) ways.
Case 2: The last die is a 2. The remaining 4 dice must sum to 18-2=16 => dp(4, 6, 16) ways.
Case 3: The last die is a 3. The remaining 4 dice must sum to 18-3=15 => dp(4, 6, 15) ways.
Case 4: The last die is a 4. The remaining 4 dice must sum to 18-4=14 => dp(4, 6, 14) ways.
Case 5: The last die is a 5. The remaining 4 dice must sum to 18-5=13 => dp(4, 6, 13) ways.
Case 6: The last die is a 6. The remaining 4 dice must sum to 18-6=12 => dp(4, 6, 12) ways.
Time O(TF)
Space O(TD)

See
- https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
- https://www.geeksforgeeks.org/dice-throw-dp-30/
"""
from typing import List


def solve(dice: int, faces: int, target: int) -> int:
    mod: int = int(1e9) + 7
    memo: List[List[int]] = [[0] * (dice + 1) for _ in range(target + 1)]
    for i in range(1, min(faces + 1, target + 1)):
        memo[i][1] = 1
    if dice > 1:
        for i in range(1, target + 1):
            for j in range(1, faces + 1):
                if i - j >= 0:
                    memo[i][dice] += memo[i - j][dice - 1]
                    memo[i][dice] = memo[i][dice] % mod
    return memo[target][dice]
