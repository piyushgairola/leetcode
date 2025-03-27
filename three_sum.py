# def threeSum(nums):
#     result = []
#     for i,v in enumerate(nums):
#         temp = twoSum(nums[i+1:],-(v))
#         if temp:
#             for i in temp:
#                 res = [v]
#                 res.extend(i)
#                 result.append(res)
    
#     return result
    
# def twoSum(nums,target):
#     memo={}
#     result = []
#     for i,v in enumerate(nums):
#         if v in memo:
#             memo[v].append(v)
#             result.append(memo[v]) 
#         else:
#             t = target - v
#             memo[t] = [v]
    
#     return result


def threeSum(nums):
    _nums = sorted(nums)

    for i,v in enumerate(_nums):
        


if __name__ == '__main__':
    ip = [-1,0,1,2,-1,-4]
    print(threeSum(ip))