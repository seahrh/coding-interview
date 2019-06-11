"""
Permutations without Dups: Write a method to compute all permutations of a string of unique
characters.
(8.7, p367)
"""


def permutate_without_duplicates(remainder):
    """
    There are n recursive calls.
    Inserting the character takes factorial time because there are n! permutations.
    This takes O(n * n!) time and O(n) space.
    """
    res = []
    if len(remainder) == 0:  # base case
        res.append('')
        return res
    head = remainder[0]
    partials = permutate_without_duplicates(remainder[1:])
    for p in partials:
        for i in range(len(p) + 1):  # also insert character at the end of the string!
            res.append(p[:i] + head + p[i:])
    return res
