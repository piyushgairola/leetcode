def minRefuelStops(target, startFuel, stations):
    # n = len(stations)
    # dp = [startFuel] + [0]*n

    # for i, (loc,capacity) in enumerate(stations):
    #     for j in range(i,-1,-1):
    #         if dp[j] >= loc:
    #             dp[j+1] = max(dp[j+1], dp[j]+capacity)


    # for i,d in enumerate(dp):
    #     if d >= target:
    #         return i

    # return -1

    n = len(stations)
    dp = [startFuel] + [0]*n
    
    for i in range(n):
        for j in range(i,-1,-1):
            if dp[j] >= stations[i][0]:
                dp[j+1] = max(dp[j+1], dp[j]+stations[i][1])
                
    for i,val in enumerate(dp):
        if val>=target:
            return i
        
    return -1



target = 100
startFuel = 50
stations = [[50,50]]

print(minRefuelStops(target, startFuel, stations))