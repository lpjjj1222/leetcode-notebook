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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return

        q = deque([root])

        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()

                #定义next指针 最右边的指针即for循环最后一个指针指向None
                if _ == size - 1:
                    node.next = None
                else:
                    node.next = q[0]

                #把孩子搞进队列
                if node.right:
                    q.append(node.left)
                    q.append(node.right)
                
        return root
            
                
                


        
