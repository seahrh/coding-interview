"""
Pattern Matching: You are given two strings, pattern and value. The pattern string consists of
just the letters a and b, describing a pattern within a string. For example, the string "catcatgocatgo"
matches the pattern "aabab" (where cat is a and go is b). It also matches patterns like a, ab, and b.
Write a method to determine if value matches pattern.

(16.18, p511)

SOLUTION: Backtracking
N is length of `value` string and length of pattern can't exceed N.
Time O(N^2)
Space O(N)
"""


def _matches(
    pattern: str, value: str, main_size: int, alt_size: int, first_alt: int
) -> bool:
    """Return True if value matches pattern, False otherwise.
    The main and alternate pattern strings are known.

    :param pattern: pattern to match
    :param value: string
    :param main_size: length of the main pattern
    :param alt_size: length of the alternate pattern
    :param first_alt: beginning index of the first occurrence of the alternate pattern in `value`
    :return: True if value matches pattern, False otherwise.
    """
    # Let i be the index of `pattern` and j be index of `value`.
    v = main_size
    main = value[:main_size]  # worst case O(N) space
    alt = value[first_alt : first_alt + alt_size]
    for p in range(1, len(pattern)):
        is_main = pattern[p] == pattern[0]
        size = main_size if is_main else alt_size
        _next = value[v : v + size]
        if is_main and main != _next:
            return False
        if not is_main and alt != _next:
            return False
        v += size
    return True


def matches(pattern: str, value: str) -> bool:
    if pattern is None or len(pattern) == 0:
        raise ValueError("pattern must not be empty string")
    if value is None or len(value) == 0:
        return False
    main = pattern[0]
    alt = "b" if main == "a" else "a"
    n_main = pattern.count(main)
    n_alt = len(pattern) - n_main
    first_alt: int = pattern.find(alt)
    max_main_size = int(len(value) / n_main)  # round down
    for main_size in range(1, max_main_size + 1):
        remainder = len(value) - main_size * n_main
        if n_alt == 0 or remainder % n_alt == 0:
            # index of first `alt` substring occurs after how many repetitions of `main` substring
            alt_index = first_alt * main_size
            alt_size = 0 if n_alt == 0 else int(remainder / n_alt)  # round down
            if _matches(pattern, value, main_size, alt_size, alt_index):
                return True
    return False
