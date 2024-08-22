def removeDuplicates(nums):
    # new_nums = []
    # for i in range(len(nums)):
    #     if nums[i] not in new_nums:
    #         new_nums.append(nums[i])
    # print(new_nums)
    # k = len(new_nums)
    # return k
    n=len(nums)
    i=1
    while i<n:
        if nums[i] == nums[i-1]:
            nums.pop(i)
        else:
            i+=1
    return len(nums)
# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


def dup(nums):
    k=1
    for i in range(1,len(nums)):
        if nums[i-1] != nums[i]:
            nums[k] = nums[i]
            k+=1
    return k

nums=[0,0,1,1,1,2,2,3,3,4]
# duplicate=dupli(nums)
# print(f'Final: {duplicate}')

def dupli(nums):
    d={}

    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]]+=1
        else:
            d[nums[i]] =1
    
    du=[]
    for k,v in d.items():
        if v>=1:
            du.append(k)
    
    return len(du)

nums=[1,1,2]
duplicate=dupli(nums)
print(f'Final: {duplicate}')