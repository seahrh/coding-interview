# Quicksort is a comparison in-place sort.
# It is not a stable sort.


def lomuto_partition(arr, lo, hi):
    # Return the last index of the left partition, and the first index of the right partition.
    # Picks the last element as the pivot
    # All elements less than or equals the pivot, move to the left by swapping
    # i is the final position of the pivot
    pivot = arr[hi]
    i = lo
    j = lo
    while j < hi:  # no need to cover the last element
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[i], arr[j] = arr[j], arr[i]
    return i - 1, i + 1


def hoare_partition(arr, lo, hi):
    # Return the last index of the left partition, and the first index of the right partition.
    # Hoare's scheme is more efficient than Lomuto's partition scheme because
    # it does three times fewer swaps on average,
    # and it creates efficient partitions even when all values are equal.
    # Like Lomuto, Hoare's partitioning scheme also degrades to O(n^2) for already sorted arrays.
    pivot = arr[int((hi - lo) / 2 + lo)]
    i = lo - 1
    j = hi + 1
    while True:
        # do-while loop forces cursor to move if all elements equal pivot
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j, j + 1
        arr[i], arr[j] = arr[j], arr[i]


def _quicksort(arr, lo, hi, partition_fn):
    # Base case: array of length one
    if lo < hi:
        last_index_of_left_partition, first_index_of_right_partition = partition_fn(arr=arr, lo=lo, hi=hi)
        _quicksort(arr, lo, last_index_of_left_partition, partition_fn)
        _quicksort(arr, first_index_of_right_partition, hi, partition_fn)


def quicksort(arr, partition_fn=lomuto_partition):
    if len(arr) == 0:
        raise ValueError('arr must not be empty')
    _quicksort(arr, 0, len(arr) - 1, partition_fn)
