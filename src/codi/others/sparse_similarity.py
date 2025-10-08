"""
Sparse Similarity: The similarity of two documents (each with distinct words) is defined to be the
size of the intersection divided by the size of the union. For example, if the documents consist of
integers, the similarity of {1, 5, 3} and {1, 7, 2, 3} is e. 4, because the intersection has size
2 and the union has size 5.
We have a long list of documents (with distinct values and each with an associated 10) where the
similarity is believed to be "sparse:'That is, any two arbitrarily selected documents are very likely to
have similarity O. Design an algorithm that returns a list of pairs of document IDs and the associated
similarity.
Print only the pairs with similarity greater than zero. Empty documents should not be printed at all. For
simplicity, you may assume each document is represented as an array of distinct integers.
EXAMPLE
Input:
13: {14, 15, 100, 9, 3}
16: {32, 1, 9, 3, 5}
19: {15, 29, 2, 6, 8, 7}
24: {7, 10}
Output:
ID1, ID2, SIMILARITY
13, 19, 0.1
13, 16, 0.25
19, 24, 0.1428

(17.26, p631)
SOLUTION
Inverted index maps from word to list of containing documents.
Let D be number of documents and W be the maximum number of words in a document.
P is the number of pairs with similarity greater than zero.
Given that the problem stated sparseness, P << D
O(DW + PW) time
O(PW + D) space
"""

from collections import defaultdict, namedtuple

Document = namedtuple("Document", "id words")

Pair = namedtuple("Pair", "d1 d2 sim")


def jaccard_similarity(left, right):
    """This takes O(W) time and O(1) space."""
    intersection = len(left.intersection(right))
    # ok to do the following because there are no duplicate words in a document.
    union = len(left) + len(right) - intersection
    return float(intersection / union)


def _inverted_index(documents):
    res = defaultdict(set)  # O(PW) space
    for d in documents:  # O(DW) time
        for w in d.words:
            res[w].add(d.id)
    return res


def _signature(id1, id2):
    if id2 < id1:
        id1, id2 = id2, id1
    return "{},{}".format(id1, id2)


def positive_similarity(documents):
    index = _inverted_index(documents)  # O(DW) time
    dmap = {}
    for d in documents:  # O(D) time, O(D) space
        dmap[d.id] = d
    candidates = set()  # O(P) space
    for dids in index.values():  # O(PW) time
        candidates = candidates.union(dids)
    res = []
    seen = set()  # O(P) space
    for d1 in candidates:  # O(PW) time
        for d2 in candidates:
            if d1 == d2:
                continue
            signature = _signature(d1, d2)
            if signature in seen:
                continue
            seen.add(signature)
            sim = jaccard_similarity(dmap[d1].words, dmap[d2].words)
            if sim > 0:
                res.append(Pair(d1=d1, d2=d2, sim=sim))
    return res
