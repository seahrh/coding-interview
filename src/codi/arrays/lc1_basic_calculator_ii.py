"""
227. Basic Calculator II https://leetcode.com/problems/basic-calculator-ii/description/

Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero.
You may assume that the given expression is always valid.
All intermediate results will be in the range of [-231, 231 - 1].
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
Example 1:
Input: s = "3+2*2"
Output: 7
Example 2:
Input: s = " 3/2 "
Output: 1
Example 3:
Input: s = " 3+5 / 2 "
Output: 5
Constraints:
1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.

SOLUTION
Problem asks to process arithmetic with +, -, *, / and spaces, but no parentheses.
Order matters with * and / but not as much with + and -.
To handle this in a single pass:
Track the most recent number and operator.
For * and /, update the last number immediately as they're higher precedence.
For + and -, store the number (with sign) for later summing.
🔧 Most common technique: Use a stack (or variable) to handle numbers,
process only when you see a new operator or reach the end.

Step-by-step
1. Prepare
Strip spaces right away, or skip them during parsing.
Use a stack/list to track numbers to be summed in the end.
Use a variable to remember the last operator (+ by default).
Parse the string character-by-character, building whole numbers as you go.
2. Processing each character
If digit: build the current number.
If operator or end of string:
  Based on last operator '+', '-', '*', '/':
  + : push current number to stack
  - : push negative current number to stack
  * : pop stack, multiply, push result back
  / : pop stack, divide truncated toward zero, push back
  Set operator as the current one.
  Reset current number.
3. At end: Sum all numbers in stack for result.

Why Does This Work?
Immediately calculates *, / so they have priority.
Delays +, - until final sum.
Division uses int() to truncate toward zero (not Python's default).
Handles spaces and multi-digit numbers.

Time O(N)
Space O(N): stack
"""

from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        stack: List[int] = []
        num = 0
        op = "+"  # Default to '+'
        s = s.strip() + "+"  # Add '+' to process last number
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                elif op == "/":
                    prev = stack.pop()
                    # Python division truncates toward -infinity,
                    # need to truncate toward zero:
                    stack.append(int(prev / num))
                op = c
                num = 0
            # ignore spaces
        return sum(stack)
