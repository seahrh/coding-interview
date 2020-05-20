"""
Letters and Numbers: Given an array filled with letters and numbers, find the longest subarray with
an equal number of letters and numbers.

(17.5, p547)
Solution:
Study the numbers before the subarray (4, 2) and the end (7, 5).
You might notice that, while the values aren't the same,
the differences are: 4 - 2 = 7 - 5. This makes sense.
Since they've added the same number of letters and numbers,
they should maintain the same difference.

Whenever we return the same difference, then we know we have found an equal subarray.
To find the biggest subarray, we just have to find the two indices
farthest apart with the same value.

To do so, we use a hash table to store the first time we see a particular difference.
Then, each time we see the same difference, check if this subarray is longer than the current max.
If so, we update the max.

O(n) time and O(n) space (to hold the deltas and result).
"""


def _deltas(arr, is_left, is_right):
    """Get the difference between the number of letters and numbers between the
    beginning of the array and each index."""
    res = []
    d = 0
    for v in arr:
        if is_left(v):
            d += 1
        elif is_right(v):
            d -= 1
        else:
            raise ValueError("char does not belong to any group")
        res.append(d)
    return res


def _longest_match(deltas):
    """Find the matching pair of values in the deltas array
    with the largest difference in indices.

    Returns tuple (lo, hi), not inclusive of hi
    """
    _map = {0: -1}  # seed distance zero at index -1
    res = None
    for index, d in enumerate(deltas):
        if d in _map:
            i = _map[d] + 1
            distance = index - i + 1
            if (res is None and distance > 0) or (
                res is not None and distance > res[1] - res[0]
            ):
                res = (i, index + 1)
            continue
        _map[d] = index
    return res


def longest_balanced_subsequence(arr, is_left, is_right):
    """
    :param arr: array of characters belonging to either LEFT or RIGHT groups
    :param is_left: function to determine if char belongs to LEFT group
    :param is_right: function to determine if char belongs to RIGHT group
    :return: matching subsequence, None otherwise.
    """
    indices = _longest_match(_deltas(arr, is_left, is_right))
    if indices is None:
        return None
    return arr[indices[0] : indices[1]]
