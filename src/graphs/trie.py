"""
Trie (prefix tree) implementation: nested hash tables.
If the charset is fixed, hash tables can be replaced with arrays.
Pros: efficient prefix queries
Cons: less space efficient than a set
Trading space for time
N is the number of words and M is the length of the longest word.
COSTS
- Insert O(M)
- Lookup O(M)
- Space O(NM)

SUBSTRING MATCHING
- Besides prefix and whole-string matching, trie can also be used for substring matching.
- Idea: prefix matching the suffixes of a word
- First build a trie of suffixes. Generate all suffixes from each word, then add suffixes to the trie.
- Given a substring, do a prefix match to check if it exists in the trie.
- Substring matching in O(M) time
- Build the trie in O(NM) time

Based on https://www.youtube.com/watch?v=AXjmTQ8LEoI
"""
from typing import Dict, Iterable, List, Optional


class Node:
    def __init__(self):
        self.children: Dict[str, "Node"] = {}
        self.end_of_word: bool = False


class Trie:
    def __init__(self, words: Iterable[str]):
        self.root: Node = Node()
        for w in words:
            self.add(w)

    def _tail(self, prefix: str) -> Optional[Node]:
        """Returns the last node of the prefix if prefix exists in the trie. Else return None.
        This takes O(m) time and O(1) space."""
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def __contains__(self, prefix: str) -> bool:
        """Returns True if prefix exists in the trie.
        This takes O(m) time and O(1) space."""
        return self._tail(prefix) is not None

    # TODO remove
    def prefixes(self, string: str) -> List[str]:
        """Returns the words in the trie that share the same prefixes as the input string.
        This takes O(m) time and O(m) space, where m is length of input string.
        """
        res = []
        node = self.root
        for i, c in enumerate(string):
            if c not in node.children:
                break
            node = node.children[c]
            if node.end_of_word:
                res.append(string[: i + 1])  # includes the ith char!
        return res

    def add(self, word: str) -> None:
        node = self.root  # start with the root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
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
