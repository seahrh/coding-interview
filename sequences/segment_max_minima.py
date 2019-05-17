import sys

# Form segments of length x from the array.
# Get the minimum value from each segment and return the highest value.
# Complete the 'segment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x is the length of the segment
#  2. INTEGER_ARRAY arr
#
# Hacker Rank coding interview question (May 2019)


def segment(x, arr):
    # Slide the segment window to the right, one element at a time.
    # This takes O(n) time and O(1) space
    if len(arr) == 0:
        raise ValueError('arr must not be empty')
    if x == 0:
        raise ValueError('x must be a positive number')
    if x > len(arr):
        raise ValueError('x must not be greater than the array length')
    _max = -sys.maxsize
    for i, v in enumerate(arr):
        if i + x - 1 < len(arr):  # segment fits in the array
            _min = sys.maxsize
            for j in range(x):
                if arr[i + j] < _min:
                    _min = arr[i + j]
            if _min > _max:
                _max = _min
    return _max
