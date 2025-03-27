def minCostClimbingStairs(costs):
    n = len(costs)
    dp = [None]*n

    for i in range(n):
        if i<2:
            dp[i] = costs[i]

        else:
            dp[i] = costs[i] + min(dp[i-1], dp[i-2])

    return min(dp[n-1], dp[n-2])


costs = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(costs))