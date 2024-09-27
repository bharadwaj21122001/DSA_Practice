# Given a row wise sorted matrix of size R*C where R and C are always odd, find the median of the matrix.

def median(matrix, R, C):
    #code here 
    n = R * C
    arr = []

    for i in range(R):
        for j in range(C):
            arr.append(matrix[i][j])
    
    arr.sort()
    
    if n % 2 == 0:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        return arr[n // 2]
    
print(median([[1, 3, 5], [2, 6, 9], [3, 6, 9]], 3, 3))
print(median( [[1], [2], [3]], 3, 1))