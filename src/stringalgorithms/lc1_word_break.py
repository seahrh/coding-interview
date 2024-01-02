"""
139. Word Break https://leetcode.com/problems/word-break/description/

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

SOLUTION
Trie and DP
W is number of words in dictionary and K is the average length of a dictionary word.
Time O(WK): search one string that contains all dictionary words; visit every node in the trie
Space O(WK): build trie
References
- https://leetcode.com/problems/word-break/solutions/2722114/python-trie-solution-beats-80-simple-recursive/
"""
from typing import Dict, List


class TrieNode:
    def __init__(self):
        self.chi: Dict[str, "TrieNode"] = {}
        self.end: bool = False


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

    def segment(self, word: str) -> bool:
        dp = {}

        def rec(node, word, i) -> bool:
            nonlocal dp
            if i == len(word):
                return node.end
            if node.end:
                r = word[i:]
                if r not in dp:
                    dp[r] = rec(self.root, word, i)
                if dp[r]:
                    return True
            if word[i] not in node.chi:
                return False
            return rec(node.chi[word[i]], word, i + 1)

        return rec(self.root, word, i=0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tr = Trie()
        for w in wordDict:
            tr.insert(w)
        return tr.segment(s)
