nums = [1,2,3,4,5,6,7,8]
n = len(nums)
k = 17

# print(nums[n-k:])
# print(nums[:n-k])
# print(nums[n-k:] + nums[:n-k])

# nums1 = [1,2]
# print(nums1[-6:])


def rotate(nums, k):
    new_list = []
    result = []
    while k > 0:
        new_list.insert(0, nums.pop())
        k -= 1
    new_list.extend(nums)
    return new_list


def rotate_inplace(nums, k):
    while k >0:
        nums.insert(0, nums.pop())
        k -= 1
    return nums


def rotate_inplace2(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums


def rotate_inplace3(nums, k):
    n = len(nums)
    # k = k%n
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums

result = rotate_inplace2(nums, k)
print(result)