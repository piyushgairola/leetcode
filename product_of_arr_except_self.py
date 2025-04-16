
## Invalid Solution. Does not work with element 0. Only for understanding.
def solution_with_divide(nums):
    prod = 1
    n = len(nums)
    for i in range(n):
        prod *= nums[i]

    for i in range(n):
        nums[i] = prod // nums[i]

    return nums


def solution_using_prefix_suffix(nums):
    n = len(nums)
    prefix_prod = [1]*n ## to calculate the product from 0 to i-1
    suffix_prod = [1]*n ## to calculate the product from i+1 to n-1

    for i in range(1,n):
        prefix_prod[i] = prefix_prod[i-1] * nums[i-1]   ## to calculate the product of all element before i

    for i in range(n-2, -1, -1):
        suffix_prod[i] = suffix_prod[i+1] * nums[i+1]   ## to calculate the product of all element after i

    result = [prefix_prod[i]*suffix_prod[i] for i in range(n)] ## product of all element before i and after i

    return result

def solution_space_optimized(nums):
    n = len(nums)
    result = [1]*n

    for i in range(1,n):
        result[i] = result[i-1]*nums[i-1]   ## prefix product

    suffix_prod = 1 ## to store the product of i+1 to n elements
    for i in range(n-1,-1,-1): ## we start with last element, multiply by 1[suffix_prod]
        result[i] *= suffix_prod ## update the product with product of i+1 to n
        suffix_prod *= nums[i] ## update the product with curr_elm for next iteration.

    return result





nums = [1,2,3,4]
print(solution_using_prefix_suffix(nums))
print(solution_space_optimized(nums))