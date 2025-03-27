def solution(nums):
    p1 = 0
    n = len(nums)

    for i in range(1,n):
        if nums[i] == nums[p1]:
            pass
        else:
            p1 += 1
            nums[p1] = nums[i] 
            # nums[i] = "_"

    return p1 + 1, nums


nums = [0,0,1,1,1,2,2,3,3,4]
result = solution(nums)
print(result)

nums = [1,2]
result = solution(nums)
print(result)