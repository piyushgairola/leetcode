def solution(n):
    if n < 0:
        return 0
    if n == 1 or n==2:
        return n

    return solution(n-1) + solution(n-2)

# print(solution(4))

def climbStairs(n):
    memo = {} ## to store the previous results
    memo[1] = 1 ## number of ways to reach step 1 = 1
    memo[2] = 2 ## number of ways to reach step 2 = 2

    def utils(n):
        if n in memo: ## if the result is already stored in the memo, return it
            return memo[n]

        ## store the number of ways to climb n steps in the memo 
        ## by calling the function recursively for n-1 and n-2
        memo[n] = utils(n-1) + utils(n-2)
        return memo[n] ## return the number of ways to reach n steps

    return utils(n)

print(climbStairs(2))


def solution(n):
    memo = {}
    memo[1] = 1
    memo[2] = 2

    ## we start from bottom and build the solution for n
    for i in range(3,n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]