"""
Given a list of integer A and a number k,
create a function foo that generate a list of integer B that element is sum of the last k number on A
Example:
foo(A=[1,2,3,4,5], k=2) -> [1, 1+2, 2+3, 3+4, 4+5] = [1,3,5,7,9]
foo(A=[1,2,3,4,1,2,3,4], k=3) ->  [1,3,6,9,8,7,6,9]

SOLUTION
Brute force solution takes O(NK) time. Improve with bottom-up DP.
dp[i] = sum of last k items ending at position i
Recurrence: dp[i] = dp[i-1] + A[i] - A[i-k]
Time O(N)
Space O(1): we need only to store dp[i-1], so we do not need the entire dp array
"""
from typing import List


def solve(A: List[int], k: int) -> List[int]:
    res = []
    prev = 0
    for i in range(len(A)):
        sm = prev + A[i]
        if i - k >= 0:
            sm -= A[i - k]
        res.append(sm)
        prev = sm
    return res
