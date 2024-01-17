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
You are given an array of n+2 elements. All elements of the array are in range 1 to n.
All elements occur once except two numbers which occur twice. Find the two repeating numbers.
For example, array = {4, 2, 4, 5, 2, 3, 1} and n = 5
The above array has n + 2 = 7 elements with all elements occurring once except 2 and 4 which occur twice.
So the output should be 4 2.

EXAMPLES
Input: [3, 1, 3, 4, 2]
Output: 3


Input: [1, 3, 4, 2, 2]
Output: 2

We want a solution that takes O(N) time and O(1) space.

SOLUTIONS

(1) Sum method
Sum(1..N) = sum_n
Sum(array) - sum_n = duplicate_number
Time O(N)
Space O(1)

(2) Sort then linear scan to find duplicate
Time O(N lg N)
Space O(1)

(3) Linear scan and use a Set to store seen values.
Time O(N)
Space O(N)

(4) Since values are positive numbers 1..N, use array indices to mark values we have seen.
Either swap value to its corresponding index, or change the value at the index to negative sign.
Time O(N)
Space O(1)

A more realistic problem would be to find a variable number of duplicates
but the space cost must be relaxed to O(N) to hold the result.
Hence the question asks for a fixed number of duplicates.

References
- https://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/
- https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/
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
