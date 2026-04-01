# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0

        def isGoodNode(root, highest):
            if not root:
                return
            if root.val >= highest:
                self.count += 1
                highest = root.val
            isGoodNode(root.left, highest)
            isGoodNode(root.right, highest)
        isGoodNode(root, root.val)
        return self.count        