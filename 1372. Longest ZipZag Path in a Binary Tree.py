# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        def dfs(node,cur_dirc,count):
            nonlocal res
            if node:
                if node.right:
                    if cur_dirc == -1:
                        dfs(node.right, 1, count+1)
                    else:
                        dfs(node.right, 1, 1)
                        res = max(res, count)
                        
                if node.left:
                    if cur_dirc == 1:
                        dfs(node.left, -1, count+1)
                    else:
                        dfs(node.left, -1, 1)
                        res = max(res, count)
                if not node.left and not node.right:
                    res = max(res, count)
        res = 0
        dfs(root.left, -1, 1)
        dfs(root.right, 1, 1)
        return res
            

        
