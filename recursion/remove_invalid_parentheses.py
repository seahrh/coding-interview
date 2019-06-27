"""
Remove Invalid Parentheses
Remove the minimum number of invalid parentheses in order to make the input string valid.
Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]

From https://leetcode.com/articles/remove-invalid-parentheses/
SOLUTION
"""
import sys


def _remove(string, index, left_count, right_count, expr, rem_count, valid_expressions, min_removed):
    """
        string: The original string we are recursing on.
        index: current index in the original string.
        left: number of left parentheses till now.
        right: number of right parentheses till now.
        ans: the resulting expression in this particular recursion.
        ignored: number of parentheses ignored in this particular recursion.
    """
    # Base case: reached the end of string.
    if index == len(string):
        # If the current expression is valid. The only scenario where it can be
        # invalid here is if left > right. The other way around we handled early on in the recursion.
        if left_count == right_count:
            if rem_count <= min_removed:
                # This is the resulting expression.
                # Strings are immutable in Python so we move around a list in the recursion
                # and eventually join to get the final string.
                possible_ans = ''.join(expr)

                # If the current count of brackets removed < current minimum, ignore
                # previous answers and update the current minimum count.
                if rem_count < min_removed:
                    valid_expressions = set()
                    min_removed = rem_count
                valid_expressions.add(possible_ans)
        return
    current_char = string[index]
    # If the current character is not a parenthesis, just recurse one step ahead.
    if current_char != '(' and current_char != ')':
        expr.append(current_char)
        _remove(string, index + 1, left_count, right_count, expr, rem_count,
                valid_expressions=valid_expressions, min_removed=min_removed)
        expr.pop()
        return
    # Else, one recursion is with ignoring the current character.
    # So, we increment the ignored counter and leave the left and right untouched.
    _remove(string, index + 1, left_count, right_count, expr, rem_count + 1,
            valid_expressions=valid_expressions, min_removed=min_removed)
    expr.append(current_char)

    # If the current parenthesis is an opening bracket, we consider it
    # and increment left and  move forward
    if string[index] == '(':
        _remove(string, index + 1, left_count + 1, right_count, expr, rem_count,
                valid_expressions=valid_expressions, min_removed=min_removed)
    elif right_count < left_count:
        # If the current parenthesis is a closing bracket, we consider it only if we
        # have more number of opening brackets and increment right and move forward.
        _remove(string, index + 1, left_count, right_count + 1, expr, rem_count,
                valid_expressions=valid_expressions, min_removed=min_removed)
    expr.pop()


def remove(string):
    valid_expressions = set()
    min_removed = sys.maxsize
    _remove(string, index=0, left_count=0, right_count=0, expr=[], rem_count=0,
            valid_expressions=valid_expressions, min_removed=min_removed)
    return list(valid_expressions)
