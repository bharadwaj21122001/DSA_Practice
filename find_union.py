def findUnion(arr1,arr2,n,m):
    '''
    :param a: given sorted array a
    :param n: size of sorted array a
    :param b: given sorted array b
    :param m: size of sorted array b
    :return:  The union of both arrays as a list
    '''
    # code here 
    # new = set(arr1)
    # for i in range(len(arr2)):
    #     new.add(arr2[i])
    # new_arr = list(new)
    # new_arr.sort()
    # return new_arr

    new_arr = []
    i = 0
    j = 0

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            if not new_arr or new_arr[-1] != arr1[i]:
                new_arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not new_arr or new_arr[-1] != arr2[j]:
                new_arr.append(arr2[j])
            j += 1
        else:
            if not new_arr or new_arr[-1] != arr1[i]:
                new_arr.append(arr1[i])
            i += 1
            j += 1
    
    while i < n:
        if not new_arr or new_arr[-1] != arr1[i]:
            new_arr.append(arr1[i])
        i += 1
    while j < n:
        if not new_arr or new_arr[-1] != arr2[j]:
            new_arr.append(arr2[j])
        j += 1
    return new_arr

n = 5 
arr1 = [1, 2, 3, 4, 5] 
m = 5 
arr2  = [1, 2, 3, 6, 7]

print(findUnion(arr1, arr2, n, m))