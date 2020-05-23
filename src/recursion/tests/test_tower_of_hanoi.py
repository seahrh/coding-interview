from recursion.tower_of_hanoi import *


class TestTowerOfHanoiRecursive:
    def test_move_1_disk(self):
        fs = [1]
        ts = []
        bs = []
        solve(len(fs), from_stack=fs, to_stack=ts, buffer_stack=bs)
        assert ts == [1]
        assert fs == []
        assert bs == []

    def test_move_3_disks(self):
        fs = [i for i in range(1, 4)]
        fs.reverse()
        ts = []
        bs = []
        solve(len(fs), from_stack=fs, to_stack=ts, buffer_stack=bs)
        assert ts == [3, 2, 1]
        assert fs == []
        assert bs == []

    def test_move_8_disks(self):
        fs = [i for i in range(1, 9)]
        fs.reverse()
        ts = []
        bs = []
        solve(len(fs), from_stack=fs, to_stack=ts, buffer_stack=bs)
        assert ts == [8, 7, 6, 5, 4, 3, 2, 1]
        assert fs == []
        assert bs == []
