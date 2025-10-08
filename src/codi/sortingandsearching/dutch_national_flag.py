"""
You are to implement a one-pass sorting algorithm on integer input array that only has 3
types of elements {0; 1; 2}. An example input is: {0; 1; 1; 1; 0; 0; 1; 2; 2; 0; 2; 1; 1; 2}.
Solve this Dutch National Flag problem using single pass, instead of the naive implementation of 2-pass sorting,
and only allowed to use O(1) extra space (same for next part with 4
unique elements). You are not allowed to use any sort() or sorted() functions from libraries.

SOLUTION
Four colours problem
Maintain four indices:
- p2_head, the first '1'
- p3_tail, the last '2'
- i the first element of the unprocessed region
- j the last element of the unprocessed region

0 0 1 1 _ _ _ _ 2 2 3 3
        ^
If current value is
- '0', swap the first '1' with i
- '1', do nothing
- '2', swap i and j
- '3', swap the last '2' with j. Then swap i with the p3_tail position.

See https://stackoverflow.com/a/3436595/519951
"""

from typing import List


def dutch_sort(arr: List[int]) -> None:
    # head and tail refer to the middle partition.
    head = 0
    i = 0
    tail = len(arr) - 1  # Space O(1)
    while i <= tail:  # Time O(N)
        if arr[i] == 0:
            arr[head], arr[i] = arr[i], arr[head]
            head += 1
            i += 1
            continue
        if arr[i] == 1:
            i += 1
            continue
        if arr[i] == 2:
            arr[tail], arr[i] = arr[i], arr[tail]
            tail -= 1
            continue
        raise ValueError("Colours must have the values 0, 1 or 2.")


def dutch_sort_four_colors(arr: List[int]) -> None:
    # There are four partitions: p0, p1, p2, p3 named after the values they hold.
    # p1_head and p2_tail mark the ends of the middle two partitions (p1, p2).
    # i and j mark the ends of the unprocessed region.
    # Space O(1)
    p1_head = 0
    p2_tail = len(arr) - 1
    j = len(arr) - 1
    i = 0
    while i <= j:  # Time O(N)
        if arr[i] == 0:
            arr[p1_head], arr[i] = arr[i], arr[p1_head]
            p1_head += 1
            i += 1
            continue
        if arr[i] == 1:
            i += 1
            continue
        if arr[i] == 2:
            arr[j], arr[i] = arr[i], arr[j]
            j -= 1
            continue
        if arr[i] == 3:
            arr[p2_tail], arr[j] = arr[j], arr[p2_tail]
            # do not swap again if this is the last element of the unprocessed region
            if i != j:
                arr[p2_tail], arr[i] = arr[i], arr[p2_tail]
            j -= 1
            p2_tail -= 1
            continue
        raise ValueError("Colours must have the values 0, 1, 2 or 3.")
