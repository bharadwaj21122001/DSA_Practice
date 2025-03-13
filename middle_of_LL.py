class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # single = head
        # double = head

        # while double is not None and double.next is not None:
        #     single = single.next
        #     double = double.next.next
        # return single
        node = []
        while head:
            node.append(head)
            head = head.next
        return node[len(node) // 2]