def solution(board, word):
    r = len(board)
    c = len(board[0])
    len_word = len(word)

    def dfs(x,y,z):
        if z == len_word:   ## base condition, if we have matched all the chars of the word
            return True     ## return True.
        
        if x<0 or x>=r or y<0 or y>=c or board[x][y] != word[z]:    ## Base condition, for false scenarios
            return False
        
        temp_word = board[x][y]
        board[x][y] = ''    ## to mark the curr cell as visited, we replace the character with empty string.

        if dfs(x+1,y,z+1) or dfs(x-1,y,z+1) or dfs(x,y-1,z+1) or dfs(x,y+1,z+1): ## word can be created by horizontally or vertically traversing
            return True
        
        board[x][y] = temp_word ## replace the current cell value to its original for later traversal.
        return False


    for i in range(r):
        for j in range(c):
            if dfs(i,j,0):  ## check from each cell in the board
                return True
            
    return False


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

print(solution(board,word))
