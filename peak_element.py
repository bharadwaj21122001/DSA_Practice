def peakElement(arr, n):
    m=arr[0]
    index=0
    
    for i in range(n):
        if arr[i] > m:
            m = arr[i]
            index = i
    return index
        
print(peakElement([1,2,3,4], 4))