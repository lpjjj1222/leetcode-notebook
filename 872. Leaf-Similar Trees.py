# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#用yield 和 yield from
'''
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findLeaf(root):
            if not root:
                return
            if not root.left and not root.right:
                yield root.val
            
            yield from findLeaf(root.left)
            yield from findLeaf(root.right)
        return list(findLeaf(root1)) == list(findLeaf(root2))
'''

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return []
            elif not root.left and not root.right:
                return [root.val]
            left = dfs(root.left)
            right = dfs(root.right)
            return left + right
        return dfs(root1) == dfs(root2)
    


        
