from math import fabs


def search(arr, key):
    if len(arr) == 0:
        raise ValueError('arr must not be empty')
    begin = 0
    end = len(arr) - 1
    while begin <= end:
        mid = int((end - begin) / 2 + begin)  # avoid integer overflow
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            begin = mid + 1
            continue
        if key < arr[mid]:
            end = mid - 1
    return -1


def search_array_with_empty_strings(arr, key):
    # Search a sorted array of strings which is interspersed with empty strings.
    # [CTCI Q9.5]
    if len(arr) == 0:
        raise ValueError('arr must not be empty')
    begin = 0
    end = len(arr) - 1
    while begin <= end:
        # ensure there is something at the end
        while begin <= end and arr[end] == '':
            end -= 1
        if end < begin:
            return -1
        mid = int((end - begin) / 2 + begin)  # avoid integer overflow
        # Keep going right until a non-empty string is found
        while arr[mid] == '':
            mid += 1
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            begin = mid + 1
            continue
        if key < arr[mid]:
            end = mid - 1
    return -1


def nearest(arr, key):
    if len(arr) == 0:
        raise ValueError('arr must not be empty')
    begin = 0
    end = len(arr) - 1
    res = 0
    while begin <= end:
        mid = int((end - begin) / 2 + begin)  # avoid integer overflow
        if arr[mid] == key:
            return mid
        if fabs(arr[mid] - key) < fabs(arr[res] - key):
            res = mid
        if key > arr[mid]:
            begin = mid + 1
            continue
        if key < arr[mid]:
            end = mid - 1
    return res
