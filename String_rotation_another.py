# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.

def rotateString(s, goal):
    if len(s) != len(goal):
            return False
    # return goal in (s+s)
    for i in range(len(s)):
        s = s[1:] + s[0]
        if goal == s:
            return True
    return False
        

print(rotateString('abcde', 'cdeab'))
print(rotateString("abcde", "abced"))