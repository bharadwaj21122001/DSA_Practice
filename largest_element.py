def largest(arr):
        # code here
        # max_ele = arr[0]
        # for i in range(len(arr)):
        #     if arr[i] > max_ele:
        #         max_ele = arr[i]
        arr.sort()
        i = 0
        j = len(arr)-1
        while i < j:
            mid = (i+j)//2
            if arr[mid] > arr[mid+1]:
                j = mid
            else:
                i = mid + 1
        return arr[i]
print(largest([1,8,7,56,90]))