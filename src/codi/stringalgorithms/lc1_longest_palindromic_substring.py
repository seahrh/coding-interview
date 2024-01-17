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
To enumerate all palindromic substrings of a given string,
we first expand a given string at each possible starting position of a palindrome
and also at each possible ending position of a palindrome and
keep track of the length of the longest palindrome we found so far.
We observe that a palindrome mirrors around its center.
Therefore, a palindrome can be expanded from its center, and there are only 2n - 1 such centers.
You might be asking why there are 2n - 1 but not n centers?
The reason is the center of a palindrome can be in between two letters.
Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.'
Time O(N^2)
Space O(1)
References
- https://leetcode.com/problems/longest-palindromic-substring/solutions/4212564/beats-96-49-5-different-approaches-brute-force-eac-dp-ma-recursion/
"""


class Solution:
    def expand_from_center(self, s: str, i: int, j: int) -> str:
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        # from index i+1 up to but not including j
        # if i+1>=j then slice is empty string
        return s[i + 1 : j]

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        max_str = s[0]
        for i in range(len(s) - 1):
            odd = self.expand_from_center(s, i, i)
            even = self.expand_from_center(s, i, i + 1)
            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
        return max_str
