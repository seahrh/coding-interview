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
Dual Stack Method
Main Stack (stack): Holds all the values you push.
Min Stack (min_stack): For every push, it also keeps the minimum value so far on top.
This means, at any moment, min_stack[-1] gives you the smallest value in the stack in O(1) time.
Operations
push(val): Add value to both stacks.
For min_stack, push the smaller of the incoming value or its current top (so you always have the minimum so far).
pop(): Remove the top value from both stacks, keeping them perfectly mirrored.
top(): Return the top value of the main stack.
getMin(): Return the top of the min stack, always the current minimum.

Time Complexity
All operations are O(1):
push, pop, top, and getMin only use stack methods (append/pop/indexing), all of which are performed in constant time.
Space Complexity
O(n) in the worst case (where n is the number of pushed elements).
Both stack and min_stack grow together, but do not use extra space beyond 2n for n elements.
Why This Is Ingenious
You always track the minimum with zero overhead—no scanning needed.
Handles “multiple identical minimums” by mirroring min value through pops.
"""

from typing import List


class MinStack:
    def __init__(self):
        self.stack: List[int] = []  # Stores all elements
        self.min_stack: List[int] = []  # Stores the minimum value at each stack level

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the minimum value so far onto min_stack
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
