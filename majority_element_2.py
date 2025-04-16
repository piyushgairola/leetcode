def solution1(nums):
    n = len(nums)
    threshold = n//2
    count = 0
    candidate = 0

    for i in range(n):
        if count == 0:
            candidate = nums[i]

        if nums[i] == candidate:
            count += 1
        else:
            count -=1


    return candidate if count > threshold else -1



def solution(nums):
    n = len(nums)
    result = []
    threshold = n//3
    
    
    candidate1 = candidate2 = 0 ## As threshold is n/3, there can only be 2 majority elements
    count1 = count2 = 0 ## each majority element count


    for i in range(n):
        if count1 == 0: ## if the count for candidate1 is 0, meaning no candidate1,
            candidate1 = nums[i]    ## we assign curr_elm as candidate1
            count1 += 1             ## and update its count

        elif count2 == 0:   ## if the count for candidate2 is 0, meaning no candidate2,
            candidate2 = nums[i]    ## we assign curr_elm as candidate1
            count2 += 1             ## and update its count

        elif nums[i] == candidate1: ## check if the curr_elem is majority candidate1,
            count1 +=1  ## update the candidate1 count
        
        elif nums[i] == candidate2: ## else check if the curr_elem is majority candidate2,
            count2 += 1 ## update the candidate2 count

        else:       ## if curr_elem is not candidate1 or candidate2, we decrement both candidates count
            count1 -= 1 
            count2 -= 1

    ## above for loop helps in identifying the majority elements, 
    ## but the current count1 and count2 after for loop, would not be equal to their occurrence in nums
    ## hence, calculating their correct occurrence.
    count1 = count2 = 0
    for i in range(n):
        if nums[i] == candidate1:
            count1+=1 
        elif nums[i] == candidate2:
            count2 += 1
    
    if count1>threshold:    ## checking if count for candidate1 is more than threshold
        result.append(candidate1)   ## if yes, adding to result
    if count2>threshold:    ## checking if count for candidate2 is more than threshold
        result.append(candidate2)    ## if yes, adding to result

    return result

nums = [1, 2, 2, 2, 4, 4, 4]
print(solution(nums))

nums = [1, 2, 2, 4, 4, 4]
print(solution(nums))




def max_session(meeting):
    sz = len(meeting)
    umap = {}
    last_meeting_end = meeting[0][1]
    for i in range(sz):
        umap[meeting[i][0]] = umap.get(meeting[i][0], 0) + 1
        umap[meeting[i][1]] = umap.get(meeting[i][1], 0) - 1
        last_meeting_end = max(last_meeting_end, meeting[i][1])

    sum_ = umap.get(0, 0)
    ans = sum_
    for i in range(1, last_meeting_end + 1):
        sum_ += umap.get(i, 0)
        if sum_ > ans:
            ans = sum_
    return ans




meeting = [[1,4],[3,5],[2,7],[5,10]]
print(max_session(meeting))
