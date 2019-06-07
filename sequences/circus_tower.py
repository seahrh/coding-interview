# A circus is designing a tower routine consisting of people standing atop one
# another’s shoulders. For practical and aesthetic reasons, each person must be
# both shorter and lighter than the person below him or her. Given the heights
# and weights of each person in the circus, write a method to compute the
# largest possible number of people in such a tower. [CTCI Q9.7]
#
# EXAMPLE: Input (ht, wt): (65, 100) (70, 150) (56, 90) (75, 190) (60, 95) (68, 110)
#
# Output: The longest tower is length 6 and includes from top to bottom:
# (56, 90) (60,95) (65,100) (68,110) (70,150) (75,190)


from collections import namedtuple
from functools import cmp_to_key

Person = namedtuple('Person', ['h', 'w'])


def _person_in_descending_order_cmp(left, right):
    if left.h > right.h:
        return -1
    if left.h < right.h:
        return 1
    if left.w > right.w:
        return -1
    if left.w < right.w:
        return 1
    return 0


def tower_length(persons):
    """Find the length of the maximum non-increasing subsequence.

    First, sort the persons by height, then weight.
    a) Start at the beginning of the sequence. Currently, max_sequence is empty.
    b) If, for the next item, the height and the weight is not greater
    than those of the previous item, we mark this item as “unfit” .
    (60,95), (65,100) (75,80) (80, 100) (unfit item)
    c) If the sequence found has more items than “max sequence”, it becomes “max sequence”.
    d) After that the search is repeated from the “unfit item”,
    until we reach the end of the original sequence.

    Solution takes O(n lg n) time and O(n) space.
    """
    # O(1) space: sort in place
    persons.sort(key=cmp_to_key(_person_in_descending_order_cmp))
    res = 0
    tmp = []  # O(n) space
    for p in persons:  # O(n) time
        if len(tmp) == 0:
            tmp.append(p)
            continue
        if p.h < tmp[-1].h and p.w < tmp[-1].w:
            tmp.append(p)
            continue
        if len(tmp) > res:
            res = len(tmp)
        tmp = [p]
    if len(tmp) > res:
        res = len(tmp)
    return res
