from itertools import accumulate

def stoneGameVII(stones):
    n = len(stones)
    dp = [[0]*n for _ in range(n)]

    stones_sum = [0] + list(accumulate(stones))

    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            dp[i][j] = max(stones_sum[j+1] - stones_sum[i+1] - dp[i+1][j], stones_sum[j] - stones_sum[i] - dp[i][j-1])

    return dp[0][n-1]



stones = [5,3,1,4,2]
print(stoneGameVII(stones))