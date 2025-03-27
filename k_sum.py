def twoSum(nums,target):
    memo={}
    res=[]
    for v in nums:
        if v in memo:
            memo[v].append(v)
            res.append(memo[v])
        else:
            t = target-v
            memo[t] = [v]
    
    return res


def ksum(k,idx,target,nums):
    if k==2:
        res = twoSum(nums[idx:],target)
    else:
        res = []
        for i in range(idx,len(nums)-k+1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            temp = ksum(k-1,i+1,target-nums[i],nums)

            if temp:
                for j in range(len(temp)):
                    temp[j].insert(0,nums[i])
            
            res.extend(temp)

    return res


if __name__=='__main__':
    arr = [-1,0,1,2,-1,-4]
    arr = sorted(arr)
    print(ksum(3,0,0,arr))
