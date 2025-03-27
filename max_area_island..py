def maxArea(grid):
    r, c = len(grid), len(grid[0])
    max_area = 0

    def dfs(x, y, grid):
        if x < 0 or y < 0 or x >= r or y >= c or grid[x][y] == 0:
            return 0
        grid[x][y] = 0

        up = dfs(x-1, y, grid)
        down = dfs(x+1, y, grid)
        left = dfs(x, y-1, grid)
        right = dfs(x, y+1, grid)

        return up+down+left+right+1

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                max_area = max(dfs(i, j, grid), max_area)

    return max_area


if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
        0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]


    print(maxArea(grid))