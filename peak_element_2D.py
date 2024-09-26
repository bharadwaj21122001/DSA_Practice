# peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left,
# right, top, and bottom.
# Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, 
# find any peak element mat[i][j] and return the length 2 array [i,j].
# You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.
# You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

def findPeakGrid(mat):
    # low = 0
    # high = 0

    # for i in range(len(mat)):
    #     for j in range(len(mat[i])):
    #         if mat[i][j] >= mat[low][high]:
    #             low = i
    #             high = j
    # return [low, high]

    m = len(mat)
    n = len(mat[0])

    left = 0
    right = m - 1

    while left <= right:
        mid_row = (left + right) // 2

        max_col = 0

        for i in range(n):
            if mat[mid_row][i] > mat[mid_row][max_col]:
                max_col = i

        if mid_row > 0:
            top_neighbor = mat[mid_row - 1][max_col]
        else:
            top_neighbor = -1
        if mid_row < m - 1:
            bottom_neighbor = mat[mid_row + 1][max_col]
        else:
            bottom_neighbor = -1
        
        if mat[mid_row][max_col] > top_neighbor and mat[mid_row][max_col] > bottom_neighbor:
            return [mid_row, max_col]
        elif mat[mid_row][max_col] < top_neighbor:
            right = mid_row - 1
        else:
            left = mid_row + 1
    return [-1, -1]

print(findPeakGrid([[1,4],[3,2]]))
print(findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]))