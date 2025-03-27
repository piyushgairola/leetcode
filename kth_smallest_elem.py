def kthSmallest(matrix,k):
    arr = []
    n = len(matrix)
    for i in range(n):
        arr.extend(matrix[i])
        arr = list(set(arr))
        
    return arr[k-1]


mat = [[1,5,9],[10,11,13],[12,13,15]]

print(kthSmallest(mat,8))