# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ans = ListNode()
        while l1 or l2 or carry:
            total = 0
            total += carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            lastDigit = total % 10
            ans.next = ListNode(lastDigit)
            ans = ans.next
            carry = total // 10
        return dummy.next
            

