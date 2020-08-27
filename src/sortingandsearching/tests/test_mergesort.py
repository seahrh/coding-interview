from sortingandsearching.mergesort import *


class TestMergesort:
    def test_array_of_length_one(self):
        arr = [1]
        mergesort(arr)
        assert arr == [1]

    def test_array_of_even_length(self):
        e = [x for x in range(1, 9)]
        arr = [7, 4, 1, 5, 8, 3, 6, 2]
        mergesort(arr)
        assert arr == e
        # already sorted array
        arr = [x for x in range(1, 9)]
        mergesort(arr)
        assert arr == e
        # with duplicates
        arr = [8, 4, 8, 2, 4, 6, 6, 2]
        mergesort(arr)
        assert arr == [2, 2, 4, 4, 6, 6, 8, 8]

    def test_array_of_odd_length(self):
        e = [x for x in range(1, 10)]
        arr = [7, 4, 9, 1, 5, 8, 3, 6, 2]
        mergesort(arr)
        assert arr == e
        # already sorted array
        arr = [x for x in range(1, 10)]
        mergesort(arr)
        assert arr == e
        # with duplicates
        arr = [9, 3, 9, 7, 1, 3, 5, 5, 1]
        mergesort(arr)
        assert arr == [1, 1, 3, 3, 5, 5, 7, 9, 9]
