"""
Finish A* search function that can find path from starting point to the end
The robot starts from start position (0,0) and finds a path to end position (4, 5)
In the maze, 0 is open path while 1 means wall (a robot cannot pass through wall)
(heuristic is provided)

example result:
[[0, -1, -1, -1, -1, -1],
[1, -1, -1, -1, -1, -1],
[2, -1, -1, -1, -1, -1],
[3, -1,  8, 10, 12, 14],
[4,  5,  6,  7, -1, 15]]
"""
from heapq import heappush, heappop
from typing import NamedTuple, Optional, List, Set, Iterable, Tuple


class Position(NamedTuple):
    row: int
    col: int

    def in_bounds(self, rows: int, cols: int) -> bool:
        if self.row < 0:
            return False
        if self.col < 0:
            return False
        if self.row >= rows:
            return False
        if self.col >= cols:
            return False
        return True


class Node:
    """A node class for A* Pathfinding"""

    def __init__(self, position: Position, parent: Optional["Node"] = None):
        self.parent: Optional["Node"] = parent
        self.position: Position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def neighbours(
        self, maze: List[List[int]], moves: Iterable[Position], walkable: int
    ) -> List["Node"]:
        # Generate children
        res = []
        for m in moves:
            pos = Position(
                row=self.position.row + m.row, col=self.position.col + m.col,
            )
            if not pos.in_bounds(rows=len(maze), cols=len(maze[0])):
                continue
            # make sure terrain walkable
            if maze[pos.row][pos.col] != walkable:
                continue
            node = Node(pos, parent=self)
            res.append(node)
        return res


def _path(tail: Node) -> List[Position]:
    res = []
    curr = tail
    while curr is not None:
        res.append(curr.position)
        curr = curr.parent
    return res[::-1]


def search(
    maze: List[List[int]],
    start: Position,
    goal: Position,
    moves: Iterable[Position],
    walkable: int = 0,
) -> List[Position]:
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    start_node = Node(start)
    goal_node = Node(goal)
    open_list: List[Tuple[int, int, Node]] = []
    closed_set: Set[Position] = set()
    heappush(open_list, (start_node.f, id(start_node), start_node))
    while len(open_list) > 0:
        _, _, current_node = heappop(open_list)
        closed_set.add(current_node.position)

        # Found the goal
        if current_node.position == goal_node.position:
            return _path(current_node)

        children = current_node.neighbours(maze=maze, moves=moves, walkable=walkable)
        # TODO continue here
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - goal_node.position[0]) ** 2) + (
                (child.position[1] - goal_node.position[1]) ** 2
            )
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
