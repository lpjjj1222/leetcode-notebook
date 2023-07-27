# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#求深度：从上往下，所以用中左右（前序）
#求高度：从下往上，所以用左右中（后序）
#前深后高


#深度是从上往下，从根节点到某一节点
#高度是从下往上，从叶子节点到某一节点

#平衡二叉树的定义是关于子树的高度，所以该题需用求高度的后序

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if self.getdepth(root) == -1:
            return False
        else:
            return True
        

    def getdepth(self,root):
    #返回值是以传入节点为根节点的树 的高度
        if not root:
            return 0
        
        #如果左右子树高度差<=1，则返回目前高度 （目前高度是较高的树高度+1）
        right_height = self.getdepth(root.right)
        left_height = self.getdepth(root.left)
        #print(right_height,left_height,root)

        #判断以左右孩子为根节点的子树是否是平衡二叉树，如果已经不是平衡二叉树了，
        #就继续向上面反馈-1，表示不可能构成平衡二叉树了
        if left_height==-1:
            return -1
        elif right_height==-1:
            return -1

        if abs(right_height-left_height)>1:
            return -1 #-1是在告诉上面的节点，下面的子树已经不是平衡二叉树了
        height = max(right_height,left_height) + 1
        return height

    


