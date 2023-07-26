"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#迭代法 深度遍历
'''
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return self.Traversal(root)
    
    def Traversal(self,root):
        children_level = []
        if not root:
            return 0

        if not root.children:
            children_level.append(0)
        else:
            for child in root.children:
                level = self.Traversal(child)
                children_level.append(level)
        return max(children_level) + 1
'''

#更简洁的迭代法 深度遍历
'''
class Solution:
    def maxDepth(self, root:'Node') -> int:
        if not root:
            return 0
        
        max_depth = 1  #没有孩子的节点就是一层

        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child) + 1)
        return max_depth
'''

#层序遍历 广度遍历
class Solution:
    from collections import deque
    def maxDepth(self, root:'Node') -> int:
        if not root:
            return 0
        
        q = deque([root])
        
        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
            level+= 1
        
        return level
            
            
