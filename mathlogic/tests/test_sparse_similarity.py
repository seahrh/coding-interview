import unittest
from mathlogic.sparse_similarity import *


class TestSparseSimilarity(unittest.TestCase):
    def test_given_example_1(self):
        self.assertListEqual(positive_similarity(
            [Document(id=13, words={14, 15, 100, 9, 3}),
             Document(id=16, words={32, 1, 9, 3, 5}),
             Document(id=19, words={15, 29, 2, 6, 8, 7}),
             Document(id=24, words={7, 10, 11})]
        ), [Pair(d1=16, d2=13, sim=0.25),
            Pair(d1=19, d2=24, sim=0.125),
            Pair(d1=19, d2=13, sim=0.1)]
        )


if __name__ == '__main__':
    unittest.main()
