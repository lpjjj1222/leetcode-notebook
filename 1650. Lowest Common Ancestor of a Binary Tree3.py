"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        #用Example 1找6和7公共祖先为例子想
        #从p出发到lowest公共祖先（a）再到根节点(b)后再从q出发到lowest公共祖先(c)再到根节点(b)   -1
        #从q出发到lowest公共祖先（c）再到根节点(b)后再从p出发到lowest公共祖先(a)再到根节点(b)   -2
        #-1: a+b+c+b
        #-2: c+b+a+b
        #由于 a+b+c = c+b+a，这一段路程一样且两边速度相同，所以此时相遇。即会在lowest公共祖先相遇
        p_origin, q_origin = p , q
        while p != q:
            p, q = p.parent, q.parent
            if p == None:
                p = q_origin
            if q == None:
                q = p_origin
        return p
            


