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
Sliding window can expand and contract to encapsulate required chars.
Time O(M+N): each char in s is visited at most twice, once by left pointer and once by right pointer.
Space O(M+N)
References
- https://leetcode.com/problems/minimum-window-substring/solutions/4530977/python-easy-mind-map-diagram-two-pointer-sliding-window-dynamic-size-space-o-m-n/
"""

from collections import Counter
from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cn = Counter(t)
        win: Dict[str, int] = {}
        valid_keys_required = len(cn)
        valid_keys_formed = 0
        mn = len(s) + 1
        lo, hi, i, j = 0, 0, 0, 0
        # Expand window until a valid substring is found
        while hi < len(s):
            c = s[hi]
            win[c] = win.get(c, 0) + 1
            if c in cn and win[c] == cn[c]:
                valid_keys_formed += 1
            # Shrink window until there is no valid substring
            while lo <= hi and valid_keys_formed == valid_keys_required:
                c = s[lo]
                if (
                    hi - lo + 1 < mn
                ):  # Update the value of output before incrementing `lo`
                    mn = hi - lo + 1
                    i, j = lo, hi
                win[c] -= 1
                if c in cn and win[c] < cn[c]:
                    valid_keys_formed -= 1
                lo += 1
            hi += 1
        return "" if mn == len(s) + 1 else s[i : j + 1]
