def solution(nums):
    n = len(nums)
    visited = [False]*n

    for i in nums:
        visited[i-1] = True

    return [ i+1 for i in range(n) if visited[i] == False]


def solution_no_extra_space(nums):
    n = len(nums)
    for elem in nums:
        idx = abs(elem) - 1
        if nums[idx] > 0:
            nums[idx] *= -1

    return [i+1 for i in range(n) if nums[i]>0]

    



nums = [4,3,2,7,8,2,3,1]

print(solution_no_extra_space(nums))

