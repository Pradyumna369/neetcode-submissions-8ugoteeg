# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        1 <= k <= no.of nodes <= 1000
        0 <= Node.val <= 1000

            5
           / \
          3   6
         / 
        2
        count = 1
        k=4
        '''
        kth = root.val
        smaller = [] 
        def dfs(node) -> int:
            if len(smaller) >= k:
                return
            if node.left:
                dfs(node.left)
            smaller.append(node.val)
            if node.right:
                dfs(node.right)

        dfs(root)
        return smaller[k - 1]
