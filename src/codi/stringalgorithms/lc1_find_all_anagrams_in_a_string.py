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
Anagrams have the same letter counts.
Slide a window of length len(p) along s and compare letter counts.
How It Works
Frequency Arrays:
freq_p: Counts each letter in p
window: Counts letters in current window in s
Initialization: Set up both arrays for the first window (the first len(p) letters of s)
Sliding Window:
For every next character in s, update the window counts:
Remove the leftmost letter (exiting window)
Add the new rightmost letter (entering window)
Compare the arrays: If equal, the window is an anagram, so add the start index.

Time: O(N), with N = len(s)
Each window move: O(1) (since fixed 26 letters)
Array comparison: O(26)
Space: O(1)
Always 26 elements, regardless of input size.
"""

from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []
        # Frequency arrays for 'a' to 'z'
        freq_p: List[int] = [0] * 26
        window: List[int] = [0] * 26
        base = ord("a")
        # Initialize frequency arrays with first window
        for i in range(len_p):
            freq_p[ord(p[i]) - base] += 1
            window[ord(s[i]) - base] += 1
        res: List[int] = []
        if freq_p == window:
            res.append(0)
        # Slide the window across s
        for i in range(len_p, len_s):
            left_idx = ord(s[i - len_p]) - base
            right_idx = ord(s[i]) - base
            window[left_idx] -= 1  # Remove char leaving the window
            window[right_idx] += 1  # Add char entering the window
            if freq_p == window:
                res.append(i - len_p + 1)
        return res
