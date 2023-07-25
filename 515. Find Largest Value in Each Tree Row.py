# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result

        q = deque([root])

        while q:
            level_node = []
            for _ in range(len(q)):
                node = q.popleft()
                level_node.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            result.append(max(level_node))
            
        return result
