def solution(s, k):
    vowels_list = ['a','e','i','o','u']
    curr_count = 0
    for i in range(k):
        if s[i] in vowels_list:
            curr_count += 1

    p1 = 0
    max_count = curr_count
    for i in range(k,len(s)):
        if s[i] in vowels_list:
            curr_count += 1
        if s[p1] in vowels_list:
            curr_count -=1

        max_count = max(max_count, curr_count)
        
        p1 +=1

    return max_count


## the above solution gives better time in leetcode than the below solution

def solution1(s,k):
    vowel_set = frozenset(['a','e','i','o','u'])

    curr_count = max_count = 0
    for i in range(len(s)):
        if s[i] in vowel_set:
            curr_count += 1
        if i>=k and s[i-k] in vowel_set:
            curr_count -= 1
        
        max_count = max(curr_count, max_count)

    return max_count

s = "tryhard"
k = 4
print(solution1(s,k))