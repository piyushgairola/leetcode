from time import time


"""
Time Complexity : O(n^2)
"""
def lis(arr):
    """
    dp[i] is the length of longest increasing subsequence for index i in arr
    We initialize dp with all 1 because initially every element will contribute length 1 in LIS. 
    if only one element, LIS length will be 1
    """
    n = len(arr)
    dp = [1] * n

    for i in range(1,n):
        for j in range(0,i):
            if arr[j]<arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)


def lis_seq(arr):
    """
    returns the sequence
    """
    n = len(arr)
    dp = [1]*n
    p = [-1]*n  

    for i in range(1,n):
        for j in range(0,i):
            if arr[j]<arr[i] and dp[i]<dp[j]+1:
                dp[i] = dp[j]+1
                p[i] = j


    ans,pos = dp[0],0
    for i in range(1,n):
        if dp[i]>ans:
            ans = dp[i]
            pos = i


    seq = []
    while(pos != -1):
        seq.insert(0,arr[pos])
        pos = p[pos]

    return seq





if __name__ == '__main__':
    arr = [0,1,0,3,2,3]
    print(lis_seq(arr))