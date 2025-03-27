def right_interval(intervals):
    res = []*len(intervals)
    dict_0 = {}
    dict_1 = {}
    sort_intervals = sorted(intervals)
    x = sort_intervals.pop(0)
    max_1 = x[1]
    dict_0[x[0]] = 0
    dict_1[x[1]] = 0

    for i, elem in enumerate(sort_intervals):
        if elem[0] > max_1:
            # res[] = i
            # to-do
            pass

        if elem[1] in dict_0.keys():
            res.append(dict_0[elem[1]])

        else:
            res.append(-1)

        dict_0[elem[0]] = i
        dict_1[elem[1]] = i

    return res


if __name__ == '__main__':
    intervals = [[4,5],[2,3],[1,2]]
    print(right_interval(intervals))