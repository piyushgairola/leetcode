def twoSum(nums,target):
    # seen = {}
    # for i, v in enumerate(nums):
    #     remaining = target - v
    #     if remaining in seen:
    #         return [seen[remaining], i]
    #     seen[v] = i
    # return []

    memo={}
    for i,v in enumerate(nums):
        if v in memo.keys():
            memo[v].append(i)
            return memo[v]
        else:
            t = target-v
            memo[t] = [i]


if __name__ == '__main__':
    nums = [3,3]
    target = 6

    print(twoSum(nums,target))
