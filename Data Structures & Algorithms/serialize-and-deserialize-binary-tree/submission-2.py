# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.string = ""
        def node(root):
            if root is None:
                self.string += ".#"
                return
            self.string += str(root.val) + "#"
            node(root.left)
            node(root.right)
        node(root)
        return self.string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # self.data = data
        # self.l = len(self.data)
        # def createNode(ind):
        #     string = ""
        #     while ind < self.l and self.data[ind] != "#":
        #         string += self.data[ind]
        #         ind += 1
        #     if string == "." or string == "":
        #         return None, ind
        #     val = int(string)
        #     if ind < self.l:
        #         ind += 1
        #     left, ind = createNode(ind) # Need to return ind because ind needs to be 
            # the ind after the whole left subtree which updates the required ind for right
        #     while ind < self.l and self.data[ind] != "#":
        #         ind += 1
        #     right, ind = createNode(ind + 1)
        #     node = TreeNode(val, left, right)
        #     return node, ind
        # root,_= createNode(0)
        # return root
        vals = data.split("#")
        self.i = 0

        def dfs():
            if vals[self.i] == ".":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()



