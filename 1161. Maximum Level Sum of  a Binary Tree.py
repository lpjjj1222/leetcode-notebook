# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        maxSum = -float('inf')
        res = 0
        q.append(root)
        level = 0
        while q:
            level_size = len(q)
            level_sum = 0
            level += 1
            for _ in range(level_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level_sum += node.val
            if level_sum > maxSum:
                maxSum = level_sum
                res = level
        return res

            
            
