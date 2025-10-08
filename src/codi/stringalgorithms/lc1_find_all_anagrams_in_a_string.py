"""
438. Find All Anagrams in a String https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
Constraints:
1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.

SOLUTION
For 2 strings to be anagrams of each other, they should have the same elements with the same frequency.
Time O(N): sliding window
Space O(1): array representing 26 letters
References
- https://leetcode.com/problems/find-all-anagrams-in-a-string/solutions/1738073/short-and-simple-c-sliding-window-solution/
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        fre = [0] * 26
        win = [0] * 26
        bas = ord("a")
        # first window
        for i in range(len(p)):
            fre[ord(p[i]) - bas] += 1
            win[ord(s[i]) - bas] += 1
        res = []
        if fre == win:
            res.append(0)
        for i in range(len(p), len(s)):  # advancing the tail of window
            win[ord(s[i - len(p)]) - bas] -= 1  # remove 1 char from the left
            win[ord(s[i]) - bas] += 1  # add 1 char to the right
            if fre == win:
                res.append(i - len(p) + 1)
        return res
