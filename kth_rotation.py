# Given an increasing sorted rotated array arr of distinct integers. 
# The array is right-rotated k times. Find the value of k.

def findKRotation(arr):
    # code here
    # k = 0
    # for i in range(len(arr)):
    #     if arr[i] <= arr[k]:
    #         k = i
    # return k
    left = 0
    right = len(arr)-1
    
    if arr[left] <= arr[right]:
        return 0
        
    while left <= right:
        mid = (left + right) // 2
        
        if mid < right and arr[mid] > arr[mid + 1]:
            return mid + 1
            
        if mid > left and arr[mid] < arr[mid - 1]:
            return mid
        
        if arr[mid] >= arr[left]:
            left = mid + 1
        else:
            right = mid - 1
            
    return 0

print(findKRotation([5, 1, 2, 3, 4]))
print(findKRotation([1, 2, 3, 4, 5]))
print(findKRotation([6, 9, 2, 4]))