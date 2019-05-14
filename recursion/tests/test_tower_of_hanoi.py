import unittest
from recursion.tower_of_hanoi import *


class TestTowerOfHanoi(unittest.TestCase):
    def test_move_1_disk(self):
        fromm = [1]
        to = []
        buf = []
        move(len(fromm), fromm=fromm, to=to, buf=buf)
        self.assertListEqual(to, [1])
        self.assertListEqual(fromm, [])
        self.assertListEqual(buf, [])

    def test_move_3_disks(self):
        fromm = [i for i in range(1, 4)]
        fromm.reverse()
        to = []
        buf = []
        move(len(fromm), fromm=fromm, to=to, buf=buf)
        self.assertListEqual(to, [3, 2, 1])
        self.assertListEqual(fromm, [])
        self.assertListEqual(buf, [])

    def test_move_8_disks(self):
        fromm = [i for i in range(1, 9)]
        fromm.reverse()
        to = []
        buf = []
        move(len(fromm), fromm=fromm, to=to, buf=buf)
        self.assertListEqual(to, [8, 7, 6, 5, 4, 3, 2, 1])
        self.assertListEqual(fromm, [])
        self.assertListEqual(buf, [])


if __name__ == '__main__':
    unittest.main()
