"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    from collections import deque
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []

        if not root:
            return result

        q = deque([root])

        while q:
            level_result = []
            for _ in range(len(q)):
                node = q.popleft()
                level_result.append(node.val)
                for child in node.children:
                    q.append(child)
            result.append(level_result)

        return result

        

        
