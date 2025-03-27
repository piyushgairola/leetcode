def maxProduct(nums):
    n = len(nums)
    curr_max =curr_min = max_ans = nums[0]

    for i in range(1,n):
        curr_max = max(curr_max*nums[i], curr_min*nums[i], nums[i])
        curr_min = min(curr_min*nums[i], curr_min*nums[i], nums[i])

        max_ans = max(max_ans,curr_max)

    return max_ans


nums = [0,2]
print(maxProduct(nums))