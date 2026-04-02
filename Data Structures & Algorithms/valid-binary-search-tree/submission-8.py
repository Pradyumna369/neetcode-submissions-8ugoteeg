# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(node, left, right) -> bool:
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return validBST(node.left, left, node.val) and validBST(node.right, node.val, right)
            
        return validBST(root, -1001, 1001)