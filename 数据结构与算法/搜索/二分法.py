def bis(arr, target):    # arr 一定升序
    i, j = 0, len(arr)-1
    while i < j:
        mid = i+j >> 1
        if arr[i] < target:    # 等号在left决定了是 bisect_left
            i = mid + 1
        else:
            j = mid
    return {'索引':i, '值': arr[i]}

if __name__ == '__main__':
    arr = [1,1,1,2,2,4,5,5]
    res = bis(arr, 2)
    print(res)