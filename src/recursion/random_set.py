"""
Random Set: Write a method to randomly generate a set of m integers from an array of size n.
Each element must have equal probability of being chosen.

(17.3, p544)
"""
from random import randint


def pick_rec(arr, m, index):
    """We can first pull a random set of size m from the first n - 1 elements.
    Then check if array[n] should be inserted into our subset
    (which would require pulling out a random element from it).
    An easy way to do this is to pick a random number k from e through n.
    If k < m, then replace subset[k] with array[n].
    This will both "fairly" (i.e. with proportional probability)
    insert array[n] into the subset and "fairly" remove a random element from the subset.
    O(n - m) time and O(n + m) space.
    """
    if index + 1 == m:  # base case
        return arr[:m]
    if index + 1 < m:
        raise ValueError("not enough items to fill all m slots")
    res = pick_rec(arr, m, index - 1)
    # let k be an index of the result set
    # any item in result set has equal chance of being replaced
    k = randint(0, index)
    if k < m:  # k must not equal m, else index out of bounds
        res[k] = arr[index]
    return res


def pick(arr, m):
    """O(n - m) time and O(m) space."""
    if m > len(arr):
        raise ValueError("not enough items to fill all m slots")
    res = arr[:m]
    for i in range(m, len(arr)):
        k = randint(0, i)
        if k < m:  # k must not equal m, else index out of bounds
            res[k] = arr[i]
    return res
