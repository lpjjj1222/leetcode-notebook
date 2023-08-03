# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root = TreeNode(max(nums))
        root_i = nums.index(max(nums))
        
        root.left = self.constructMaximumBinaryTree(nums[:root_i])
        root.right= self.constructMaximumBinaryTree(nums[root_i+1:])

        return root

