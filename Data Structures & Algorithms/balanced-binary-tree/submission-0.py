# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Return max height
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if left is False or right is False:
                return False
            else:
                if abs(left - right) > 1:
                    return False
                else:
                    return 1 + max(left, right)
        ans = dfs(root)
        if ans is False:
            return False
        else:
            return True

        