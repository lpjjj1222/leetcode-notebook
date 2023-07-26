# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #题目要求小于O（N），那就不能有多少个node遍历多少次了
        #这题看代码随想录的利用完全二叉树的性质的解法
        #满二叉树的定义：一个完全二叉树，如果底层全满，则为满二叉树
        #一个完全二叉树，如果是满二叉树，那么一直顺着左孩子遍历的深度=一直顺着右孩子遍历的深度
        #一个完全二叉树，总是能递归到某个节点，其子树是一个满二叉树（递归到最底层的话，则最底层的叶子自己就是一棵满二叉树）

        if not root:
            return 0
        
        left_depth = 0
        right_depth = 0
        right_node = root.right
        left_node = root.left
        while right_node:
            right_node = right_node.right
            right_depth += 1
        while left_node:
            left_node = left_node.left
            left_depth += 1
        
        if left_depth == right_depth: #满二叉树
            node_num = 2**(right_depth+1) -1
        else: #非满二叉树
            node_num = self.countNodes(root.right) + self.countNodes(root.left) +1
        return node_num


    

        
        


      

