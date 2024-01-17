"""
17. Letter Combinations of a Phone Number https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:
Input: digits = ""
Output: []
Example 3:
Input: digits = "2"
Output: ["a","b","c"]
Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

SOLUTION
Base case: partial solution grown to full length.
Time O(3^N)
Space O(N)
"""
from typing import List


class Solution:
    def rec(self, digits: str, i: int, p: str, full: List[str]) -> None:
        if len(p) == len(digits):
            full.append(p)
            return
        if digits[i] == "2":
            self.rec(digits=digits, i=i + 1, p=str(p) + "a", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "b", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "c", full=full)
        elif digits[i] == "3":
            self.rec(digits=digits, i=i + 1, p=str(p) + "d", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "e", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "f", full=full)
        elif digits[i] == "4":
            self.rec(digits=digits, i=i + 1, p=str(p) + "g", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "h", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "i", full=full)
        elif digits[i] == "5":
            self.rec(digits=digits, i=i + 1, p=str(p) + "j", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "k", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "l", full=full)
        elif digits[i] == "6":
            self.rec(digits=digits, i=i + 1, p=str(p) + "m", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "n", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "o", full=full)
        elif digits[i] == "7":
            self.rec(digits=digits, i=i + 1, p=str(p) + "p", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "q", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "r", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "s", full=full)
        elif digits[i] == "8":
            self.rec(digits=digits, i=i + 1, p=str(p) + "t", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "u", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "v", full=full)
        elif digits[i] == "9":
            self.rec(digits=digits, i=i + 1, p=str(p) + "w", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "x", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "y", full=full)
            self.rec(digits=digits, i=i + 1, p=str(p) + "z", full=full)

    def letterCombinations(self, digits: str) -> List[str]:
        full: List[str] = []
        if len(digits) != 0:
            self.rec(digits=digits, i=0, p="", full=full)
        return full
