def get_min_max(arr):
    # min_ele = arr[0]
    # max_ele = arr[len(arr)-1]
    # for i in range(len(arr)):
    #     if arr[i] < min_ele:
    #         min_ele = arr[i]
    #     if arr[i] > max_ele:
    #         max_ele = arr[i]
    # return min_ele, max_ele
    min_ele = min(arr)
    max_ele = max(arr)
    return min_ele, max_ele

print(get_min_max([3,2,1,5,1000,6,7]))
print(get_min_max([34353,64545,234,67544]))