# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You can return the answer in any order.
# The best way to solve this solution is use two for loops one from 0th index and another from next to it,
# and check the sum.

def twoSum(nums, target):
        for i in range(len(nums)):  
            for j in range(i+1, len(nums)):  
                if nums[i] + nums[j] == target:
                    return i, j
                
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,2,3], 6))
print(twoSum([3,3], 6))