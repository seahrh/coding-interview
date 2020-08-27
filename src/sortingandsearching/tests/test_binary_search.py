from sortingandsearching.binary_search import *


class TestBinarySearch:
    def test_search_array_of_length_one(self):
        assert search(arr=[1], key=1) == 0
        assert search(arr=[1], key=0) == -1
        assert search(arr=[1], key=2) == -1

    def test_search_array_of_length_two(self):
        assert search(arr=[1, 2], key=1) == 0
        assert search(arr=[1, 2], key=2) == 1
        assert search(arr=[1, 2], key=0) == -1
        assert search(arr=[1, 2], key=3) == -1
        assert search(arr=[1, 3], key=2) == -1

    def test_search_array_of_length_three_or_greater(self):
        arr = [1, 2, 3]
        assert search(arr=arr, key=1) == 0
        assert search(arr=arr, key=2) == 1
        assert search(arr=arr, key=3) == 2
        assert search(arr=arr, key=0) == -1
        assert search(arr=arr, key=4) == -1
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        assert search(arr=arr, key=1) == 0
        assert search(arr=arr, key=2) == 1
        assert search(arr=arr, key=3) == 2
        assert search(arr=arr, key=4) == 3
        assert search(arr=arr, key=5) == 4
        assert search(arr=arr, key=6) == 5
        assert search(arr=arr, key=7) == 6
        assert search(arr=arr, key=8) == 7
        assert search(arr=arr, key=0) == -1
        assert search(arr=arr, key=99) == -1


class TestBinarySearchArrayWithEmptyStrings:
    def test_search_array_of_length_one(self):
        assert search_array_with_empty_strings(arr=["b"], key="b") == 0
        assert search_array_with_empty_strings(arr=["b"], key="a") == -1
        assert search_array_with_empty_strings(arr=["b"], key="c") == -1

    def test_search_array_of_length_two(self):
        assert search_array_with_empty_strings(arr=["b", "c"], key="b") == 0
        assert search_array_with_empty_strings(arr=["b", "c"], key="c") == 1
        assert search_array_with_empty_strings(arr=["b", ""], key="b") == 0
        assert search_array_with_empty_strings(arr=["", "c"], key="c") == 1
        assert search_array_with_empty_strings(arr=["b", "c"], key="a") == -1
        assert search_array_with_empty_strings(arr=["b", "c"], key="d") == -1
        assert search_array_with_empty_strings(arr=["b", "d"], key="c") == -1

    def test_search_array_of_length_three(self):
        assert search_array_with_empty_strings(arr=["b", "c", "d"], key="b") == 0
        assert search_array_with_empty_strings(arr=["b", "c", "d"], key="c") == 1
        assert search_array_with_empty_strings(arr=["b", "c", "d"], key="d") == 2
        assert search_array_with_empty_strings(arr=["b", "", "d"], key="b") == 0
        assert search_array_with_empty_strings(arr=["b", "c", ""], key="c") == 1
        assert search_array_with_empty_strings(arr=["", "c", "d"], key="d") == 2
        assert search_array_with_empty_strings(arr=["b", "c", "d"], key="a") == -1
        assert search_array_with_empty_strings(arr=["b", "c", "d"], key="e") == -1
        assert search_array_with_empty_strings(arr=["b", "d", "e"], key="c") == -1

    def test_when_array_has_only_empty_strings_then_not_found(self):
        assert search_array_with_empty_strings(arr=[""], key="a") == -1
        assert search_array_with_empty_strings(arr=["", ""], key="a") == -1


class TestBinarySearchNearest:
    def test_search_array_of_length_one(self):
        assert nearest(arr=[1], key=1) == 0
        assert nearest(arr=[1], key=0) == 0
        assert nearest(arr=[1], key=2) == 0

    def test_search_array_of_length_two(self):
        assert nearest(arr=[1, 2], key=1) == 0
        assert nearest(arr=[1, 2], key=2) == 1
        assert nearest(arr=[1, 2], key=0) == 0
        assert nearest(arr=[1, 2], key=3) == 1
        assert nearest(arr=[1, 4], key=2) == 0
        assert nearest(arr=[1, 4], key=3) == 1

    def test_search_array_of_length_three(self):
        arr = [1, 2, 3]
        assert nearest(arr=arr, key=1) == 0
        assert nearest(arr=arr, key=2) == 1
        assert nearest(arr=arr, key=3) == 2
        assert nearest(arr=arr, key=0) == 0
        assert nearest(arr=arr, key=4) == 2
        assert nearest(arr=[1, 2, 40], key=39) == 2
        assert nearest(arr=[1, 2, 40], key=3) == 1
