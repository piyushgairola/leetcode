def numDecodings(s):
    if len(s)==0 or s[0] == "0":
        return 0

    dp = [0]*(len(s)+1)
    dp[:2] = [1,1]

    for i in range(2,len(s)+1):
        if int(s[i-1:i]) > 0:
            dp[i] += dp[i-1]

        if 10<=int(s[i-2:i])<=26:
            dp[i] += dp[i-2]

    return dp[-1]



print(numDecodings("06"))