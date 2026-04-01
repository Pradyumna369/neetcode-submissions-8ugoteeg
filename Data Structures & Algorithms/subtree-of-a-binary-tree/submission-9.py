# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        def isSameTree(root, subRoot) -> bool:
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                left = isSameTree(root.left, subRoot.left)
                right = isSameTree(root.right, subRoot.right)
                if left and right:
                    return True
            return False

        if root and subRoot:
            if root.val == subRoot.val:
                if isSameTree(root, subRoot):
                    return True
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            if left or right:
                return True
        return False

        


    