"""
N+1
Unsorted Array will only have 1..N range inclusive
Array length is N+1

[3, 1, 3, 4, 2]
3


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

A more realistic problem would be to find a variable number of duplicates
but the space cost must be relaxed to O(N) to hold the result.
Hence the question asks for a fixed number of duplicates.
"""
from typing import List, Tuple


def find_one(arr: List[int]) -> int:
    res: int = 0
    for _ in arr:
        # temp variable `res` is required to do the swap properly!
        # the following swap does not work!
        # arr[0], arr[arr[0]] = arr[arr[0]], arr[0]
        res = arr[0]
        if res == arr[res]:
            break
        arr[0], arr[res] = arr[res], arr[0]
    return res


def find_two(arr: List[int]) -> Tuple[int, int]:
    first = 0
    second = 0
    for a in arr:
        if arr[abs(a)] < 0:
            if first == 0:
                first = abs(a)
            elif second == 0:
                second = abs(a)
                break
            continue  # do not update the negated value again
        arr[abs(a)] *= -1
    return first, second
