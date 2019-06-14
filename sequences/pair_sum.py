# Find pairs of elements from an array whose sum equals a given number. The
# array can contain any integer, including zero, negative numbers and duplicates.
# Return all pairs.
from collections import defaultdict


def pair_sum(arr, summ):
    """Returns a set of pairs (therefore no duplicate pairs).
    Builds a hash table where key is a complement and value is the number of times
    that this complement can be added to a valid pair.
    Requires only one pass because addition is commutative
    i.e. order of operands does not matter.

    This takes O(n) time and O(n) space.
    """
    res = set()
    unpaired_count = defaultdict(int)
    for v in arr:
        complement = summ - v
        if unpaired_count[v] > 0:  # current value is a matching complement
            if v < complement:
                res.add((v, complement))
            else:
                res.add((complement, v))
            unpaired_count[v] -= 1
            continue
        unpaired_count[complement] += 1
    return res


# Same problem as above, but suppose array is already sorted.


def pair_sum_sorted(arr, summ):
    """Let first point to the head of the array and last point to the end of the array.
    To find the complement of first,we just move last backwards until we find it.

    Why must this find all complements for first? Because the array is sorted and we're trying progressively
    smaller numbers. When the sum of first and last is less than the sum, we know that trying even smaller
    numbers won't help us find a complement.

    Why must this find all complements for last? Because all pairs must be made up of a first and a last.
    We've found all complements for first, therefore we've found all complements of last.

    O(n) time and O(n) space (to hold the result).
    """
    res = set()
    i = 0
    j = len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == summ:
            if arr[i] < arr[j]:
                res.add((arr[i], arr[j]))
            else:
                res.add((arr[j], arr[i]))
            i += 1
            j -= 1
            continue
        # we need a bigger sum so move left pointer to a greater number
        if s < summ:
            i += 1
        else:  # we need a smaller sum so move right pointer to a smaller number
            j -= 1
    return res


# Same problem as above but simpler:
# Return True if pair is found, False otherwise.
#
# Based on https://youtu.be/XKu_SEDAykw

def has_pair_sum(arr, summ):
    """Build a set to store the complements. If complement exists, then the pair is found.

    This takes O(n) time and O(n) space."""
    if len(arr) == 0:
        raise ValueError('arr must not be empty')
    complements = set()
    for v in arr:
        if v in complements:
            return True
        complements.add(summ - v)
    return False
