# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# This problem can be solved in two ways one by using binary search and another linear search. 
# Binary search has O(log n) time complexity, which linear search has O(n).

def search(nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1

print(search([-1,0,3,5,9,12], 9))
print(search([-1,0,3,5,9,12], 2))