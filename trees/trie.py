"""
Trie (prefix tree) implementation: nested hash tables.
If the charset is fixed, hash tables can be replaced with arrays.
Trie is used for prefix and whole-string matching.
Constructing a trie takes O(nm) time,
where n is the number of words and m is the length of the longest word.
Based on https://www.youtube.com/watch?v=AXjmTQ8LEoI

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            self.add(w)

    def __contains__(self, item):
        """This takes O(m) time and O(1) space."""
        node = self.root
        for c in item:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    def add(self, word):
        node = self.root  # reset to root for each word
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True

    def remove(self, word):
        """This takes O(m) time and O(1) space."""
        node = self.root
        path = [node]
        for c in word:
            if c not in node.children:
                return  # no-op
            node = node.children[c]
            path.append(node)
        if not node.end_of_word:
            return  # no-op
        while len(path) != 0:
            node = path.pop()
            if node.end_of_word:
                continue
            # index of the popped node
            del node.children[word[len(path)]]
