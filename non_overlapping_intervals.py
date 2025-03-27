def non_overlapping(intervals):
    count = 0
    n = len(intervals)
    map = {}
    for i in range(n):
        _n = len(intervals[i])
        temp = intervals[i]
        flag = False
        j = 0
        while(j<_n and not flag):
            if j not in map.keys():
                map[j] = []

            if temp[j] in map[j]:
                flag = True
            else:
                map[j].append(temp[j])

            j +=1

        if flag:
            count+=1

    return count


if __name__ == '__main__':
    inter  = [[1,2],[2,3]]
    print(non_overlapping(inter))