"""
720. Longest Word in Dictionary https://leetcode.com/problems/longest-word-in-dictionary/description/

Given an array of strings words representing an English Dictionary,
return the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.
Note that the word should be built from left to right with each additional character being added to the end of a previous word.
Example 1:
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.

SOLUTION
References
- https://leetcode.com/problems/longest-word-in-dictionary/solutions/113916/python-trie-bfs/
"""
from collections import deque
from typing import Deque, Dict, List


class TrieNode:
    def __init__(self):
        self.chi: Dict[str, "TrieNode"] = {}
        self.end: bool = False
        self.word: str = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.chi:
                curr.chi[c] = TrieNode()
            curr = curr.chi[c]
        curr.end = True
        curr.word = word

    def bfs(self) -> str:
        q: Deque[TrieNode] = deque([self.root])
        res = ""
        while len(q) != 0:
            cur = q.popleft()
            for c in cur.chi.values():
                if c.end:
                    q.append(c)
                    if len(c.word) > len(res):
                        res = c.word
                    elif len(c.word) == len(res) and c.word < res:
                        res = c.word
        return res


class Solution:
    def longestWord(self, words: List[str]) -> str:
        tr = Trie()
        for w in words:
            tr.insert(w)
        return tr.bfs()
