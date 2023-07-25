"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    from collections import deque
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 

        q = deque([root])
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                #如果是某层最右边的node
                if _ == size-1:
                    node.next = None
                else:
                    node.next = q[0]
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
