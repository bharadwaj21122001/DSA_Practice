class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        return count