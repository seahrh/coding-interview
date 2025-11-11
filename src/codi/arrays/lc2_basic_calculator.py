"""
224. Basic Calculator https://leetcode.com/problems/basic-calculator/description/

Given a string s representing a valid expression, implement a basic calculator to evaluate it,
and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
Example 1:
Input: s = "1 + 1"
Output: 2
Example 2:
Input: s = " 2-1 + 2 "
Output: 3
Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
Constraints:
1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.

SOLUTION
🧩 Problem Recap
We must evaluate a valid arithmetic expression string with:
Integers
+ and - operators
Parentheses ( and )
Optional unary - (e.g. -(2 + 3))
No multiplication or division appear in this version (unlike Basic Calculator II).

⚙️ Core Idea — Recursion with a Stack
The main insight:
Each pair of parentheses ( ... ) can be treated as a subproblem.
Inside each recursion:
Keep track of the running number (num)
Maintain a stack for partial results
Each time we hit an operator, we apply the previous sign and push to the stack
When we see ( → recursively solve until matching )
When we see ) → return the sum of the current stack to the parent context

📦 Helper Function
helper(i) returns:
value: the evaluated integer value from s[i:]
next_index: the position where the recursive evaluation stopped (e.g. right after ))
This allows the outer recursion to resume scanning correctly after a closed parenthesis.

Time O(N): Each character in the string is visited once.
Space O(N): Stack and recursion depth proportional to number of parentheses.
"""

from typing import List, Tuple


class Solution:
    def calculate(self, s: str) -> int:
        """
        Evaluate a mathematical expression string containing +, -, (, ), and integers.
        Supports nested parentheses and unary minus.
        """

        def rec(i: int) -> Tuple[int, int]:
            """Recursively evaluate expression from index i and return (value, next_index)."""
            stack: List[int] = []
            num, sign = 0, "+"

            def apply(op: str, val: int) -> None:
                """Apply the previous operation to the current value and update the stack."""
                if op == "+":
                    stack.append(val)
                elif op == "-":
                    stack.append(-val)

            while i < len(s):
                char = s[i]
                if char.isdigit():
                    num = num * 10 + int(char)  # build multi-digit number
                elif char in "+-":
                    apply(sign, num)
                    num, sign = 0, char  # reset for next number
                elif char == "(":
                    num, i = rec(i + 1)  # recursively evaluate inside parentheses
                elif char == ")":
                    apply(sign, num)
                    return sum(stack), i  # return to previous recursive level
                i += 1
            apply(sign, num)
            return sum(stack), i  # reached end of string

        # remove spaces for simplicity
        s = s.replace(" ", "")
        return rec(0)[0]
