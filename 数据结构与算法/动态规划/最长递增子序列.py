# 给定数组arr，设长度为n，输出arr的最长递增子序列。（如果有多个答案，请输出其中字典序最小的)
# 引申问题：求最长递增子序列的个数

from bisect import bisect_left

def LIS(arr):
    n = len(arr)
    if not n: return []
    dp = [1]*n  # dp[i] 表示以 arr[i] 结尾的子序列的最大长度
    end = [arr[0]] # end[i] 长度为 i+1 的字典序最小的长子序列的尾值，单调自增
    for i in range(n):
        index = bisect_left(end, arr[i])
        if index == len(end):
            end.append(arr[i])
        else:
            end[index] = arr[i]
        dp[i] = index + 1
    length = len(end)
    ans = [0] * length
    for i in range(len(dp)-1, -1, -1):
        if dp[i] == length:
            ans[length-1] = arr[i]
            length -= 1
    return ans

if __name__ == '__main__':
    test = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    # dp = [1, 1, 2, 2, 3, 3, 4, 5, 4] 
    res = LIS(test)
    print(res)