"""
Calculator: Given an arithmetic equation consisting of positive integers, +, -, * and / (no parentheses),
compute the result.
EXAMPLE
Input: 2*3+5/6*3+15
Output: 23.5

(16.26, p535)
"""
from enum import Enum


class Operator(Enum):
    ADD = 1
    SUBTRACT = 1
    MULTIPLY = 2
    DIVIDE = 2
    NOOP = 0

    @staticmethod
    def parse(string):
        if string == '+':
            return Operator.ADD
        if string == '-':
            return Operator.SUBTRACT
        if string == '*':
            return Operator.MULTIPLY
        if string == '/':
            return Operator.DIVIDE
        return None

    def apply(self, left, right):
        if self.name == Operator.ADD:
            return left + right
        if self.name == Operator.SUBTRACT:
            return left - right
        if self.name == Operator.MULTIPLY:
            return left * right
        if self.name == Operator.DIVIDE:
            return left / right
        return right


def _collapse(future_top, operand_stack, operator_stack):
    """Collapse top until priority(futureTop) > priority(top).
    Collapsing means to pop the top 2 numbers and
    apply the operator popped from the top of the operator stack,
    and then push that onto the numbers stack."""
    while len(operator_stack) >= 1 and len(operand_stack) >= 2:
        if future_top.value > operator_stack[-1].value:
            break
        right = operand_stack.pop()
        left = operand_stack.pop()
        res = operator_stack.pop().apply(left, right)
        operand_stack.append(res)


def calculate(string):
    operand_stack = []
    operator_stack = []
    for term in string.split():
        op = Operator.parse(term)
        if op is None:
            operand_stack.append(float(term))
            continue
        _collapse(op, operand_stack, operator_stack)
        operator_stack.append(op)
    _collapse(Operator.NOOP, operand_stack, operator_stack)
    return operand_stack.pop()
