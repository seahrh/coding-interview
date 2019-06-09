"""
Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
ascending order, write a method to find an element.
(10.9, p421)
"""


def find(matrix, key):
    """
    This algorithm works by elimination. Start from the top right hand corner.
    Every move to the left (--col) eliminates all the elements below the current cell in that column.
    Likewise, every move down eliminates all the elements to the left of the cell in that row.

    This takes O(m+n) time and O(1) space,
    where m and n are number of rows and columns respectively.

    :param matrix: 2d sorted matrix
    :param key:
    :return: index of the element if found, otherwise -1
    """
    if len(matrix) == 0:
        raise ValueError('matrix must not be empty')
    rows = len(matrix)
    cols = len(matrix[0])
    i = 0
    j = cols - 1
    while i < rows and j >= 0:
        if matrix[i][j] == key:
            return i, j
        if key < matrix[i][j]:
            j -= 1
        else:
            i += 1
    return -1
