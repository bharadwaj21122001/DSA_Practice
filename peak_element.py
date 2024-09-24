def peakElement(arr, n):
    # m=arr[0]
    # index=0
    
    # for i in range(n):
    #     if arr[i] > m:
    #         m = arr[i]
    #         index = i
    # return index

    i = 0
    j = n-1
    
    while i<j:
        mid = (i+j)//2
        
        if arr[mid] >= arr[mid+1]:
            j = mid
        else:
            i = mid+1
    return i
        
print(peakElement([1,2,3,4], 4))