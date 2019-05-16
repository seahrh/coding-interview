# Design an algorithm and write code to remove the duplicate characters in
# a string without using any additional buffer. NOTE: One or two additional
# variables are fine. An extra copy of the array is not. [CTCI Q1.3]


def remove_duplicates(s):
    # This takes O(n) time and O(m) space, where m is the number of unique chars.
    # assume UTF-8 ASCII charset only
    num_chars = 128
    flags = [False] * num_chars
    res = ''
    for c in s:
        cp = ord(c)
        if flags[cp] is False:
            res += c
            flags[cp] = True
    return res
