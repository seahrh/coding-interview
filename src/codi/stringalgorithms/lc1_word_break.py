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
1. Why use a Trie?

A Trie (prefix tree) allows us to check prefixes efficiently while traversing s.
Instead of re-scanning the dictionary for every substring, we can explore valid word paths directly.
This avoids repeated substring operations and speeds up lookups significantly
when many dictionary words share prefixes (like cat, cater, catering).

2. DFS + Memoization

We use dfs(index) to test if substring s[index:] can be segmented.
At each step:
Start from the Trie root.
Traverse character by character.
Each time you hit a Trie node with is_end=True, it means you’ve matched a valid word,
now recursively check if the remaining substring can be segmented.
Memoization (memo[index]) stores results for each index to prevent recomputation.

3. Base & Termination Conditions

Base case: If index == len(s), we’ve successfully segmented the entire string → return True.
Failure case: If we exhaust the Trie without finding a valid path → return False.

4. Complexity Analysis

Let N = length of the string s
W = number of words in dictionary
K = average word length
Building the Trie:
O(W * K) time and space.
DFS Traversal:
At most O(N²) calls in the worst case (if all prefixes are valid words),
but typically much less thanks to memoization and Trie pruning.
Overall:
✅ Average case ≈ O(WK + N²)
✅ Space ≈ O(WK + N) (Trie + memo)

4.1 What’s happening in the DFS?

We recursively call dfs(index) to check if the substring s[index:] can be segmented.
At each call:
We start from index
We try every possible end position for a valid word that begins at index
For each position i from index to len(s) - 1, we check s[index:i+1] (a prefix substring)
Each recursive step can, in the worst case, iterate over up to N - index characters.

4.2 How many distinct DFS calls are there?

Because of memoization, we call dfs(index) at most once per index.
There are N possible start positions (0 to N-1).
So we have O(N) distinct recursive calls.

4.3. What does each call cost?

Inside each call dfs(index):
We iterate forward through the string:
for i in range(index, len(s))
That loop can run up to N - index times.
If we sum that across all possible index, we get: N*(N+1)/2
That’s O(N²) total character checks across all recursive calls.

4.4 Why not worse than O(N²)?

Because of memoization, we never recompute a state once it’s known.
Even if there are multiple word paths that reach the same index, we just look up the result from memo[index].
So we don’t multiply by the number of dictionary words — we only pay once per character position.

5. Intuition Recap
Imagine walking along the string s, with the Trie as a map of “valid word paths.”
Each time you reach a valid endpoint in the Trie, you can either:
Stop there (marking a word boundary), or
Keep going to find longer matches.
If any full segmentation path reaches the end of the string, the function returns True.
"""

from typing import Dict, List


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.end: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end = True

    def segment(self, s: str) -> bool:
        """Return True if string s can be segmented into dictionary words."""
        memo: Dict[int, bool] = {}

        def dfs(index: int) -> bool:
            """Return True if substring s[index:] can be segmented."""
            # If we've consumed the entire string, it's valid
            if index == len(s):
                return True
            if index in memo:
                return memo[index]
            node = self.root
            for i in range(index, len(s)):
                ch = s[i]
                if ch not in node.children:
                    break  # no further path in Trie
                node = node.children[ch]
                # Found a valid word ending here; recurse for the remainder
                if node.end and dfs(i + 1):
                    memo[index] = True
                    return True
            memo[index] = False
            return False

        return dfs(0)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tr = Trie()
        for w in wordDict:
            tr.insert(w)
        return tr.segment(s)
