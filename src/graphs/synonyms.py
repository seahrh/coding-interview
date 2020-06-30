"""
Baby Names: Each year, the government releases a list of the 10,000 most common baby names
and their frequencies (the number of babies with that name). The only problem with this is that
some names have multiple spellings. For example, "John" and "Jon" are essentially the same name
but would be listed separately in the list. Given two lists, one of names/frequencies and the other
of pairs of equivalent names, write an algorithm to print a new list of the true frequency of each
name. Note that if John and Jon are synonyms, and Jon and Johnny are synonyms, then John and
Johnny are synonyms. (It is both transitive and symmetric.) In the final list, any name can be used
as the "real" name.
EXAMPLE
Input:
Names: John (15), Jon (12), Chris (13), Kris (4), Christopher (19)
Synonyms: (Jon, John), (John, Johnny), (Chris, Kris), (Chris, Christopher)
Output: John (27), Kris (36)

(17.7, p553)

SOLUTION
Equivalence classes as disconnected graph components.
Reading in the data is linear with respect to the size of the data,
so it takes 0 (B + P) time, where B is the number of baby names and
P is the number of pairs of synonyms.
This is because we only do a constant amount of work per piece of input data.
To compute the frequencies, each edge gets "touched" exactly once across all of the graph searches and
each node gets touched exactly once to check if it's been visited. The time of this part is 0 (B + P) .
Therefore, the total time of the algorithm is 0 (B + P).
We know we cannot do better than this since we must at least read in the B + P pieces of data.
O(B) space to hold the `visited` set. Worst case: no names are synonyms.
"""
from typing import NamedTuple
from graphs.graph import *


class Node(NamedTuple):
    name: str
    freq: int


class Synonym(NamedTuple):
    first: str
    second: str


def _graph(
    names: List[Tuple[str, int]], synonyms: List[Tuple[str, str]]
) -> Graph[Node]:
    g = Graph[Node]()
    nodes: Dict[str, Node] = {}
    for name, freq in names:
        nodes[name] = Node(name=name, freq=freq)
    g.add_nodes(*nodes.values())  # expand collection to varargs
    for name1, name2 in synonyms:
        if name1 in nodes and name2 in nodes:
            g.add(Edge(nodes[name1], nodes[name2]))
    return g


def merge(names: List[Tuple[str, int]], synonyms: List[Tuple[str, str]]) -> Set[Node]:
    res: Set[Node] = set()
    g = _graph(names, synonyms)
    visited = set()
    for n in g.nodes():
        if n in visited:
            continue
        _sum = 0
        component = g.component(n)
        for c in component.nodes():
            _sum += c.freq
            visited.add(c)
        res.add(Node(n.name, _sum))
    return res
