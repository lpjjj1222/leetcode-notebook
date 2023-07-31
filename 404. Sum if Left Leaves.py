# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#递归法
'''
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        left_tree_value = self.sumOfLeftLeaves(root.left)
        right_tree_value = self.sumOfLeftLeaves(root.right)
        #如果节点的左孩子存在且这个左孩子没有孩子，则这个节点的左孩子是左叶子
        if root.left and not root.left.left and not root.left.right:
            left_tree_value = root.left.val
        sum_value = left_tree_value + right_tree_value
        return sum_value
'''

#用栈做迭代法
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        result = 0
        while stack:
            node = stack.pop()
            if node.left and not node.left.left and not node.left.right:
                result += node.left.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result

        
            
    
