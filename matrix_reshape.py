def matrixReshape(mat,r,c):
    _r,_c = len(mat),len(mat[0])
    if r*c != _r*_c:
        return mat

    _mat = [[0]*c for _ in range(r)]
    count = 0
    for i in range(_r):
        for j in range(_c):
            _mat[count//c][count%c] = mat[i][j]
            count += 1


    return _mat



mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
print(matrixReshape(mat,2,10))