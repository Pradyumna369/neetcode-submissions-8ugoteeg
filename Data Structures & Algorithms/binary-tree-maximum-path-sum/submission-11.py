# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.longest = root.val

        # # Return max path till that node
        # def path(root):
        #     if not root:
        #         return -1001
        #     left = path(root.left)
        #     right = path(root.right)
        #     total = root.val
        #     if left > 0:
        #         total += left
        #     if right > 0:
        #         total += right 
        #     self.longest = max(self.longest, total, left, right)
        #     return max(root.val + left, root.val + right, root.val)
        # path(root)
        # return self.longest

        def path(root):
            if not root:
                return 0
            
            left = path(root.left)
            right = path(root.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)

            self.longest = max(self.longest, root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        path(root)
        return self.longest







