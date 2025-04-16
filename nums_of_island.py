def solution(grid):
    r = len(grid)
    c = len(grid[0])

    count = 0

    def dfs(x,y,grid):
        if x<0 or y<0 or x>=r or y >=c or grid[x][y]=="0":
            return 
        
        grid[x][y] = "0"

        dfs(x+1,y,grid)
        dfs(x-1,y,grid)
        dfs(x,y+1,grid)
        dfs(x,y-1,grid)

        return 

    for i in range(r):
        for j in range(c):
            if grid[i][j] == "1":
                dfs(i,j,grid)
                count += 1
    
    return count


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


print(solution(grid))