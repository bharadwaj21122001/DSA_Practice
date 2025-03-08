class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def __init__(self):
        self.head = None
    def searchKey(self, n, head, key):
        #Code here
        temp = head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False