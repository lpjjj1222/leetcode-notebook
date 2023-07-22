# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0

        if not root:
            return 0
        
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            level += 1
        
        return level
            
        
