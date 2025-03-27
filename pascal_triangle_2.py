def pascal_triangle(k):
    res = []
    for i in range(k+1):
        temp = []
        for j in range(i+1):
            if j==0 or i==j:
                temp.append(1)
            else:
                a = res[i-1][j-1]
                b = (res[i-1][j])
                temp.append(a+b)
        res.append(temp)

    return res


if __name__ == '__main__':
    print(pascal_triangle(3))