from codi.sortingandsearching.quicksort import *


class TestMedianOfThree:
    # noinspection PyTypeChecker
    def test_median_of_three(self):
        a = [1]
        median_of_three(a)
        assert a[-1] == 1
        a = [2, 1]
        median_of_three(a)
        assert a[-1] == 2
        a = [2, 3, 1]
        median_of_three(a)
        assert a[-1] == 2
        a = [2, 4, 1, 3]
        median_of_three(a)
        assert a[-1] == 3
        a = [2, 4, 3, 1, 5]
        median_of_three(a)
        assert a[-1] == 3


# noinspection PyTypeChecker
class TestQuicksort:
    def test_array_of_length_one_with_lomuto_partition_scheme(self):
        arr = [1]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        assert arr == [1]

    def test_array_of_even_length_with_lomuto_partition_scheme(self):
        e = [x for x in range(1, 9)]
        arr = [7, 4, 1, 5, 8, 3, 6, 2]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        assert arr == e
        # already sorted array
        arr = [x for x in range(1, 9)]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        assert arr == e
        # with duplicates
        arr = [8, 4, 8, 2, 4, 6, 6, 2]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        assert arr == [2, 2, 4, 4, 6, 6, 8, 8]

    def test_array_of_odd_length_with_lomuto_partition_scheme(self):
        e = [x for x in range(1, 10)]
        arr = [7, 4, 9, 1, 5, 8, 3, 6, 2]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        assert arr == e
        # already sorted array
        arr = [x for x in range(1, 10)]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        assert arr == e
        # with duplicates
        arr = [9, 3, 9, 7, 1, 3, 5, 5, 1]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        assert arr == [1, 1, 3, 3, 5, 5, 7, 9, 9]

    def test_array_of_length_one_with_hoare_partition_scheme(self):
        arr = [1]
        quicksort(arr=arr, partition_fn=hoare_partition)
        assert arr == [1]

    def test_array_of_even_length_with_hoare_partition_scheme(self):
        e = [x for x in range(1, 9)]
        arr = [7, 4, 1, 5, 8, 3, 6, 2]
        quicksort(arr=arr, partition_fn=hoare_partition)
        assert arr == e
        # already sorted array
        arr = [x for x in range(1, 9)]
        quicksort(arr=arr, partition_fn=hoare_partition)
        assert arr == e
        # with duplicates
        arr = [8, 4, 8, 2, 4, 6, 6, 2]
        quicksort(arr=arr, partition_fn=hoare_partition)
        assert arr == [2, 2, 4, 4, 6, 6, 8, 8]

    def test_array_of_odd_length_with_hoare_partition_scheme(self):
        e = [x for x in range(1, 10)]
        arr = [7, 4, 9, 1, 5, 8, 3, 6, 2]
        quicksort(arr=arr, partition_fn=hoare_partition)
        assert arr == e
        # already sorted array
        arr = [x for x in range(1, 10)]
        quicksort(arr=arr, partition_fn=hoare_partition)
        assert arr == e
        # with duplicates
        arr = [9, 3, 9, 7, 1, 3, 5, 5, 1]
        quicksort(arr=arr, partition_fn=hoare_partition)
        assert arr == [1, 1, 3, 3, 5, 5, 7, 9, 9]
