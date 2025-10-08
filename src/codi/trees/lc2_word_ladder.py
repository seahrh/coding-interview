"""
127. Word Ladder https://leetcode.com/problems/word-ladder/description/

A transformation sequence from word beginWord to word endWord using a dictionary wordList
is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList,
return the number of words in the shortest transformation sequence from beginWord to endWord,
or 0 if no such sequence exists.
Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.

SOLUTION
Shortest transformation seq is actually BFS shortest path.
Time O(NL): N is the size of word list and L is the length of longest word.
Space O(N+L): BFS queue, visited set, string slice
References
- https://leetcode.com/problems/word-ladder/solutions/1764371/a-very-highly-detailed-explanation/
"""

from collections import deque
from typing import Deque, List, Set


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words: Set[str] = set(wordList)
        if endWord not in words:
            return 0
        q: Deque[str] = deque([beginWord])
        vis = set()
        res = 1
        while len(q) != 0:
            qn = len(q)
            for _ in range(qn):  # process level by level
                a = q.popleft()
                vis.add(a)
                if a == endWord:
                    return res
                for i in range(len(a)):
                    for j in range(26):
                        b = a[:i] + chr(ord("a") + j) + a[i + 1 :]
                        if b in words and b not in vis:
                            q.append(b)
            res += 1
        return 0
