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
"""
from graphs.graph import *


class Node:
    def __init__(self, name, freq, is_visited=False):
        self.name = name
        self.freq = freq
        self.is_visited = is_visited


def _graph(names, synonyms):
    g = Graph()
    nodes = {}
    for name, freq in names:
        nodes[name] = Node(name=name, freq=freq)
    g.add_nodes(nodes.values())
    for name1, name2 in synonyms:
        if name1 in nodes and name2 in nodes:
            g.add_edge(nodes[name1], nodes[name2])
    return g


def _component_sum(graph, node):
    res = node.freq
    node.is_visited = True
    for n in graph.adjacent(node):
        res += n.freq
        n.is_visited = True
    return res


def merge(names, synonyms):
    res = []
    g = _graph(names, synonyms)
    for n in g.nodes():
        if n.is_visited:
            continue
        res.append((n.name, _component_sum(g, n)))
    return res
