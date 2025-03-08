class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    #Function to insert a node at the end of the linked list.
    def __init__(self):
        self.head = None
    def insertAtEnd(self,head,x):
        # code here 
        new_node = Node(x)
        if head is None:
            head = new_node
            return head
        else:
            temp = head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
        return head