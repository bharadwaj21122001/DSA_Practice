# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# The bet idea to solve this solution is to use XOR operation. 

def singleNumber(nums):
        x = 0

        for i in range(len(nums)):
            x = x ^ nums[i]
        return x

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))