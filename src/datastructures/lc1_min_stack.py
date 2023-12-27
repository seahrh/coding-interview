"""
155. Min Stack https://leetcode.com/problems/min-stack/description/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]
Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
Constraints:
-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

SOLUTION
Use stack to keep track of min element.
References
- https://leetcode.com/problems/min-stack/solutions/4387183/neet-code-runtime-beats-98-99-memory-beats-92-96-of-users/
"""
from typing import List


class MinStack:
    def __init__(self):
        self.st1: List[int] = []
        self.st2: List[int] = []

    def push(self, val: int) -> None:
        self.st1.append(val)
        other = val
        if len(self.st2) != 0:
            other = self.st2[-1]
        self.st2.append(min(val, other))

    def pop(self) -> None:
        self.st1.pop()
        self.st2.pop()

    def top(self) -> int:
        return self.st1[-1]

    def getMin(self) -> int:
        return self.st2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
