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
Optimised Sliding Window
Use a dictionary to remember the last index of each character.
When you see a duplicate, jump the left boundary i forward.
Why is it better? Directly jumps i over duplicates, saving time.

Time O(N)
Space O(1): constant size of ASCII charset
"""

from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index: Dict[str, int] = {}  # Stores the last index of each character
        max_len = 0
        i = 0
        for j, c in enumerate(s):
            if c in char_index and char_index[c] >= i:
                i = char_index[c] + 1  # Move start to one past the LAST occurrence
            max_len = max(max_len, j - i + 1)
            char_index[c] = j  # Update last seen index
        return max_len
