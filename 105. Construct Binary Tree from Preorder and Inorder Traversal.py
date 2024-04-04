# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #preorder第一个 找到根节点
        #inorder找到根节点所在的index, 左边的是左子树，右边的是右子树
        #把preorder也分成左子树的前序和右子树的前序
        #递归构造

        if not preorder:
            return None
        else:
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0]) #根节点所在index

            root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
            root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root
