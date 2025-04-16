def solution(nums,target):
    l = 0
    r = len(nums)-1

    while l<=r: ## binary search is implemented as the array is sorted
        m = (l+r)//2

        if nums[m] == target:
            return m
        
        elif nums[l] <= nums[m]:    ## as the array is rotated, first check if the left sub-array is sorted
            if nums[l] <= target <= nums[m]:    ## if it is then, check if the target value lies in left sub-array
                r = m-1 ## if yes, then update the right index.
            else:
                l = m+1 ## else, the target value must lie in right sub-array, hence update the left index

        else:
            if nums[m] <= target <= nums[r]:    ## check if the target value lies in the sorted right sub-array
                l = m+1     ## if yes, update the left index
            else:
                r = m-1     ## else, update the right index


    return -1   ## if target not present, return -1


nums = [4,5,6,7,0,1,2]
target = 3
print(solution(nums,target))