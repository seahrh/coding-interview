"""
Trie implementation: tree built on nested hash tables.
If the charset is fixed, hash tables can be replaced with arrays.
Based on https://www.youtube.com/watch?v=AXjmTQ8LEoI

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self, words):
        """This takes O(nm) time, where n is the number of words and m is the length of the word.
        """
        self.root = TrieNode()
        for w in words:
            node = self.root  # reset to root for each word
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.end_of_word = True

    def __contains__(self, item):
        """This takes O(m) time, where m is the length of the word."""
        node = self.root
        for c in item:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    def add(self, word):
        # TODO
        raise NotImplementedError()

    def remove(self, word):
        # TODO
        raise NotImplementedError()
