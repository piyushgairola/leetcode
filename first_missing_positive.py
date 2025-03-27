# def firstMissingPositive(nums):
#     n = len(nums)
#     i = 0
#     while(i<n):
#         if(nums[i]>=1 and nums[i]<n and nums[nums[i]-1] != nums[i]): # IMPORTANT. UNDERSTAND PROPERLY
#             nums = swap(nums,i,nums[i]-1)
#         else:
#             i+=1
    
#     i = 0
#     while(nums[i]<n and nums[i] == i+1):
#         i+=1
    
#     return i+1


# def swap(nums,i,j):
#     t = nums[i]
#     nums[i] = nums[j]
#     nums[j] = t
#     return nums


# if __name__ == '__main__':
#     arr = [0,2,2,1,3]
#     print(firstMissingPositive(arr))


def solution(nums):
    n = set(nums)
    i = 1

    while True:
        if i in n:
            i += 1
        else:
            return i


nums = [3,4,-1,1]
print(solution(nums))