from typing import List, Tuple

"""
Design an algorithm and write code to remove the duplicate characters in
a string without using any additional buffer. NOTE: One or two additional
variables are fine. An extra copy of the array is not. [CTCI Q1.3]
"""


def remove(s):
    # This takes O(n) time and O(m) space, where m is the number of unique chars.
    # assume UTF-8 ASCII charset only
    num_chars = 128
    is_present = [False] * num_chars
    res = ""
    for c in s:
        cp = ord(c)
        if is_present[cp] is False:
            res += c
            is_present[cp] = True
    return res


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
