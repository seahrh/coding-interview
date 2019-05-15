# Find pairs of elements from an array whose sum equals a given number. The
# array can contain any integer, including zero and negative numbers. The array
# elements are unique.


def pairs(arr, summ):
    # Convert the array into a hashtable where the key is the value of the
    # array element, and the value is the index of the array element. Makes two
    # passes through the array, first to build the hashtable, second to check
    # whether the other sum operand exists.
    #
    # This takes O(n) time and O(n) space.
    if len(arr) == 0:
        raise ValueError('arr must not be empty')
    indices = dict()
    for i, j in enumerate(arr):
        indices[j] = i
    res = set()
    for i, j in enumerate(arr):
        target = summ - j
        k = indices.get(target)
        if k is not None and i != k:  # other number in the pair must not be self
            if k < i:
                res.add((k, i))
            else:
                res.add((i, k))
    return res
