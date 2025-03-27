def isInterleave(s1,s2,s3):
    if len(s1)+len(s2) != len(s3):
        return False

    memo = [[-1]*len(s2) for _ in range(len(s1))]

    return check(s1,s2,s3,0,0,0,memo)


def check(s1,s2,s3,i,j,k,memo):
    if i == len(s1):
        return s2[j:] == s3[k:]
    
    if j == len(s2):
        return s1[i:] == s3[k:]

    if memo[i][j] >= 0:
        return True if memo[i][j] == 1 else False
    
    ans = False
    if((s1[i]==s3[k] and check(s1,s2,s3,i+1,j,k+1,memo)) or (s2[j]==s3[k] and check(s1,s2,s3,i,j+1,k+1,memo))):
        ans = True
    
    if ans:
        memo[i][j] = 1
    else:
        memo[i][j] = 0

    return ans


if __name__ == "__main__":
    s1 = "aabc"
    s2 = "abad"
    s3 = "aabadabc"

    print(isInterleave(s1,s2,s3))
