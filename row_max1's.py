# You are given a 2D array consisting of only 1's and 0's, where each row is sorted in non-decreasing order. 
# You need to find and return the index of the first row that has the most number of 1s. 
# If no such row exists, return -1.

def rowWithMax1s(arr):
    # code here
    ones_row = -1
    count = 0
    
    for i in range(len(arr)):
        first_one = first_ones(arr[i])
        if first_one != -1:
            ones_count = len(arr[i]) - first_one
            if ones_count > count:
                count = ones_count
                ones_row = i
    return ones_row

def first_ones(row):
        low = 0
        high = len(row) - 1
            
        while low <= high:
            mid = (low + high) // 2
            
            if row[mid] == 1:
                if mid == 0 or row[mid - 1] == 0:
                    return mid
                else:
                    high = mid - 1
            else:
                low = mid + 1
        return -1

print(rowWithMax1s([[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]))
print(rowWithMax1s([[0, 0], [1, 1]]))