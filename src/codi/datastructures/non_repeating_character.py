"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

SOLUTION
We scan the string from left to right counting the number occurrences of each character in a hashtable.
Then we perform a second pass and check the counts of every character.
Whenever we hit a count of 1 we return that character, that’s the first unique letter.

Time O(N)
Space O(N)
"""

from collections import defaultdict
from typing import DefaultDict


def first_non_repeating_character(s: str) -> int:
    if s is None:
        raise ValueError("string must not be None.")
    counts: DefaultDict[str, int] = defaultdict(int)
    for c in s:
        counts[c] += 1
    for i, c in enumerate(s):
        if counts[c] == 1:
            return i
    # all chars are repeating
    return -1
