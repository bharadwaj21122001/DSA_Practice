# Check function iterates through each element of the array and check if the ith element is greater than the i+1th element,
# if it greater than the count will increase and %n is done for check the 0th element and last element of the array, for the purpose of rotation
# The time complexity is O(n).

def check(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i] > nums[(i+1)%n]:
            count += 1
        if count > 1:
            return False
    return True
print(check([3,4,5,1,2]))
print(check([2,1,3,4]))
print(check([1,1,1]))   