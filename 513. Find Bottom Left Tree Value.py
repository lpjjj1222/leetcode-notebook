# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#递归法
'''
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        #注意这个初始化流程是为了防止出现‘reference before assignment‘之类的报错
        self.result = None
        self.max_depth = float('-inf')
        self.Traversal(root,0)
        return self.result

    def Traversal(self, root,depth):
        #如果遍历到的节点是叶子结点：
        if not root.left and not root.right:
            #对比当前叶子深度是否比遍历过的最大深度深
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = root.val
                return
        #如果不是叶子结点，就继续左右向下遍历
        if root.left:
            self.Traversal(root.left,depth+1)
        if root.right:
            self.Traversal(root.right,depth+1)
'''

#层序遍历
class Solution:
    from collections import deque
    def findBottomLeftValue(self,root: Optional[TreeNode]) -> int:
        self.result = None
        if not root:
            return self.result
        
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if _ == 0:
                    self.result = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return self.result
        

