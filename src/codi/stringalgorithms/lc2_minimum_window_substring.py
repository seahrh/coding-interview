"""
76. Minimum Window Substring https://leetcode.com/problems/minimum-window-substring/description/

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s
such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
Follow up: Could you find an algorithm that runs in O(m + n) time?

SOLUTION
Sliding Window with Two Pointers
Why Sliding Window?
A "window" is a range in s like s[left:right+1].
We expand the right bound to include more characters,
and contract the left bound to remove unnecessary characters;
always making sure that the window covers all of t.

Step-by-step:
Count Characters Needed
Use Counter(t) to count how many of each character we need from t.
Window Setup
We use a dictionary (window_count) to track how many of each relevant character appear within our current window.
Expand the Window
Move the right pointer (right) through s, one character at a time:
Add the character to window_count.
If the character completes one of the required character counts, increment formed.
Shrink the Window
When every character in t is represented (formed == required):
Try to contract the left side of the window to make it as small as possible without losing any required characters.
Keep track of the minimum-length window found so far.
Return Result
After traversing s, return the smallest valid window found.

Complexity
Time: O(|s| + |t|), since each pointer only moves forward and each character is processed at most twice.
Space: O(|s| + |t|), for the various counters.

References
- https://leetcode.com/problems/minimum-window-substring/solutions/4530977/python-easy-mind-map-diagram-two-pointer-sliding-window-dynamic-size-space-o-m-n/
"""

from collections import Counter
from typing import Dict, Tuple


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        # Count the required characters in t
        target_count = Counter(t)
        window_count: Dict[str, int] = {}
        required = len(target_count)
        formed = 0
        left = 0  # Left pointer of window
        min_len = float("inf")
        min_window: Tuple[int, int] = (0, 0)
        # Right pointer expands the window
        for right, char in enumerate(s):
            window_count[char] = window_count.get(char, 0) + 1
            # If the current char added makes the window satisfy more of t's requirement
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            # Shrink window from the left if all requirements are met
            while formed == required:
                # Capture the left pointer before window is shrunk!
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = (left, right)
                # Remove the leftmost char from the window
                left_char = s[left]
                window_count[left_char] -= 1
                if (
                    left_char in target_count
                    and window_count[left_char] < target_count[left_char]
                ):
                    formed -= 1
                left += 1
        l, r = min_window
        return "" if min_len == float("inf") else s[l : r + 1]
