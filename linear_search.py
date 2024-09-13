def searchInSorted(arr, K):
        #Your code here
        # for i in range(N):
        #     if arr[i] == K:
        #         return 1
        # return -1
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == K:
                return 1
            elif arr[mid] < K:
                left = mid + 1
            elif arr[mid] > K:
                right = mid - 1
        return -1

print(searchInSorted([1,2,3,4,6], 6))
print(searchInSorted([1,3,4,5,6], 2))