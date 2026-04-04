"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, newNodes = None):
        self.val = val
        self.newNode = newNode if newNode is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = defaultdict()
        newNodes = deque([node])
        nodes[node] = Node(node.val)
        first = node
        while newNodes:
            node = newNodes.popleft()
            for neighbor in node.neighbors:
                if neighbor not in nodes:
                    nodes[neighbor] = Node(neighbor.val)
                    newNodes.append(neighbor)
                nodes[node].neighbors.append(nodes[neighbor])
        return nodes[first]