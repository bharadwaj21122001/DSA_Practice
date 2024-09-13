def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        # b = (len(nums) - k) % len(nums)
        # nums[:] = nums[b:] + nums[:b]
        # return nums

        n = len(nums)
        b = k % n

        temp = nums[-b:] + nums[:-b]

        for i in range(n):
            nums[i] = temp[i]
        return nums


print(rotate([1,2,3,4,5,6,7], 3))
print(rotate([-1,-100,3,99], 2))