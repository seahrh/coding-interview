# Write a method that takes O(n) time to decide if two strings are anagrams or not.
# [CTCI Q1.4]
# Assume charset is UTF-8 ASCII values only.


def is_anagram(s, t):
    # This takes O(s + t) time and O(1) space.
    if s == '':
        raise ValueError('s must not be empty')
    if t == '':
        raise ValueError('t must not be empty')
    if len(s) != len(t):
        return False
    num_chars = 128
    counts = [0] * num_chars
    for c in s:
        cp = ord(c)
        counts[cp] += 1
    for c in t:
        cp = ord(c)
        if counts[cp] == 0:
            return False
        counts[cp] -= 1
    # check non-zero counts remaining
    return sum(counts) == 0
