# Characteristics of mergesort
# Mergesort takes O(n) space but quicksort takes less space O(lg n).
# stable sort
# not in-place


def mergesort(arr):
    # Base case: empty array or array of length 1
    if len(arr) < 2:
        return
    mid = int(len(arr) / 2)
    left = list(arr[:mid])
    right = list(arr[mid:])
    mergesort(left)
    mergesort(right)
    _merge(left, right, arr)


def _merge(left, right, arr):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
