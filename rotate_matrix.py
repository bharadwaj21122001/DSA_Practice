def rotate(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(len(matrix)):
            matrix[i].reverse()
        return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))