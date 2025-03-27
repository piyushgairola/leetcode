from collections import Counter

def numFriendRequests(ages):
        count = 0
        counter = {}
        l = len(ages)
        for i in ages:
            if i in counter:
                counter[i]+=1
            else:
                counter[i] = 1
                
        for i in counter:
            for j in counter:
                if check(i,j):
                    if i==j:
                        count += counter[i]*(counter[i]-1)
                    else:
                        count += counter[i]*counter[j]
                    
        
        return count
    
def check(a,b):
    if((b<= (int(0.5*a)+7)) or b>a):
        return False
    else:
        return True


if __name__ == "__main__":
    arr = [20,30,100,120,110]
    print(numFriendRequests(arr))