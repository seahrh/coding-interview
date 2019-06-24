"""
Longest Word: Given a list of words, write a program to find the longest word made of other words
in the list.

Assume
- A word could be formed by any number of other words.
- A composed word contains only given words, with no gap in between.

(17.15, p583)
SOLUTION: DP with memoization to cache the results.
O(W lg W + WC) time, where W is number of words and C is number of characters.
O(W + C) space: memo table and depth of call stack
"""


def _is_composed(word, is_original, memo):
    """

    :param word:
    :param is_original: If it is the original word, do not retrieve result from memo table.
    :param memo: memo table to cache the results of previous recurses
    :return: True if this word is composed of other words, False otherwise.
    """
    if not is_original and word in memo:
        return memo[word]
    for i in range(1, len(word)):  # O(C) time
        left = word[:i]
        right = word[i:]
        if left in memo and memo[left] is True and _is_composed(right, False, memo):
            return True
    memo[word] = False
    return False


def longest_word(words):
    memo = {}
    for word in words:
        memo[word] = True
    # start with longest word first, so sort in descending length
    words.sort(key=len, reverse=True)  # O(W lg W) time, sort in-place
    for word in words:  # O(WC) time
        if _is_composed(word, is_original=True, memo=memo):
            return word
    return None
