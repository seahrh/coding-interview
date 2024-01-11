"""
224. Basic Calculator https://leetcode.com/problems/basic-calculator/description/

Given a string s representing a valid expression, implement a basic calculator to evaluate it,
and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions,
such as eval().
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
2 stacks: each recursion has its own stack to store intermediate values. Let's call this, intermediate stack.
Output of recursion is the sum of intermediate stack.
References
- https://leetcode.com/problems/basic-calculator/solutions/1456850/python-basic-calculator-i-ii-iii-easy-solution-detailed-explanation/
"""
from typing import List, Tuple


class Solution:
    def calculate(self, s: str) -> int:
        def rec(i: int) -> Tuple[int, int]:
            """Returns a pair (final output, last index of s where recursion stopped)."""

            def update(op: str, v: int) -> None:
                if op == "+":
                    stack.append(v)
                if op == "-":
                    stack.append(-v)
                # immediately compute higher precedence operation
                if op == "*":
                    stack.append(stack.pop() * v)
                if op == "/":
                    stack.append(stack.pop() // v)

            num: int = 0
            stack: List[int] = []
            sign: str = "+"
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] in "+-*/":
                    update(sign, num)  # apply the previous operation
                    num, sign = 0, s[i]
                elif s[i] == "(":  # recursion has a separate "intermediate" stack
                    num, i = rec(i + 1)
                elif s[i] == ")":
                    update(sign, num)  # apply last operation!
                    return sum(stack), i
                i += 1
            update(sign, num)  # apply last operation!
            return sum(stack), len(s)

        return rec(0)[0]
