"""
3. Longest Substring Without Repeating Characters https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

SOLUTION
Time O(N): each char in s is added or removed from set at most once.
Space O(1): constant size of ASCII charset
"""
from typing import Set


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        see: Set[str] = set()
        i = 0
        j = 0
        res = 0
        while j < len(s):
            if s[j] in see:
                while len(see) != 0 and i < j:
                    see.remove(s[i])
                    i += 1
                    if s[i - 1] == s[j]:
                        break
            see.add(s[j])
            res = max(res, j - i + 1)
            j += 1
        return res
