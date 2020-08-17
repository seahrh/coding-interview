from typing import List


def search(arr: List[int], key: int) -> int:
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = int(lo / 2 + hi / 2)  # avoid integer overflow
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            lo = mid + 1
            continue
        hi = mid - 1
    return -1


def search_array_with_empty_strings(arr: List[str], key: str) -> int:
    # Search a sorted array of strings which is interspersed with empty strings.
    # [CTCI Q9.5]
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        # ensure there is something at the end
        while lo <= hi and arr[hi] == "":
            hi -= 1
        if hi < lo:
            return -1
        mid = int(lo / 2 + hi / 2)  # avoid integer overflow
        # Keep going right until a non-empty string is found
        while arr[mid] == "":
            mid += 1
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            lo = mid + 1
            continue
        hi = mid - 1
    return -1


def nearest(arr: List[int], key: int) -> int:
    lo = 0
    hi = len(arr) - 1
    res = 0
    while lo <= hi:
        mid = int(lo / 2 + hi / 2)  # avoid integer overflow
        if arr[mid] == key:
            return mid
        if abs(arr[mid] - key) < abs(arr[res] - key):
            res = mid
        if key > arr[mid]:
            lo = mid + 1
            continue
        hi = mid - 1
    return res
