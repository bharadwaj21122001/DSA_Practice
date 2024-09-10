def missingNumber(nums):
    nums.sort()
    n = len(nums)
    
    # if n == 0:
    #     return 1
    
    # if nums[0] > 1:
    #     return 1

    # if nums[0] == 1:
    #     return 0
    
    # for i in range(1, n):
    #     if nums[i] > 0 and nums[i] != nums[i-1] and nums[i] != nums[i-1] + 1:
    #         return nums[i-1] + 1
    
    # return nums[-1] + 
    
    # for i in range(n):
    #     if nums[i] != i:
    #         return i
    # return n

    total = n * (n + 1) // 2
    actual = sum(nums)
    return total - actual

print(missingNumber([3,0,1]))
print(missingNumber([0,1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))