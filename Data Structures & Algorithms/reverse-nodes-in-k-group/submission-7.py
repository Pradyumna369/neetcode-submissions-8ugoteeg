# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        head = [3 -> 2 ->1, 4, 5, 6], k = 3
                         ^ ^      ^  ^
                         p f      l  n
        [3, 2, 1, 6, 5, 4]
        len = n
        1 <= k <= n <= 100
        0 <= Node.val <= 100
        '''
        def reverse(node, k, prev) -> [ListNode]:
            if not node:
                return
            f = n = node
            for _ in range(k - 1):
                if n and n.next:
                    n = n.next
                else:
                    return
            n = n.next
            p = None
            for _ in range(k):
                t = f.next
                f.next = p
                p, f = f, t
            node.next = n
            prev.next = p
            reverse(n, k, node)
        dummy = ListNode()
        prev = dummy
        dummy.next = head
        reverse(head, k, prev)
        return dummy.next
        
