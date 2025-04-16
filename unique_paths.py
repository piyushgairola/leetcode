def solution(m,n):
    if m == 0 or n == 0: ## grid with zero rows or columns has no valid paths
        return 0
    if m == 1 or n == 1: ## grid with one row or one column has exactly one path (straight line).
        return 1
    
    ## the first row and first column of the grid always have exactly 1 unique path to reach any cell[straight line].
    ## In the first row, you can only move right to reach any cell. Therefore, there is exactly 1 unique path to each cell in the first row.
    ## in the first column, you can only move down to reach any cell. Thus, there is exactly 1 unique path to each cell in the first column.
    ## By initializing the entire dp array with 1, you automatically handle these base cases without needing additional logic.
    dp = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1,m):
        for j in range(1, n):
            ## number of ways to reach [i,j] = number of ways to reach from up [i-1, j] + number of ways to reach from left [i, j-1]
            dp[i][j] = dp[i-1][j] + dp[i][j-1] 
    
    return dp[-1][-1] ## return the number of ways to reach bottom right cell.
    

m = 3
n = 7
print(solution(m,n))