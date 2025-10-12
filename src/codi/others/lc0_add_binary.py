"""
67. Add Binary https://leetcode.com/problems/add-binary/description/
Given two binary strings a and b, return their sum as a binary string.
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

SOLUTION
We add bits from right to left, just like manual addition, keeping track of a carry.
At each step:
Add the bits from both strings (if present) plus the carry.
Compute the new bit: sum % 2
Compute the new carry: sum // 2
Continue until all bits and the carry are processed.

Time: O(N) — iterate once through both strings
Space: O(N) — for result storage
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            res.append(str(total % 2))
            carry = total // 2
        return "".join(reversed(res))
