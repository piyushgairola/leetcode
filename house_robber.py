def solution(nums):
    dp1,dp2=0,0

    for n in nums:
        dp1,dp2 = dp2,max(dp1+n,dp2)

    return dp2

nums = [2,7,9,3,1]
print(solution(nums))