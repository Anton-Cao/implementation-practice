def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(a, b):
    ai = 0
    bi = 0
    res = []
    while ai < len(a) or bi < len(b):
        if bi == len(b) or ai < len(a) and a[ai] < b[bi]:
            res.append(a[ai])
            ai += 1
        else:
            res.append(b[bi])
            bi += 1
    return res
