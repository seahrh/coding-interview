"""
Re-Space: Oh, no! You have accidentally removed all spaces, punctuation, and capitalization in a
lengthy document. A sentence like "I reset the computer. It still didn't boot!"
became "iresetthecomputeritstilldidntboot":
You'll deal with the punctuation and capitalization later;
right now you need to re-insert the spaces. Most of the words are in a dictionary but
a few are not. Given a dictionary (a list of strings) and the document (a string), design an algorithm
to unconcatenate the document in a way that minimizes the number of unrecognized characters.

EXAMPLE
Input: jesslookedjustliketimherbrother
Output: jess looked just like tim her brother (7 unrecognized characters)
        ____                  ___

(17.13, p575)
SOLUTION
After we choose the first space, we can recursively pick the second space, then the third space, and so on,
until we are done with the string.

Memoization (caching) to avoid recomputing recursive paths that are overlapping.

We don't need a hash table in this case because the start index is the key.

O(n^2) time and O(n) space, where n is the number of characters.
"""
import sys
from collections import namedtuple

ParseResult = namedtuple("ParseResult", "n_invalid parsed")


def _split(dictionary, text, start, memo, separator=" "):
    if start >= len(text):  # base case
        return ParseResult(n_invalid=0, parsed="")
    if memo[start] is not None:
        return memo[start]
    _min = sys.maxsize
    parsed = None
    partial = ""
    for i in range(start, len(text)):  # O(n) time
        partial += text[i]
        n_invalid = 0 if partial in dictionary else len(partial)
        # short circuit: skip this recursive path
        # if the current number of invalid chars is worse than the best option
        if n_invalid < _min:
            # recurse, putting a space after this char
            # update the best option if necessary
            res = _split(dictionary, text, i + 1, memo, separator)  # O(n) time
            n_invalid += res.n_invalid
            if n_invalid < _min:
                _min = n_invalid
                parsed = partial + separator + res.parsed
                if _min == 0:  # short circuit
                    break
    memo[start] = ParseResult(n_invalid=_min, parsed=parsed)
    return memo[start]


def split(dictionary, text, separator=" "):
    res = _split(dictionary, text, 0, memo=[None] * len(text), separator=separator)
    return None if res is None else res.parsed.strip()
