# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        carry = 0
        dummy = ans = ListNode()
        while first or second:
            total = 0
            total += carry
            if first:
                total += first.val
                first = first.next
            if second:
                total += second.val
                second = second.next
            lastDigit = total % 10
            ans.next = ListNode(lastDigit)
            ans = ans.next
            carry = total // 10
        if carry > 0:
            ans.next = ListNode(1)
        return dummy.next
            

