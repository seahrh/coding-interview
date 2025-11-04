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
Mapping: A dictionary (digit_to_letters) matches each digit to its corresponding letters,
according to classic phone keypads.
Early exit: If digits is empty, return [] immediately.
Backtracking:
Start at index 0, and build up the solution (path) one character at a time.
At each step, for the current digit, try every possible letter.
When the partial solution (path) reaches the same length as digits,
we’ve formed a valid combination—add it to the results.

Time: O(3ⁿ)...O(4ⁿ), where n = len(digits) (since some digits map to 3, some to 4 letters).
Space: O(n) for the recursion stack and output.
"""

from typing import Dict, List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Map digits to letters, just like on a keypad
        digit_to_letters: Dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
        result: List[str] = []

        # Backtracking helper
        def backtrack(index: int, path: str):
            if index == len(digits):
                result.append(path)
                return
            for letter in digit_to_letters[digits[index]]:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result
