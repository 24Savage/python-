# 给定数组arr，设长度为n，输出arr的最长递增子序列。（如果有多个答案，请输出其中字典序最小的)
# 引申问题：求最长递增子序列的个数

from bisect import bisect_left

def LIS(arr):
    if not arr: return
    dp = []  # dp[i] 表示以 arr[i] 结尾的子序列的最大长度
    end = [] # end[i] 长度为 i+1 的字典序最小的长子序列的尾值，单调自增
    for num in arr:
        index = bisect_left(end, num)   # 二分查找最适合当前 num 的位置
        if index == len(end):
            end.append(num)
        else:
            end[index] = num
        dp.append(index+1)
    l = len(end)
    ans = [0] * l
    for i in range(len(dp)-1, -1, -1):  # 由 end 的构造方式，可知 dp[i] 相同时 i 越大 arr[i] 越小
        if dp[i] == l:
            ans[l-1] = arr[i]
            l -= 1
    return ans

if __name__ == '__main__':
    # 思考怎么测试
    # 先明确输入参数的类型 （List[int]）
    # 考虑等价类法：
    # arr 不是 list 类型：None、非 None 也非 list 对象
    # arr 是 list：空列表、[None]、单调递增列表、单调递减列表、同时考虑 int 的边界值
    test = [2, 1, 5, 3, 6, 4, 8, 9, 7]
    # dp = [1, 1, 2, 2, 3, 3, 4, 5, 4] 
    res = LIS(test)
    print(res)