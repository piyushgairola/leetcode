def nextPermutation(nums):
    l = len(nums)-1
    idx=-1
    for i in range(l,0,-1):
        if nums[i] > nums[i-1]:
            idx = i-1
            break

    for i in range(l,idx,-1):
        if nums[idx]<nums[i]:
            nums = swap(nums,idx,i)
            break

    nums = reverse(nums,idx+1,l)

            
    if(idx<0):
        nums.sort()

    return nums


def swap(nums,a,b):
    t = nums[a]
    nums[a] = nums[b]
    nums[b] = t
    return nums

def reverse(nums,start,end):
    while(start<end):
        swap(nums,start,end)
        start +=1
        end -=1

    return nums


if __name__ == '__main__':
    arr= [1,4,3,3,3 ]
    print(nextPermutation(arr))
    