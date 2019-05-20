# Quicksort is a comparison in-place sort.
# It is not a stable sort.


def lomuto_partition(arr, lo, hi):
    # Picks the last element as the pivot
    # All elements less than or equals the pivot, move to the left by swapping
    # i is the final position of the pivot
    # Return the last index of the left partition, and the first index of the right partition
    pivot = arr[hi]
    i = lo
    j = lo
    while j < hi:  # no need to cover the last element
        if arr[j] <= pivot:
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp
            i += 1
        j += 1
    tmp = arr[i]
    arr[i] = pivot
    arr[hi] = tmp
    return i - 1, i + 1


def _quicksort(arr, lo, hi, partition_fn):
    # Base case: array of length one
    if lo < hi:
        last_index_of_left_partition, first_index_of_right_partition = partition_fn(arr=arr, lo=lo, hi=hi)
        _quicksort(arr, lo, last_index_of_left_partition, partition_fn)
        _quicksort(arr, first_index_of_right_partition, hi, partition_fn)


def quicksort(arr, partition_fn=lomuto_partition):
    _quicksort(arr, 0, len(arr) - 1, partition_fn)
