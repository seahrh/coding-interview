"""
Word Rectangle: Given a list of millions of words, design an algorithm to create the largest possible
rectangle of letters such that every row forms a word (reading left to right) and every column forms
a word (reading top to bottom). The words need not be chosen consecutively from the list, but all
rows must be the same length and all columns must be the same height.

(17.25, p629)
"""
from collections import defaultdict


class Trie:
    def __init__(self, *words, terminator='$'):
        self.root = {}
        self.terminator = terminator
        for w in words:
            curr = self.root
            for c in w:
                curr = curr.setdefault(c, {})
            curr[self.terminator] = self.terminator

    def contains(self, word):
        curr = self.root
        if len(word) == 0:
            return self.terminator in curr
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return True


def _max_length(words):
    _max = 0
    for w in words:
        if len(w) > _max:
            _max = len(w)
    return _max


def _group_by_length(words):
    res = defaultdict(list)  # O(W) space
    for w in words:  # O(W) time
        res[len(w)].append(w)
    return res


def _column_word(matrix, index):
    res = ''
    for row in range(len(matrix)):
        res += matrix[row][index]
    return res


def _validate_columns(matrix, words):
    for i in range(len(matrix[0])):
        word = _column_word(matrix, i)
        if word not in words:
            return False
    return True


def _validate_partial_columns(matrix, trie):
    for i in range(len(matrix[0])):
        word = _column_word(matrix, i)
        if not trie.contains(word):
            return False
    return True


def _rectangle(length, height, word_groups, tries):
    if length not in word_groups or height not in word_groups:
        return None
    if height not in tries:
        tries[height] = Trie(word_groups[height])
    return _build(length, height, word_groups, tries, rectangle=[])


def _build(length, height, word_groups, tries, rectangle):
    #print('_build(rectangle={})'.format(rectangle))
    if len(rectangle) == height:  # base case: rectangle built up to full height
        if _validate_columns(rectangle, word_groups[height]):
            return rectangle
        return None
    if len(rectangle) != 0 and not _validate_partial_columns(rectangle, tries[height]):
        return None
    for word in word_groups[length]:
        taller = list(rectangle)
        taller.append(list(word))
        taller = _build(length, height, word_groups, tries, taller)
        if taller is not None:
            return taller
    return None


def largest_word_rectangle(words):
    max_len = _max_length(words)  # O(W) time
    lwmap = _group_by_length(words)  # O(W) time
    tries = {}
    max_area = max_len * max_len
    for area in range(max_area, 0, -1):
        for length in range(1, max_len + 1):
            if area % length != 0:  # height must be an integer
                continue
            height = area / length
            if height <= max_len:
                res = _rectangle(length, height, word_groups=lwmap, tries=tries)
                if res is not None:
                    return res
    return []
