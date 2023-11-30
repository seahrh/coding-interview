"""
Kth Multiple: Design an algorithm to find the kth number such that the only prime factors are 3, 5,
and 7. Note that 3,5, and 7 do not have to be factors, but it should not have any other prime factors.
For example, the first several multiples would be (in order) 1,3, 5, 7, 9, 15,21.

(17.9, p561)
Solution: insert multiples into respective 'factor' queues.

1. Initialize array and queues Q3, QS, and Q7
2. Insert 1 into array.
3. Insert 1 * 3,1 *5 and 1 *7 into Q3, Q5, and Q7 respectively.
4. Let x be the minimum element in Q3, Q5, and Q7. Append x to magic.
5. If x was found in:
    Q3 -> append x*3, x*5 and x*7 to Q3, Q5, and Q7. Remove x from Q3.
    Q5 -> append x*5 and x*7 to Q5 and Q7. Remove x from Q5.
    Q7 -> only append x*7 to Q7. Remove x from Q7.
6. Repeat steps 4 - 6 until we've found k elements.

O(k) time and O(k) space.
"""
import sys
from collections import deque


def kth_multiple(k):
    if k < 1:
        raise ValueError("k must be a positive integer")
    res = 1
    q3 = deque()
    q5 = deque()
    q7 = deque()
    q3.append(1)
    for _ in range(k):
        v3 = q3[0] if len(q3) > 0 else sys.maxsize
        v5 = q5[0] if len(q5) > 0 else sys.maxsize
        v7 = q7[0] if len(q7) > 0 else sys.maxsize
        res = min(v3, v5, v7)
        if res == v3:
            q3.popleft()
            q3.append(res * 3)
            q5.append(res * 5)
        elif res == v5:
            q5.popleft()
            q5.append(res * 5)
        else:
            q7.popleft()
        q7.append(res * 7)  # always enqueue q7
    return res
