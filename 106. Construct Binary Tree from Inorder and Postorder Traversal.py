# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#这个递归最容易理解
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #中（左中右）
        #后（左右中）
        #eg. 中[9，3，15，20，7]    后[9,15,7,20,3]
        #step1: 后序的最后一个肯定是根节点
        #step2：在中序将根节点左右两边分开，分别为左子树和右子树
        #step3:后序的左子树就是从后序左边开始，提取跟中序左子树长度一样的区间 剩下的就是右子树
        #step4: 后序的右子树区间作为后序的新序列，中序的右子树作为中序的新序列
        # 循环：提取后序最后一个节点为根节点，在中序里切。。。

        if not postorder:
            return None
        #step1: 后序的最后一个肯定是根节点
        root = TreeNode(postorder[-1])
        #step2：在中序将根节点左右两边分开，分别为左子树和右子树
        in_root_i = inorder.index(root.val)
        in_root_left = inorder[:in_root_i]
        in_root_right = inorder[in_root_i+1:]
        length_left = len(in_root_left)
        length_right = len(in_root_right)
        
        #step3:后序的左子树就是从后序左边开始，提取跟中序左子树长度一样的区间 剩下的就是右子树
        post_root_left = postorder[:length_left]
        post_root_right = postorder[length_left:-1]

        root.left = self.buildTree(in_root_left, post_root_left)
        root.right = self.buildTree(in_root_right,post_root_right)

        return root
'''

#简洁版 这个比上面的简洁是因为其实根节点在中序的index其实就是左子树的长度了 所以不需要len()来统计
class Solution:
    def buildTree(self, inorder:List[int],postorder:List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        #step1: 后序的最后一个肯定是根节点,将其变成treenode并获取其在中序的位置
        root = TreeNode(postorder[-1])
        in_dex = inorder.index(postorder[-1]) 
        #step2：在中序将根节点左右两边分开，分别为左子树和右子树
        root.left = self.buildTree(inorder[:in_dex], postorder[:in_dex])
        root.right = self.buildTree(inorder[in_dex+1:], postorder[in_dex:-1])
        return root

        
        #step3:后序的左子树就是从后序左边开始，提取跟中序左子树长度一样的区间 剩下的就是右子树


        

        

        
        
