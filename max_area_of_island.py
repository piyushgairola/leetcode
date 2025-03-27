def solution(grid):
    rows = len(grid)
    cols = len(grid[0])

    max_area = 0

    def dfs(x,y,grid):
        if x<0 or y<0 or x>rows or y>cols or grid[x][y] == 0: ## base case
            return 0

        grid[x][y] = 0  ## marking it visited

        l_area = dfs(x-1,y,grid) 
        r_area = dfs(x+1,y,grid)
        u_area = dfs(x,y+1,grid)
        b_area = dfs(x,y-1,grid)

        return l_area + r_area + u_area + b_area + 1 ## 1 is being added for current element


    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                max_area = max(dfs(i,j,grid), max_area)


    return max_area
                