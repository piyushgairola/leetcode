def solution(nums, k):
    nums.sort()

    p1 = 0
    p2 = len(nums) - 1

    result = 0

    while p1 < p2:
        curr_sum = nums[p1] + nums[p2]
        if curr_sum == k:
            p1 +=1
            p2 -= 1
            result += 1
        elif curr_sum > k:
            p2 -= 1
        else:
            p1 += 1
    
    return result
    


nums = [4,4,1,3,1,3,2,2,5,5,1,5,2,2,3,5,4]
k = 2


print(solution(nums, k))


### think solution with collections.Counter