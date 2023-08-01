# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        #如果碰到叶子结点，判断是否减到0
        if not root.right and not root.left:
            targetSum -= root.val
            if targetSum == 0:
                return True
            else:
                return False
            
        right = self.hasPathSum(root.right, targetSum-root.val)
        left = self.hasPathSum(root.left, targetSum - root.val)
        return right or left
