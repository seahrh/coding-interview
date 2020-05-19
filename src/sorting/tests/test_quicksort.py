import unittest
from sorting.quicksort import *


class TestQuicksort(unittest.TestCase):

    def test_array_of_length_one_with_lomuto_partition_scheme(self):
        arr = [1]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        self.assertListEqual(arr, [1])

    def test_array_of_even_length_with_lomuto_partition_scheme(self):
        e = [x for x in range(1, 9)]
        arr = [7, 4, 1, 5, 8, 3, 6, 2]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        self.assertListEqual(arr, e)
        # already sorted array
        arr = [x for x in range(1, 9)]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        self.assertListEqual(arr, e)
        # with duplicates
        arr = [8, 4, 8, 2, 4, 6, 6, 2]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        self.assertListEqual(arr, [2, 2, 4, 4, 6, 6, 8, 8])

    def test_array_of_odd_length_with_lomuto_partition_scheme(self):
        e = [x for x in range(1, 10)]
        arr = [7, 4, 9, 1, 5, 8, 3, 6, 2]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        self.assertListEqual(arr, e)
        # already sorted array
        arr = [x for x in range(1, 10)]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        self.assertListEqual(arr, e)
        # with duplicates
        arr = [9, 3, 9, 7, 1, 3, 5, 5, 1]
        quicksort(arr=arr, partition_fn=lomuto_partition)
        self.assertListEqual(arr, [1, 1, 3, 3, 5, 5, 7, 9, 9])

    def test_array_of_length_one_with_hoare_partition_scheme(self):
        arr = [1]
        quicksort(arr=arr, partition_fn=hoare_partition)
        self.assertListEqual(arr, [1])

    def test_array_of_even_length_with_hoare_partition_scheme(self):
        e = [x for x in range(1, 9)]
        arr = [7, 4, 1, 5, 8, 3, 6, 2]
        quicksort(arr=arr, partition_fn=hoare_partition)
        self.assertListEqual(arr, e)
        # already sorted array
        arr = [x for x in range(1, 9)]
        quicksort(arr=arr, partition_fn=hoare_partition)
        self.assertListEqual(arr, e)
        # with duplicates
        arr = [8, 4, 8, 2, 4, 6, 6, 2]
        quicksort(arr=arr, partition_fn=hoare_partition)
        self.assertListEqual(arr, [2, 2, 4, 4, 6, 6, 8, 8])

    def test_array_of_odd_length_with_hoare_partition_scheme(self):
        e = [x for x in range(1, 10)]
        arr = [7, 4, 9, 1, 5, 8, 3, 6, 2]
        quicksort(arr=arr, partition_fn=hoare_partition)
        self.assertListEqual(arr, e)
        # already sorted array
        arr = [x for x in range(1, 10)]
        quicksort(arr=arr, partition_fn=hoare_partition)
        self.assertListEqual(arr, e)
        # with duplicates
        arr = [9, 3, 9, 7, 1, 3, 5, 5, 1]
        quicksort(arr=arr, partition_fn=hoare_partition)
        self.assertListEqual(arr, [1, 1, 3, 3, 5, 5, 7, 9, 9])


if __name__ == '__main__':
    unittest.main()
