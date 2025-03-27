def findErrorNums(nums):
    l = len(nums)+1
    # visited = set()
    # miss = set()
    # dup = None
    
    # for i in range(1,l):
    #     if nums[i-1] in visited:
    #         dup = nums[i-1]

    #     if nums[i-1] != i and i not in visited:
    #         miss.add(i)

    #     if nums[i-1] in miss:
    #         miss.remove(nums[i-1])

    #     visited.add(nums[i-1])

    # return [dup,list(miss)[0]]

    visited = {}
    for i in range(1,l):
        if nums[i-1] not in visited:
            visited[nums[i-1]] = 1
        else:
            visited[nums[i-1]] += 1 

    dup = 


if __name__ == '__main__':
    arr = [3,2,3,4,6,5]
    print(findErrorNums(arr))