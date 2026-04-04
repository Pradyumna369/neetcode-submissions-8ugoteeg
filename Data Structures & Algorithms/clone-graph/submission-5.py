"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, newNodes = None):
        self.val = val
        self.newNode = newNode if newNode is not None else []
"""

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        clones = {}
        queue = deque([node])
        clones[node] = Node(node.val)
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clones[curr].neighbors.append(clones[neighbor])
        return clones[node]

