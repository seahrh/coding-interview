"""
Sum numeric strings a + b without adding them up directly.
Examples
“123” + "1" = “124”
"999" + "1" = "1000"

SOLUTION
Time O(N)
Space O(N): store the result, else O(1).
"""

from typing import List


def solve(a: str, b: str) -> str:
    res: str = ""
    digits: List[str] = [str(i) for i in range(10)]
    longer = a
    shorter = b
    if len(a) < len(b):
        longer, shorter = b, a
    carry_over = 0
    for i in range(len(longer)):
        li = len(longer) - 1 - i
        si = len(shorter) - 1 - i
        d = int(longer[li]) + carry_over
        if si >= 0:
            d += int(shorter[si])
        res = digits[d % 10] + res
        if d <= 9:
            carry_over = 0
        else:
            carry_over = 1
    if carry_over == 1:
        res = "1" + res
    return res
