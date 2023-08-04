# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#我自己写的 递归+创造新树
'''
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            root = None
            return

        if not root1:
            root = TreeNode(root2.val)
            root.left = self.mergeTrees(None, root2.left)
            root.right = self.mergeTrees(None,root2.right)
        elif not root2:
            root = TreeNode(root1.val)
            root.left = self.mergeTrees(root1.left,None)
            root.right = self.mergeTrees(root1.right,None)
        else:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right,root2.right)
        return root
'''
#代码随想录的递归+创造新树
'''
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #其中一个None，直接返回另一个，如果两个都是None,就返回None
        #注意，这里返回另一个，其实也会把这一个下面的子树返回！
        #确实如此，比如某个
        #而且return了 就不用看后面的操作
        if not root1:
            return root2
        if not root2:
            return root1
        #有了上面，下面的roo1 和 root2 都是非None的

        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left,root2.left)
        root.right = self.mergeTrees(root1.right,root2.right)

        return root
'''

#代码随想录 递归+更新root
class Solution:
    def mergeTrees(self,root1:Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #更新root1 instead of create a new root 节省空间和时间
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1
        

        
