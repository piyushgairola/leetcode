from collections import deque

def maxSlidingWindow(nums,k):
    d = deque()
    res = []

    for i,val in enumerate(nums):
        while d and nums[d[-1]] < val:
            d.pop()

        d += [i]

        if d[0] == i-k:
            d.popleft()

        if i>=k-1:
            res.append(nums[d[0]])

    return res


nums = [8,7,6,5,4,3,2,1]
print(maxSlidingWindow(nums,3))