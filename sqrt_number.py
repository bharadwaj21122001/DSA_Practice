# Given an integer n, find the square root of n. If n is not a perfect square, then return the floor value.
# Floor value of any number is the greatest Integer which is less than or equal to that number

def floorSqrt(n): 
    #Your code here
        i = 1
        ans = 0
        while i <= n:
            if (i * i) == n:
                return i
            elif (i * i) < n:
                ans = i
                i += 1
            else:
                return ans
            
print(floorSqrt(5))
print(floorSqrt(4))