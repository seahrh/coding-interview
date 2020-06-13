"""
You are to implement a one-pass sorting algorithm on integer input array that only has 3
types of elements {0; 1; 2}. An example input is: {0; 1; 1; 1; 0; 0; 1; 2; 2; 0; 2; 1; 1; 2}.
Solve this Dutch National Flag problem using single pass, instead of the naive implementation of 2-pass sorting,
and only allowed to use O(1) extra space (same for next part with 4
unique elements). You are not allowed to use any sort() or sorted() functions from libraries.

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
    p2_head = 0
    p3_head = 0
    i = 0
    p3_tail = len(arr) - 1  # Space O(1)
    while i <= p3_tail:  # Time O(N)
        if arr[i] == 0:
            arr[p2_head], arr[i] = arr[i], arr[p2_head]
            p2_head += 1
            p3_head += 1
            i += 1
            continue
        if arr[i] == 1:
            arr[p3_head], arr[i] = arr[i], arr[p3_head]
            p3_head += 1
            i += 1
            continue
        if arr[i] == 2:
            i += 1
            continue
        if arr[i] == 3:
            arr[p3_tail], arr[i] = arr[i], arr[p3_head]
            p3_tail -= 1
            continue
        raise ValueError("Colours must have the values 0, 1, 2 or 3.")
