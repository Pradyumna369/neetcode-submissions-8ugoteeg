# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        # while fast and slow:
        #     if fast.next and fast.next.next and slow.next:
        #         fast = fast.next.next
        #         slow = slow.next
        #     else:
        #         return False
        #     if fast == slow:
        #         return True
        # return False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False