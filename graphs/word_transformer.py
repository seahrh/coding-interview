"""
Word Transformer: Given two words of equal length that are in a dictionary, write a method to
transform one word into another word by changing only one letter at a time. The new word you get
in each step must be in the dictionary.
EXAMPLE
Input: DAMP, LIKE
Output: DAMP -> LAMP -> LIMP -> LIME -> LIKE

(17.22, p613)
"""
from collections import defaultdict, namedtuple, deque


def _wildcards(word, symbol='_'):
    """Return list of wildcards associated with word."""
    res = []
    for i in range(len(word)):
        res.append(word[:i] + symbol + word[i + 1:])
    return res


def _wildcard_map(words):
    """Returns a hash table where the key is a wildcard
    and the value is a list of words that match the wildcard.
    """
    res = defaultdict(list)
    for word in words:
        for wildcard in _wildcards(word):
            res[wildcard].append(word)
    return res


def _neighbours(word, wildcard_map):
    """Returns all words that are at edit distance one-away.
    If an edge represents an edit distance of 1, then return all neighbours of the target word.
    """
    res = set()
    for wildcard in _wildcards(word):
        for neighbour in wildcard_map.get(wildcard, []):
            if neighbour != word:
                res.add(neighbour)
    return res


Node = namedtuple('Node', 'word prev')


def _path(node, from_head=True):
    res = deque()
    n = node
    while n is not None:
        if from_head:
            res.append(n.word)
        else:
            res.appendleft(n.word)  # reverse direction, so add predecessor!
        n = n.prev
    return res


class BreadthFirstSearch:
    def __init__(self, root):
        head = Node(word=root, prev=None)
        self.to_visit = deque([head])  # FIFO queue of nodes to visit
        self.visited = {root: head}  # map from word to node

    def is_finished(self):
        return len(self.to_visit) == 0


def _merge(bfs1, bfs2, connecting_word):
    tail = bfs1.visited.get(connecting_word)  # path1: src -> tail
    head = bfs2.visited.get(connecting_word)  # path2: head -> dest
    path1 = _path(tail, from_head=False)
    path2 = _path(head, from_head=True)
    path2.popleft()  # remove connection
    path1.extend(path2)
    return path1


def _search_level(wildcard_map, primary, secondary):
    """Search one level of the tree and return collision, if any.
    Count nodes in primary's level and only do that many nodes.
    Continue to enqueue nodes to visit.
    """
    for i in range(len(primary.to_visit)):
        curr = primary.to_visit.popleft()  # dequeue head
        word = curr.word
        if word in secondary.visited:
            return word
        for word in _neighbours(word, wildcard_map):
            if word not in primary.visited:
                _next = Node(word=word, prev=curr)
                primary.visited[word] = _next
                primary.to_visit.append(_next)
    return None


def transform(from_word, to_word, words):
    if len(from_word) != len(to_word):
        raise ValueError('Both words must have equal length')
    if to_word not in words or from_word not in words:
        return []
    wmap = _wildcard_map(words)
    src = BreadthFirstSearch(from_word)
    dest = BreadthFirstSearch(to_word)
    while not src.is_finished() and not dest.is_finished():
        # search out from source
        collision = _search_level(wmap, src, dest)
        if collision is not None:
            return _merge(src, dest, collision)
        # search out from destination
        collision = _search_level(wmap, dest, src)
        if collision is not None:
            return _merge(src, dest, collision)
    return []
