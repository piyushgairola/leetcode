def distributeCandies(candyType):
    l = len(candyType)
    candy = []
    i=0
    for j in range(l):
        if candyType[j] not in candy:
            candy.append(candyType[j])
            i+=1
            
    if i < l//2:
        return i
    else:
        return l//2




if __name__ == '__main__':
    print(distributeCandies([6,6,6,6]))