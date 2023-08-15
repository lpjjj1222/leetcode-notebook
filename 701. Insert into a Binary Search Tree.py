# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#这题看代码随想录的视频最清晰，下面这段是看完解题思路之后自己写出来的
'''
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val > root.val:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        if val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left,val)
        return root
'''

#迭代法 
#(这里引入cur是为了最后return根节点的时候可以直接return root）
#（引入parent是因为可以记录叶子节点，在跳出循环后找到父节点)
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode],val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        parent = None
        cur = root

        while cur:
            parent = cur
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                cur = cur.right
        #跳出while循环，即到空节点的时候 可以插入了。 跳出循环前的parent记录的就是叶子结点
        if val > parent.val:
            parent.right = TreeNode(val)
        if val < parent.val:
            parent.left = TreeNode(val)
        return root
        

        


        
        
        
        
        
