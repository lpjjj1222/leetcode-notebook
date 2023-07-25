# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #最后返回的是一个二维数组，每一行是一层
        #队列
        q = deque()
        result = []

        if root:
            q.append(root)
        
        while q:
            level_result = []
            for _ in range(len(q)):
                node = q.popleft()
                level_result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_result)

        return result


        
