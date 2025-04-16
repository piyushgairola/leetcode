import time

def longestConsecutive(nums):
    start_time = time.time()
    nums = set(nums)
    ans = 0

    for x in nums:
        if x-1 not in nums:
            y = x+1
            while y in nums:
                y+=1
            
            ans = max(ans, y-x)
    end_time = time.time()
    print(f"time taken == {end_time-start_time}")
    return ans

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))



## I prefer this solution because it is more readable and easy to understand.
def solution(nums):
    start_time = time.time()
    if not nums: # if nums is empty
        return 0
    nums = sorted(set(nums)) # to handle duplicates

    max_length = 0
    n = len(nums)
    curr_length = 1

    for i in range(1,n):
        if nums[i] == nums[i-1] + 1:
            curr_length += 1
        else:
            max_length = max(max_length, curr_length)
            curr_length = 1
    
    max_length = max(max_length, curr_length)
    end_time = time.time()
    print(f"time taken == {end_time-start_time}")
    return max_length


print(solution([0,3,7,2,5,8,4,6,0,1]))
# print(solution([]))