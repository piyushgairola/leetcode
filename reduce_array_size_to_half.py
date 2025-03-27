from collections import Counter

# def minSetSize(arr):
#     count_map = Counter(arr)
#     freq = list(count_map.values())
#     freq.sort()

#     half_size = len(arr)//2
#     ans, reduced = 0,0
#     while reduced<half_size:
#         ans += 1
#         reduced += freq.pop()

#     return ans


def minSetSize(arr):
    count_map = {}
    for i in arr:
        if i in count_map:
            count_map[i] += 1
        else:
            count_map[i] = 1

    freq = list(count_map.values())
    freq.sort()
    half_size = len(arr)//2
    ans, reduced = 0,0
    while reduced<half_size:
        ans += 1
        reduced += freq.pop()

    return ans



arr = [1,2,3,4,5,6,7,8,9,10]
print(minSetSize(arr))