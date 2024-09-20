# Given a sorted array arr[] of size n without duplicates, and given a value x. 
# Floor of x is defined as the largest element k in arr[] such that k is smaller than or equal to x. 
# Find the index of k(0-based indexing).

def findFloor(A,N,X):
        #Your code here
        low = 0
        high = N-1
        result = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            if A[mid] <= X:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return result

print(findFloor([1,2,8,10,11,12,19], 7, 0))
print(findFloor([1,2,8,10,11,12,19], 7, 5))