def missingNumber(nums):
    n = len(nums)
    actual_sum = sum(nums)
    expected_sum = n*(n+1)//2

    return expected_sum-actual_sum


def missingNumber_bitManipulation(nums):
    missing = len(nums)
    for i,val in enumerate(nums):
        missing ^= i^val

    return missing


nums = [3,0,1]
print(missingNumber_bitManipulation(nums))