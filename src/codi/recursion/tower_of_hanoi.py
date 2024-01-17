from typing import List


def solve(
    n: int, from_stack: List[int], to_stack: List[int], buffer_stack: List[int]
) -> None:
    """
    Move a tower of height-1 to an intermediate pole, using the final pole.
    Move the remaining disk to the final pole.
    Move the tower of height-1 from the intermediate pole to the final pole using the original pole.
    Time O(2^N)
    Space O(N): recursive call stack
    """
    if n == 0:  # Base case: no disk to move
        return
    solve(n - 1, from_stack, buffer_stack, to_stack)
    to_stack.append(from_stack.pop())
    solve(n - 1, buffer_stack, to_stack, from_stack)
