# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(root):
            if not root:
                return
                
            invert(root.left)
            invert(root.right)
            root.left, root.right = root.right, root.left

        invert(root)
        return root
'''


#更简洁的写法：
'''
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
'''

#用stack的迭代法
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        stack = [(root,False)]

        while stack:
                node, visited = stack.pop()
                if node:
                    if visited:
                        node.right, node.left = node.left, node.right
                    else:
                        stack.append((node.right, False))
                        stack.append((node.left, False))
                        stack.append((node,True))
        return root

        




        


            

