# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#我写的，没有利用二叉搜索树的性质 （递归）
'''
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        
        left = self.searchBST(root.left,val)
        right = self.searchBST(root.right,val)
        return left or right
'''

#我写的，利用了二叉搜索树的性质 （递归）
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return 
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left,val)
        elif root.val < val:
            return self.searchBST(root.right,val)

#代码随想录 （迭代法 本来迭代法深度搜索用栈，广度搜索用队列，但是由于二叉搜索树的有序性，不需要借助栈或队列） 
class Solution:
    def searchBST(self, root: Optional[TreeNode],val:int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None

        

    
