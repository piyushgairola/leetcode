def countBinarySubstring(s):
    ans, prev, curr = 0,0,1

    for i in range(1,len(s)):
        if s[i-1] != s[i]:
            ans+=min(prev,curr)
            prev=curr
            curr=1
        else:
            curr +=1

    ans += min(prev,curr)
    return ans

if __name__ == '__main__':
    s = "0110001111"
    print(countBinarySubstring(s))