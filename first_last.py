# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
# This problem can be solved by performing binary search to fing leftmost and after again we need to perform 
# binary search to fing rightmost.

def searchRange(nums, target):
        def binarySearch(nums, left):
            low = 0
            high = len(nums) - 1
            result = -1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    result = mid
                    if left:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return result

        first = binarySearch(nums, True)

        if first == -1:
            return [-1,-1]

        last = binarySearch(nums, False)
        
        return [first, last]

print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 6))
print(searchRange([], 0))