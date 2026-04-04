"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, newNodes = None):
        self.val = val
        self.newNode = newNode if newNode is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = defaultdict()
        if not node:
            return None
        first = Node(node.val)
        nodes[first.val] = first
        newNodes = deque([node])
        completed = set()
        while newNodes:
            for _ in range(len(newNodes)):
                node = newNodes.popleft()
                if node in completed:
                    continue
                completed.add(node)
                if node.val not in nodes:
                    nodes[node.val] = Node(node.val)
                for neighbor in node.neighbors:
                    if neighbor.val not in nodes:
                        nodes[neighbor.val] = Node(neighbor.val)
                        newNodes.append(neighbor)
                    nodes[node.val].neighbors.append(nodes[neighbor.val])
        return first


