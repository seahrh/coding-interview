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
- First build a trie of suffixes. Generate all suffixes of the word, then add suffixes to the trie.
- Given a substring, do a prefix match to check if it exists in the trie.
- Find all positions of the substring in O(M) time
- Build the trie in O(M) time

Based on https://www.youtube.com/watch?v=AXjmTQ8LEoI
"""
from typing import Dict, Iterable, List, Optional, Set, Tuple


class Node:
    def __init__(self):
        self.children: Dict[str, "Node"] = {}
        self.end_of_word: bool = False
        # index offset of char in parent string. Only used in suffix tries.
        self.offsets: Set[int] = set()


class Trie:
    def __init__(self, words: Iterable[str]):
        self.root: Node = Node()
        for i, w in enumerate(words):
            self.add(w, offset=i)

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

    def words(self, prefix: str) -> Set[str]:
        """Returns a set of words that match a given prefix.
        This can be used to implement an autocomplete function.
        """
        res: Set[str] = set()
        root = self._tail(prefix)
        if root is None:
            return res
        st: List[Tuple[str, Node]] = [(prefix, root)]
        while len(st) != 0:
            word, node = st.pop()
            if node.end_of_word:
                res.add(word)
            for k, v in node.children.items():
                st.append((word + k, v))
        return res

    def find(self, substring: str) -> Set[int]:
        if substring is None:
            raise ValueError("substring must not be None")
        _len = len(substring)
        if _len == 0:
            return set()
        node = self.root
        for s in substring:
            if s not in node.children:
                return set()
            node = node.children[s]
        # get the offset of the first char in the substring
        return set([i - (_len - 1) for i in node.offsets])

    # TODO remove deprecated
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

    def add(self, word: str, offset: int = 0) -> None:
        node = self.root  # start with the root
        i = offset
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            node.offsets.add(i)
            i += 1
        node.end_of_word = True

    def remove(self, word: str) -> None:
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
