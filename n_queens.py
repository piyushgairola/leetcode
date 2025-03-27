from time import time
def solveNQueens(n):
    def dfs(queens,reverse_diag,normal_diag):
        row = len(queens)
        if row == n:
            result.append(queens)
            # result +=1
            return None

        for col in range(n):
            if col not in queens and row-col+n-1 not in reverse_diag and row+col not in normal_diag:
                dfs(queens+[col], reverse_diag+[row-col+n-1], normal_diag+[row+col])


    result =[]
    dfs([],[],[])

    return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
    


def solveNQueensBitmask(n):
    def dfs(queen,column,normal_diag, reverse_diag):
        row = len(queen)
        if row == n:
            result.append(queen)
            return
        
        for col in range(n):
            if column & 1<<col or normal_diag & (1<<row+col) or reverse_diag & (1<< row-col+n-1):
                continue
            dfs(queen+[col],column ^ 1<<col, normal_diag ^ 1<<(row+col), reverse_diag ^ 1<<(row-col+n-1))

    result = []
    dfs([],0,0,0)
    # return result
    return [["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


start_time = time()
print(solveNQueensBitmask(4))
print(f"time taken: {((time()-start_time))*1000}")

start_time = time()
print(solveNQueens(4))
print(f"time taken: {((time()-start_time))*1000}")