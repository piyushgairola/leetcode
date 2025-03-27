def solution(pressedKeys):
    n = len(pressedKeys)
    dp = [0]* (n+1) 

    dp[0] = 1 ## base case

    for i in range(1,n+1):
        dp[i] = dp[i-1] ## 
        if i-2 >= 0 and pressedKeys[i-1] == pressedKeys[i-2]:
            dp[i] += dp[i-2]

        if i-3 >= 0 and pressedKeys[i-1] == pressedKeys[i-3]:
            dp[i] += dp[i-3]

        if pressedKeys[i-1] in ("7","9"):
            if i-4 >= 0 and pressedKeys[i-4] == pressedKeys[i-1]:
                dp[i] += dp[i-4]

    return dp[-1]


pressedKeys = "22233"
print(solution(pressedKeys))

        