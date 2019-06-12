"""
Diving Board: You are building a diving board by placing a bunch of planks of wood end-to-end.
There are two types of planks, one of length shorter and one of length longer. You must use
exactly K planks of wood. Write a method to generate all possible lengths for the diving board.
(16.11, p497)
"""


def all_lengths_rec(k, shorter, longer):
    """Recursive solution
    O(k) time and O(2^k) space (to store the result)
    """
    if k < 1:
        raise ValueError('k must not be less than 1')
    if k == 1:
        return {shorter, longer}
    res = set()
    for l in all_lengths_rec(k - 1, shorter, longer):  #
        res.add(l + shorter)
        res.add(l + longer)
    return res
