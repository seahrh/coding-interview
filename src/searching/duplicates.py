"""
N+1
Unsorted Array will only have 1..N range inclusive
Array length is N+1

[3, 1, 3, 4, 2]
3


[1, 3, 4, 2, 2]
2


[1, 3, 4, 2, 2]
2


Sum(1..N) = sum_n
Sum(array) - sum_n = duplicate_number
Time O(N)
Space O(1)

Time O(N)
Space O(1)


[2, 1, 2, 3, 4]
i=0
"""
from typing import List


def find_one_duplicate(arr: List[int]) -> int:
    while True:
        # temp variable is required to do the swap properly!
        # the following swap does not work!
        # arr[0], arr[arr[0]] = arr[arr[0]], arr[0]
        tmp = arr[0]
        if tmp == arr[tmp]:
            return tmp
        arr[0], arr[tmp] = arr[tmp], arr[0]
