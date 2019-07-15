"""
Multi Search: Given a string b and an array of smaller strings T, design a method to search b for
each small string in T.

Return a hash table where the key is a small string T and the value is an array of indexes
where T can be found in b.

(17.17, p589)
SOLUTION
1. Use big string to construct a suffix tree.
2. Use small strings to construct a trie (prefix tree).
"""
from collections import defaultdict
from trees.trie import *


def multisearch(big, smalls):
    res = defaultdict(list)
    maxlen = len(big)
    trie = Trie(smalls)
    return res


def multisearch_with_bstrie(big, smalls):
    res = defaultdict(list)
    trie = BigStringTrie()
    for i in range(len(big)):
        trie.insert(big[i:], i)  # insert suffix
    for s in smalls:
        indexes = trie.search(s)
        _normalize(indexes, len(s))  # adjust to starting index
        res[s] = indexes
    return res


def _normalize(indexes, delta):
    if indexes is None:
        return
    for i in range(len(indexes)):
        indexes[i] = indexes[i] - delta


class BigStringTrieNode:
    def __init__(self, terminator):
        self.value = None
        self.children = {}  # map from character to BigStringTrieNode
        self.indexes = []
        self.terminator = terminator

    def terminates(self):
        return self.terminator in self.children

    def child(self, char):
        return self.children.get(char, None)

    def search(self, string):
        if len(string) == 0:
            return self.indexes
        head = string[0]
        if head in self.children:
            remainder = string[1:]
            return self.children[head].search(remainder)
        return []

    def insert(self, string, index):
        self.indexes.append(index)
        if string is None or len(string) == 0:
            self.children[self.terminator] = None
            return
        self.value = string[0]
        child = None
        if self.value in self.children:
            child = self.children[self.value]
        else:
            child = BigStringTrieNode(terminator=self.terminator)
            self.children[self.value] = child
        remainder = string[1:]
        child.insert(remainder, index + 1)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.__dict__)


class BigStringTrie:
    def __init__(self, string=None, terminator='*'):
        self.root = BigStringTrieNode(terminator=terminator)
        if string is not None:
            self.root.insert(string, 0)

    def search(self, string):
        return self.root.search(string)

    def insert(self, string, index):
        self.root.insert(string, index)

    def __repr__(self):
        return repr(self.root)
