# Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.

def count(arr, n, x):
    # code here
    # count = arr.count(x)
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    return count

print(count([1, 1, 2, 2, 2, 2, 3], 7, 2))
print(count([1, 1, 2, 2, 2, 2, 3], 7, 4))