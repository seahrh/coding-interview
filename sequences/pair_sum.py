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
