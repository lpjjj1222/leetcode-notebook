# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#中序遍历搜索二叉树，放进数组，然后遍历数组（递归法）
'''
class Solution:
    def __init__(self):
        self.seq = []

    def Traversal(self, root):
        if not root:
            return 
        left = self.Traversal(root.left)
        self.seq.append(root.val)
        right = self. Traversal(root.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        mindiff = float('inf')
        self.Traversal(root)
        for i in range(1,len(self.seq)):
            diff = abs(self.seq[i] - self.seq[i-1])
            if diff < mindiff:
                mindiff = diff
        return mindiff
'''

#中序遍历搜索二叉树，一边递归一边找最小差值（递归法）
'''
class Solution:
    def __init__(self):
        self.result = float('inf')
        self.pre = None

    def Traversal(self,cur):
        if not cur:
            return
        self.Traversal(cur.left)
        if self.pre is not None:
            diff = cur.val - self.pre.val
            self.result = min(diff,self.result) 
        self.pre = cur
        self.Traversal(cur.right)

    def getMinimumDifference(self,root: Optional[TreeNode]) -> int:
        self.Traversal(root)
        return self.result
'''

#迭代法
class Solution:
    def getMinimumDifference(self,root: Optional[TreeNode]) -> int:
        stack = []
        cur = root
        pre = None
        result = float('inf')

        while len(stack) > 0 or cur is not None:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre is not None:
                    result = min(cur.val - pre.val,result)
                pre = cur
                cur = cur.right
        return result
            

        
