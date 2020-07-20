def __merge(arr1, arr2):
    l1, l2 = len(arr1), len(arr2)
    res = list()
    i, j = 0, 0
    while i < l1 and j < l2:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    while i != l1:
        res.append(arr1[i])
        i += 1
    while j != l2:
        res.append(arr2[j])
        j += 1
    return res

def merge_sort(num):
    n = len(num)
    if n == 1 or n == 0:
        return num
    mid = n>>1
    return __merge(merge_sort(num[:mid]), merge_sort(num[mid:]))