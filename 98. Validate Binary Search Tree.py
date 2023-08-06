# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#所有的总体思路都是：中序遍历下，整个二叉搜索树就变成了递增的

#最简单的，创造数组记录，然后判断数组是否递增（递归法）
'''
class Solution:
    def traversal(self,root):
        if not root:
            return
        left = self.traversal(root.left)
        self.seq.append(root.val)
        right = self.traversal(root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.seq=[]
        self.traversal(root)
        for i in range(1,len(self.seq)):
            if self.seq[i] <= self.seq[i-1]:
                return False
        return True
'''

#记录目前遍历到的最大值，一边遍历，一边看是否递增 （递归法）
'''
class Solution:
    def __init__(self):
        self.maxval = float("-inf")

    def isValidBST(self, root:Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.isValidBST(root.left)
        
        if root.val > self.maxval:
            self.maxval = root.val
        else:
            return False
        
        right = self.isValidBST(root.right)

        return left and right
'''

#迭代法
class Solution:
    def isValidBST(self, root:Optional[TreeNode]) -> bool:
        stack = []
        cur = root
        pre = None

        while cur is not None or len(stack) >0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif not cur:
                cur = stack.pop()
                if pre is not None and pre.val >= cur.val:
                    return False
                pre = cur
                cur = cur.right
        return True
                





        
    
        
 
