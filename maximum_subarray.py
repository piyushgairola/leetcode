def solution(nums):
    curr_sum = 0
    max_sum = float('-inf')


    for i in nums:
        curr_sum += i
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0


    return max_sum


def solution1(nums):
    ## this handle the edge case such as all negative element in nums, this will return the least negative sum
    curr_sum = max_sum = nums[0] 
    
    for i in nums[1:]:
        curr_sum = max(curr_sum+i, i) ## decide if extending curr_elm give larger sum or keeping only curr_elm gives larger sum
        max_sum = max(curr_sum,max_sum)

    return max_sum



def solution2(nums):
    curr_sum = max_sum = nums[0]
    start_idx = end_idx = temp_start =  0

    for i in range(1, len(nums)):
        if nums[i] > curr_sum + nums[i]:
            temp_start = i
            curr_sum = nums[i]
        else:
            curr_sum += nums[i]
        
        
        if max_sum < curr_sum:
            max_sum = curr_sum
            start_idx = temp_start
            end_idx = i


    return max_sum, start_idx, end_idx, nums[start_idx:end_idx+1]

        
nums = [5,4,-1,7,8]
print(solution2(nums))


