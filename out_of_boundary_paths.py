def findPaths(m, n, maxMoves, startRow, startColumn):
    dp = [[[-1]*(maxMoves+1) for _ in range(n+1)]for _ in range(m+1)]

    def solve(i,j,moves):
        if moves<0:
            return 0
        
        if i<0 or i>=m or j<0 or j>=n:
            return 1

        if dp[i][j][moves] != -1:
            return dp[i][j][moves]

        a = solve(i+1,j,moves-1) 
        b = solve(i-1,j,moves-1) 
        c = solve(i,j+1,moves-1)
        d = solve(i,j-1,moves-1)

        dp[i][j][moves] = a+b+c+d 
        return dp[i][j][moves]

    solve(startRow,startColumn,maxMoves)



