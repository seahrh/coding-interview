"""
Diving Board: You are building a diving board by placing a bunch of planks of wood end-to-end.
There are two types of planks, one of length shorter and one of length longer. You must use
exactly K planks of wood. Write a method to generate all possible lengths for the diving board.
(16.11, p497)
"""

from typing import Set


def all_lengths_rec(k: int, shorter: int, longer: int) -> Set[int]:
    """Recursive solution
    O(k) time and O(k) space (to store the result)
    """
    if k < 1:
        raise ValueError("k must not be less than 1")
    if k == 1:  # base case
        return {shorter, longer}
    res = set()
    for _len in all_lengths_rec(k - 1, shorter, longer):
        res.add(_len + shorter)
        res.add(_len + longer)
    return res


def all_lengths(k: int, shorter: int, longer: int) -> Set[int]:
    """Iterative solution
    We just need to go through all unique sets of K planks (sets, not orders!).
    There are only K ways of picking K planks if we only have two possible types:
    {O of type A, K of type B}, {1 of type A, K -1 of type B}, {2 of type A, K - 2 of type B}, ...
    O(k) time and O(k) space (to store the result)
    """
    if k < 1:
        raise ValueError("k must not be less than 1")
    res = set()
    for n_shorter in range(k + 1):
        _len = n_shorter * shorter + (k - n_shorter) * longer
        res.add(_len)
    return res
