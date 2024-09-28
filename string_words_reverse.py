# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.

def reverseWords(s):
        splited = s.split()
        new = splited[::-1]
        res = ""
        
        for i in range(len(new)):
            if new[i] == new[-1]:
                res += new[i]
            else:
                res += new[i]
                res += ' '
        return res

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))