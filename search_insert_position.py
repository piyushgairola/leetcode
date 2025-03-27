import time


def search_insert(nums, target):    # My code
    start = 0
    end = len(nums)

    while start < end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            start = mid + 1

        else:
            end = mid

    return end


def searchInsert(nums,target):      # Faster and better version of code.
    start, end = 0, len(nums)-1
    while start < end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            start = mid + 1

        else:
            end = mid

    if end == len(nums) - 1 and target > nums[-1]:
        return len(nums)
    return end


if __name__ == '__main__':
    nums = [1, 2, 4, 5, 6, 8, 9]
    target = 10
    t0 = time.time()
    print(search_insert(nums, target), end=' ')
    print(time.time() - t0)

    t1 = time.time()
    print(searchInsert(nums, target), end=' ')
    print(time.time() - t1)