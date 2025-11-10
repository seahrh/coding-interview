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
1. Problem Restatement
You need the shortest sequence of valid transformations from beginWord to endWord, where:
Each transformation changes exactly one letter.
Every intermediate word must exist in wordList.
Return the number of words (not edges) in the sequence.
So the goal is essentially to find the shortest path in an unweighted graph, where:
Each node = a valid word
Each edge = one-letter difference between words
This naturally maps to a Breadth-First Search (BFS) problem.

2. Algorithm: BFS
BFS explores all words reachable in 1 step, then 2 steps, etc.
The first time we encounter endWord, we’ve found the shortest path.
Steps:
Put beginWord into a queue.
For each word in the queue:
Generate all possible words differing by one letter.
If the new word is in the dictionary and not yet visited:
Mark it visited.
Add it to the queue for the next BFS level.
Count BFS levels — each level = +1 step in transformation.
Return the level when we reach endWord.

Time O(N * L^2)
For each of N words, we may check up to 26L possible transformations (L = word length). Efficient with set lookups.
Space O(N * L)
BFS queue, visited set, and temporary strings.

References
- https://leetcode.com/problems/word-ladder/solutions/1764371/a-very-highly-detailed-explanation/
"""

from collections import deque
from typing import Deque, List, Set


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set: Set[str] = set(wordList)
        if endWord not in word_set:
            return 0  # No valid transformation if endWord not in list
        queue: Deque = deque([(beginWord, 1)])  # (current_word, current_level)
        visited: Set[str] = {beginWord}
        while len(queue) != 0:
            word, level = queue.popleft()
            if word == endWord:
                return level  # Found shortest transformation path
            for i in range(len(word)):
                # Try replacing one letter at each position
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == word[i]:
                        continue  # Skip replacing with same character
                    # Creating this string by slicing costs O(L) time!
                    # You do that for each position (L) and each letter (26).
                    next_word = word[:i] + c + word[i + 1 :]
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))
        return 0  # No transformation sequence found
