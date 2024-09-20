# Given an unsorted array arr[] of integers and an integer x, find the floor and ceiling of x in arr[].
# Floor of x is the largest element which is smaller than or equal to x. 
# Floor of x doesn’t exist if x is smaller than smallest element of arr[].
# Ceil of x is the smallest element which is greater than or equal to x. 
# Ceil of x doesn’t exist if x is greater than greatest element of arr[].
# Return an array of integers denoting the [floor, ceil]. Return -1 for floor or ceiling if the floor or ceiling is not present.
# This problem can be solved in two methods, one is binary search and another is iterating through each element, 
# and comparing with 'x' to determine floor and ceil.

def getFloorAndCeil(x, arr):
        # code here
        # arr.sort()
        # left = 0
        # right = len(arr)-1
        floor = -1
        ceil = -1
        
        for i in arr:
            if i <= x and i > floor:
                floor = i
            if i >= x and (ceil == -1 or i < ceil):
                ceil = i
        
        # while left <= right:
        #     mid = (left + right) // 2
            
        #     if arr[mid] == x:
        #         return x, x
                
        #     if arr[mid] < x:
        #         floor = arr[mid]
        #         left = mid + 1
        #     else:
        #         ceil = arr[mid]
        #         right = mid - 1
                
        return floor, ceil

print(getFloorAndCeil(7, [5, 6, 8, 9, 6, 5, 5, 6]))
print(getFloorAndCeil(10, [5, 6, 8, 8, 6, 5, 5, 6]))