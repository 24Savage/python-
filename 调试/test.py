class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == "__main__":
    data = [1,2,3,4,5,6,7,0]
    cnt = Solution().InversePairs(data)
    print(cnt)