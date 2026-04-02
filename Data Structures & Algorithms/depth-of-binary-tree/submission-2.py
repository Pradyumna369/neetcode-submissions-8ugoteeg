# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node) -> int:
            left = right = 0
            if node.left:
                left = depth(node.left)
            if node.right:
                right = depth(node.right)
            return max(left, right) + 1
        if not root:
            return 0
        return depth(root)