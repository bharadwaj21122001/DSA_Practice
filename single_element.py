# You are given a sorted array consisting of only integers where every element appears exactly twice, 
# except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.

def singleNonDuplicate(nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return nums[low]

print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
print(singleNonDuplicate([3,3,7,7,10,11,11]))