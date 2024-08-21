# Done without sorting because we will get an wrong output for inouts like [10,5,10]

def print2ndlargest(arr):
    max_1 = 0
    max_2 = -1

    for i in range(len(arr)):
        if arr[i] > max_1:
            max_2 = max_1
            max_1 = arr[i]
        elif arr[i] > max_2 and max_1 != arr[i]:
            max_2 = arr[i]
    return max_2
print(print2ndlargest([10,5,8,10]))

# def max2(arr):

#     a=0
    
#     s=set(arr)
#     l=list(s)

#     print(f'Type: {type(s)} , {s}, Type: {type(l)}, {l}')

#     for i in l:
#         if i>a:
#             a=i
#     l.remove(a)

#     m2=-1
#     for i in l:
#         if i> m2:
#             m2=i
#     return m2

    # arr=list(set(arr))
    # arr.sort()
    # return arr[-2]

# print(max2([10,5,8,10]))