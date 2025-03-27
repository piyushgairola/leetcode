def containsNearbyAlmostDuplicate(nums, k, t):
    for i in range(len(nums)):
        j= 1
        while(j<k+1 and i+j< len(nums)):
            if abs(nums[i] - nums[i + j]) <= t:
                return True
            j+=1
    return False


if __name__ == '__main__':
    nums = [2,2]
    print(containsNearbyAlmostDuplicate(nums,3,0))