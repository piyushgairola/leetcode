"""
time complexity : O(n)
space complexity : O(1)
"""

def find_duplicate(nums):
    solution = []
    n = len(nums)
    for idx in range(n):
        if nums[abs(nums[idx])-1] < 0:
            solution.append(abs(nums[idx]))
        nums[abs(nums[idx])-1] *= -1

    return solution


if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    print(find_duplicate(nums))