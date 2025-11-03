"""
5. Longest Palindromic Substring https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.

SOLUTION
The core trick: Any palindrome is mirrored around its center.
There are 2n - 1 possible centers in a string of length n:
n for single-character centers (odd-length palindromes)
n - 1 for between-character centers (even-length palindromes)
Expand around each center, keep track of the longest found.

How It Works
Iterate through all possible centers:
For each index, check for both odd and even-length palindromes.
Expand from center:
Grow the window left/right as long as the substring is symmetric.
Keep track of the longest palindrome found.
At the end, return the longest one.
Complexity
Time: O(N²) — Each center is expanded at most N times.
Space: O(1), excluding input/output.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return palindrome found; slice ends at right (exclusive)
            return s[left + 1 : right]

        if not s:
            return ""
        longest = ""
        for i in range(len(s)):
            # Expanding from (i, i) covers palindromes with a single center.
            # Odd length palindrome (center at s[i])
            p1 = expand_from_center(i, i)
            # Expanding from (i, i+1) covers palindromes with a center between two characters.
            # Even length palindrome (center between s[i] and s[i+1])
            p2 = expand_from_center(i, i + 1)
            # Update answer if longer palindrome found
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2
        return longest
