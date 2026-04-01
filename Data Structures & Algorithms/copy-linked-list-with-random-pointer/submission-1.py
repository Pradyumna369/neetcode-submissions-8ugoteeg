"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        nodes = {}
        first = clone = Node(head.val)
        nodes[head] = clone
        ind = 0
        while head:
            if head.next:
                if head.next not in nodes:
                    nodes[head.next] = Node(head.next.val)
                clone.next = nodes[head.next]
            if head.random:
                if head.random not in nodes:
                    nodes[head.random] = Node(head.random.val)
                clone.random = nodes[head.random]
            head = head.next
            clone = clone.next
        return first
            

            
            