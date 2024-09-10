def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[k]
            nums[k] = nums[i]
            nums[i] = temp
            k += 1 
    return nums
print(moveZeroes([0,1,0,3,12]))