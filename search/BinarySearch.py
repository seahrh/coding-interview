def search(arr, key):
    if len(arr) == 0:
        raise ValueError('arr must not be empty')
    begin = 0
    end = len(arr) - 1
    while begin <= end:
        mid = int((end - begin) / 2 + begin)
        print('begin={}, end={}, mid={}'.format(begin, end, mid))
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            begin = mid + 1
            continue
        if key < arr[mid]:
            end = mid - 1
    return -1
