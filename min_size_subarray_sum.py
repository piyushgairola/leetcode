def solution(nums, target):
    if sum(nums) < target:
        return 0
    

    n = len(nums)
    curr_sum = 0
    l = 0
    min_len = n+1
    for r in range(n):
        curr_sum += nums[r]

        while curr_sum >= target:
            min_len = min(min_len, r-l+1)
            curr_sum -= nums[l]
            l += 1
    
    return min_len if min_len != n+1 else 0


nums = [2,3,1,2,4,3]
target = 7
print(solution(nums,target))
