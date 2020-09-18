def findNstUgly(n):
    '''
    每个丑数都是由2、3、5中的某一个乘以一个丑数得到的
    对2、3、5可以用字典分别记录它乘过的最小的丑数
    第一个丑数是1
    '''
    base = {2:0,3:0,5:0}
    dp = [1]*n
    for i in range(1, n):
        dp[i] = min([k*dp[v] for k,v in base.items()])
        for k,v in base.items():
            if k*dp[v] == dp[i]:
                base[k] += 1
    print(dp[-1])
