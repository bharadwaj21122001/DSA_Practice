def reverseWord(s):
    #your code here
    # new_str = s[::-1]
    # return new_str
    new_str = ""
    for i in range(len(s)-1,-1,-1):
        new_str += s[i]
    return new_str

print(reverseWord("Geeks"))