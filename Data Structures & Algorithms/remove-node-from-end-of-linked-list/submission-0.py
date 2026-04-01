# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 1
        curr = head
        while curr.next:
            curr = curr.next
            l += 1
        
        index = l - n
        curr = head
        dummy = prev = ListNode(0)
        prev.next = curr
        for i in range(index):
            prev = curr
            curr = curr.next
        if curr.next:
            prev.next = curr.next
        else:
            prev.next = None
        
        return dummy.next