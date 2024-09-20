# You're given a sorted array 'a' of 'n' integers and an integer 'x'.
# Find the floor and ceiling of 'x' in 'a[0..n-1]'.
# Floor of 'x' is the largest element in the array which is smaller than or equal to 'x'.
# Ceiling of 'x' is the smallest element in the array greater than or equal to 'x'.
# This solution can be solved using binary search.

def getFloorAndCeil(a, n, x):
    # Write your code here.
    floor = -1
    ceil = -1
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == x:
            return [x, x]
        if a[mid] < x:
            floor = a[mid]
            low = mid + 1
        else:
            ceil = a[mid]
            high = mid - 1
    return floor, ceil

print(getFloorAndCeil([3, 4, 4, 7, 8, 10], 6, 8))
print(getFloorAndCeil([3, 4, 4, 7, 8, 10], 6, 2))