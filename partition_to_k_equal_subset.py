def canPartitionKSubsets(nums,k):
    if len(nums)<k or sum(nums) % k != 0 or max(nums) > sum(nums)//k:
            return False
        
    nums.sort(reverse=True)
    subset=[0]*k
    target = sum(nums)//k
    
    def dfs(idx):
        if idx == len(nums):
            return True
        
        seen = []
        for i in range(k):
            if subset[i] in seen:
                continue
            if subset[i] + nums[idx] <= target:
                seen.append(subset[i])
                subset[i] += nums[idx]
                
                if dfs(idx+1):
                    return True
                
                subset[i] -= nums[idx]
                
        return False
    
    return dfs(0)


nums = [4,3,2,3,5,2,1]
k = 4
print(canPartitionKSubsets(nums,k))