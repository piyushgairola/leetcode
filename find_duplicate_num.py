def solution_array_changed(nums):
    n = len(nums)
    
    for i in range(n):
        idx = abs(nums[i])-1

        if nums[idx] <0:
            return idx+1
        else:
            nums[idx] *= -1


def solution_constant_space(nums):
    slow = nums[0]
    fast = nums[0]

    while True: ## to detect the cycle in nums array
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:    ## once the cycle is detected, 
            break           ## we break out to get the start of cycle, which will be duplicate element

    slow = nums[0]
    while slow != fast: ## finding the start of the cycle,i.e, duplicate element
        slow = nums[slow]
        fast = nums[fast]

    return slow


nums = [3,1,3,4,2]
# print(solution_array_changed(nums))
print(solution_constant_space(nums))