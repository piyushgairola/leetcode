def solution(nums, k):
    result = 0
    
    for i in range(len(nums)-k + 1):
        curr_avg = sum(nums[i:i+k]) / k
        result = max(curr_avg, result)

    return result


nums = [1,12,-5,-6,50,3]
k = 4

# print(solution(nums, k))

def solution1(nums,k):
    
    
    ## we are only concerned about the sum of elements from idx to idx+k
    ## hence we only calculate the pre_sum of the array within the window of [idx,idx+k]
    
    # pre_sum = [0]*len(nums)
    # avg_list = []
    
    # for idx,val in enumerate(nums):
    #     pre_sum[idx] = pre_sum[idx-1] + val

    # for i in range(k-1,len(nums)):
    #     if i-k >= 0:
    #         avg_list.append((pre_sum[i] - pre_sum[i-k] )/ k)
    #     else:
    #         avg_list.append(pre_sum[i] / k)

    # return max(avg_list)


    curr_sum = max_sum = sum(nums[:k])

    for i in range(k, len(nums)):
        curr_sum = nums[i] - nums[i-k]
        max_sum = max(max_sum,curr_sum)

    return max_sum/k
        

nums = [-1]
k = 1 #constraint k <= n

print(solution1(nums, k))