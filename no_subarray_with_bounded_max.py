def numSubarray(nums, L, R):
    # res,dp =0,0
    # prev = -1

    # for i in range(len(nums)):
    #     if nums[i] < L and i>0:
    #         res += dp
        
    #     if nums[i] > R:     ## when no sub-array exist for i
    #         dp = 0          ## so we make dp = 0
    #         prev = i        ## and store the index

    #     if L <= nums[i] <= R:
    #         dp = i-prev
    #         res += dp

    # return res

    window_open = 0
    ans = 0
    temp = 0

    for i,val in enumerate(nums):
        if L<= val <= R:
            temp = i - window_open + 1
            ans += temp
        elif val < L:
            ans += temp
        else:
            window_open = i +1
            temp = 0

    return ans


nums = [2,1,4,2,3]

print(numSubarray(nums, 2,4))