"""
Calculator: Given an arithmetic equation consisting of positive integers, +, -, * and / (no parentheses),
compute the result.
EXAMPLE
Input: 2*3+5/6*3+15
Output: 23.5

(16.26, p535)
Solution with two stacks (1 stack for operators and 1 stack for operands)
takes O(n) time and O(n) space, where n is the length of the expression to evaluate.
"""
from enum import Enum


class Operator(Enum):
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    NOOP = ''

    @staticmethod
    def parse(string):
        if string == Operator.ADD.value:
            return Operator.ADD
        if string == Operator.SUBTRACT.value:
            return Operator.SUBTRACT
        if string == Operator.MULTIPLY.value:
            return Operator.MULTIPLY
        if string == Operator.DIVIDE.value:
            return Operator.DIVIDE
        return None

    def priority(self):
        if self == Operator.ADD:
            return 1
        if self == Operator.SUBTRACT:
            return 1
        if self == Operator.MULTIPLY:
            return 2
        if self == Operator.DIVIDE:
            return 2
        return 0

    def apply(self, left, right):
        if self == Operator.ADD:
            return left + right
        if self == Operator.SUBTRACT:
            return left - right
        if self == Operator.MULTIPLY:
            return left * right
        if self == Operator.DIVIDE:
            return left / right
        return right


def _collapse(future_top, operand_stack, operator_stack):
    """Collapse top until priority(futureTop) > priority(top).
    Collapsing means to pop the top 2 numbers and
    apply the operator popped from the top of the operator stack,
    and then push that onto the numbers stack."""
    while len(operator_stack) >= 1 and len(operand_stack) >= 2:
        if future_top.priority() > operator_stack[-1].priority():
            break
        right = operand_stack.pop()
        left = operand_stack.pop()
        res = operator_stack.pop().apply(left, right)
        operand_stack.append(res)


def calculate(string):
    if len(string.strip()) < 6:
        raise ValueError('Expression must have at least one operator and two operands')
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
