"""
Write a function to check whether two given strings are anagram of each other or not.
An anagram of a string is another string that contains same characters,
only the order of characters can be different.
For example, “abcd” and “dabc” are anagram of each other.

[CTCI Q1.4]
See https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/

SOLUTION
Sort the strings then compare.
Time O(N lg N)
Space O(1)

Assume charset is UTF-8 ASCII values only. Then faster solution is possible.
In first string, count each character and number of distinct chars. Check this tally in the second string.
Time O(N)
Space O(1): assume charset is of constant size
"""


def is_anagram(s: str, t: str) -> bool:
    if s == "":
        raise ValueError("s must not be empty")
    if t == "":
        raise ValueError("t must not be empty")
    if len(s) != len(t):
        return False
    num_chars = 128
    counts = [0] * num_chars
    uniques = 0
    for c in s:
        cp = ord(c)
        if counts[cp] == 0:
            uniques += 1
        counts[cp] += 1
    for c in t:
        cp = ord(c)
        if counts[cp] == 0:
            return False
        counts[cp] -= 1
        if counts[cp] == 0:
            uniques -= 1
            if uniques == 0:  # all chars accounted for
                return True
    return False
