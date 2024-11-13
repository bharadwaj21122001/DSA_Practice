# You are given 2 numbers (n , m); the task is to find n√m (nth root of m).

def NthRoot(n, m):
    # Code here
    root = m ** (1/n)
    rounded_root = round(root)
    if rounded_root ** n == m:
        return rounded_root
    else:
        return -1
    
print(NthRoot(2,9))
print(NthRoot(3,9))
