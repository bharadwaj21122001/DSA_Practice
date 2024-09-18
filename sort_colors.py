# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent, 
# with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

def sortColors(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(1, len(nums)-i):
                if nums[j-1] >= nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        return nums