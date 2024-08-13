def kthSmallest(arr, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()
        ele = arr[k-1]
        return ele
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kthSmallest(arr, k))