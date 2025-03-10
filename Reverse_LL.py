class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_linkedlist(self, head):
        if not head or not head.next:
            return head
        
        new_head = self.reverse_linkedlist(head.next)

        head.next.next = head
        head.next = None

        return new_head