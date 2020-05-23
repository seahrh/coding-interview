"""
Finish A* search function that can find path from starting point to the end
The robot starts from start position (0,0) and finds a path to end position (4, 5)
In the maze, 0 is open path while 1 means wall (a robot cannot pass through wall)
(heuristic is provided)

Example input:
[
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
]

A* search
===========
One important aspect of A* is f = g + h.
The f, g, and h variables are in our Node class and get calculated every time we create a new node.
F is the total cost of the node.
G is the distance between the current node and the start node.
H is the heuristic — estimated distance from the current node to the end node.

"""
from heapq import heappush, heappop
from typing import NamedTuple, Optional, List, Set, Iterable, Tuple, Callable


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
    curr: Optional[Node] = tail
    while curr is not None:
        res.append(curr.position)
        curr = curr.parent
    return res[::-1]


def pythagorean_heuristic(start: Node, goal: Node) -> int:
    return ((start.position.row - goal.position.row) ** 2) + (
        (start.position.col - goal.position.col) ** 2
    )


def search(
    maze: List[List[int]],
    start: Position,
    goal: Position,
    moves: Iterable[Position],
    walkable: int = 0,
    heuristic: Callable = pythagorean_heuristic,
) -> List[Position]:
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    start_node = Node(start)
    goal_node = Node(goal)
    # first element is the f-score; 2nd element is the Node pointer to break ties.
    open_list: List[Tuple[int, int, Node]] = []
    closed_set: Set[Position] = set()
    heappush(open_list, (start_node.f, id(start_node), start_node))
    while len(open_list) > 0:
        # get the node with the lowest f-score in the open list
        _, _, current_node = heappop(open_list)
        closed_set.add(current_node.position)

        # Found the goal
        if current_node.position == goal_node.position:
            return _path(current_node)

        children = current_node.neighbours(maze=maze, moves=moves, walkable=walkable)
        for child in children:
            if child.position in closed_set:
                continue
            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = heuristic(current_node, goal_node)
            child.f = child.g + child.h
            heappush(open_list, (child.f, id(child), child))

    return []  # path not found
