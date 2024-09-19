# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
# This solution can be solved in two ways one is to use two variables, one for tracking the count of the element,
# another to track the element. Another method is to use dictionary .

def majorityElement(nums):
    # count = 0
    # majority = 0

    # for i in range(len(nums)):
    #     if count == 0:
    #         majority = nums[i]
    #     if majority == nums[i]:
    #         count += 1
    #     else:
    #         count -= 1
    # return majority

    counts = {}
    n = len(nums)

    for i in range(len(nums)):
        if nums[i] in counts:
            counts[nums[i]] += 1
        else:
            counts[nums[i]] = 1
    for k,v in counts.items():
        if v > n // 2:
            return k
                

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([6,6,6,7,7]))