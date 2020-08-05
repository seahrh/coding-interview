"""
Given two strings and operations add, delete and substitution,
what is the minimum number of operations to convert one string to another string?

SOLUTION: Dynamic programming, memoization table
Each cell in the memo table represents the #operations to convert from one string to the other.
Initialize the first diagonal at top LH corner as zero (empty string to empty string).
Answer is at the last bottom RH cell.
Time O(N^2)
Space O(N^2)
"""

from typing import List


def edit_distance(s: str, t: str) -> int:
    memo: List[List[int]] = [[-1] * (len(t) + 1) for _ in range(len(s) + 1)]
    memo[0][0] = 0
    # number of ops to convert from empty string to S
    for i in range(1, len(s) + 1):
        memo[i][0] = i
    # number of ops to convert from empty string to T
    for j in range(1, len(t) + 1):
        memo[0][j] = j
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            diagonal = memo[i - 1][j - 1]
            # carry forward the diagonal if current chars are the same
            # i.e. s[i - 1] == t[j - 1]
            # index minus 1, remember we are using table index!
            if s[i - 1] != t[j - 1]:
                diagonal += 1
            memo[i][j] = min(diagonal, memo[i - 1][j] + 1, memo[i][j - 1] + 1)
    return memo[len(s)][len(t)]
