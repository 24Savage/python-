#  数组中，按照原始顺序的一对前大后小的数叫一个逆序对
# 基于归并排序，从底层一步步计算
class Solution:
    def InversePairs(self, data):
        # write code here
        def count(i, j):
            if i >= j: return 0
            mid = i+j >> 1
            cnt = count(i,mid) + count(mid+1,j)
            l, r = i, mid+1
            tmp = []
            # 左半边和右边小已经排好序
            while l<=mid or r<=j:
                # 加入左边的数 cur  到 tmp 时，右半边已经进去的数均小于 cur
                if r>j or l<=mid and data[l] < data[r]:
                    tmp.append(data[l])
                    l += 1
                    cnt += r-mid-1
                else:
                    tmp.append(data[r])
                    r += 1                    
            for z in range(j-i+1):
                data[i+z] = tmp[z]
            return cnt
        return count(0,len(data)-1)

if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,0]
    cnt = Solution().InversePairs(data)
    print(cnt)