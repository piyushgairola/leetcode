def solution(s):
    n = len(s)
    ans = 0
    if n < 1:
        return 0
    
    distinct_char_set = set(s[0])
    ans = 1 ## because we added s[0]

    for r in range(1,n):
        if s[r] in distinct_char_set:
            while l<r and s[r] in distinct_char_set:
                distinct_char_set.remove(s[l])
                l +=1
        
        distinct_char_set.add(s[r])

        ans = max(ans, r-l+1)

    return ans


def solution1(s):
    n = len(s)
    l = 0 ## assign the initial starting index of the current sub string
    ans = 0
    distinct_set = set()    ## set to keep track of distinct char in sub_string

    for r in range(n):  
        while(s[r] in distinct_set):    ## if the curr_char in the distinct_set, then 
            distinct_set.remove(s[l])   ## remove the starting char of the substring from the distinct_set
            l += 1                      ## move the starting index of the sub_string
        
        distinct_set.add(s[r])          ## now, add the curr_char in the distinct_set
        ans = max(ans, r-l+1)           ## update the ans

    return ans
    
s = " "

print(solution1(s))
