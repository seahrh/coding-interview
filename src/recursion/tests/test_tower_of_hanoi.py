from recursion.tower_of_hanoi import *


class TestTowerOfHanoi:
    def test_move_1_disk(self):
        fromm = [1]
        to = []
        buf = []
        move(len(fromm), fromm=fromm, to=to, buf=buf)
        assert to == [1]
        assert fromm == []
        assert buf == []

    def test_move_3_disks(self):
        fromm = [i for i in range(1, 4)]
        fromm.reverse()
        to = []
        buf = []
        move(len(fromm), fromm=fromm, to=to, buf=buf)
        assert to == [3, 2, 1]
        assert fromm == []
        assert buf == []

    def test_move_8_disks(self):
        fromm = [i for i in range(1, 9)]
        fromm.reverse()
        to = []
        buf = []
        move(len(fromm), fromm=fromm, to=to, buf=buf)
        assert to == [8, 7, 6, 5, 4, 3, 2, 1]
        assert fromm == []
        assert buf == []
