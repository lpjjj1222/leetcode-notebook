# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#层序遍历（广度遍历）
'''
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
'''

#深度遍历 核心：求最大深度其实就是根节点的高度
#对任一个node，求出左右两子树的高度 取两者最大值后+1 就能知道这个node目前的最大高度
#递归到最上面那个node即可

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.Traversal(root)

    def Traversal(self,root):
        #如果任一node不存在，则高度就是0 因为Null下面没东西的
        if not root:
            return 0
        leftdepth = self.Traversal(root.left)
        rightdepth = self.Traversal(root.right)

        nodedepth = max(leftdepth,rightdepth) + 1
        return nodedepth
    





        
