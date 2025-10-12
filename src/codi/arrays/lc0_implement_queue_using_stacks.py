"""
232. Implement Queue using Stacks https://leetcode.com/problems/implement-queue-using-stacks/description/

Implement a first in first out (FIFO) queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:
You must use only standard operations of a stack,
which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively.
You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]
Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity?
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

SOLUTION
How It Works (Amortized O(1)):
Each element undergoes at most:
1. One push into inp
2. One move from inp → out
3. One pop from out
That’s three O(1) actions total per element, no matter how many total operations you do.
So even if a single pop() triggers a big transfer (O(n)), it doesn’t happen often —
each element contributes only once to that cost.
So even if a pop() or peek() occasionally takes O(n), the average cost per operation across many calls is O(1).
References
- https://leetcode.com/problems/implement-queue-using-stacks/solutions/2513639/very-easy-100-fully-explained-java-c-python-python3/
"""


class MyQueue:
    def __init__(self):
        self.inp = []  # stack for incoming elements
        self.out = []  # stack for outgoing elements

    def push(self, x: int) -> None:
        self.inp.append(x)

    def pop(self) -> int:
        # Transfer only if out is empty
        if len(self.out) == 0:
            while len(self.inp) != 0:
                self.out.append(self.inp.pop())
        return self.out.pop()

    def peek(self) -> int:
        if len(self.out) == 0:
            while len(self.inp) != 0:
                self.out.append(self.inp.pop())
        return self.out[-1]

    def empty(self) -> bool:
        return len(self.inp) == 0 and len(self.out) == 0
