# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#对某个节点来说，如果pq一个在左一个在右，则返回该节点
#如果pq都在左边，则返回左子节点
#如果pq都在右边，则返回右子节点
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if not root:
                return False

            if root ==q or root==p:
                return root
            else:
                left = self.lowestCommonAncestor(root.left,p,q)
                right = self.lowestCommonAncestor(root.right,p,q)
            if left and right:
                return root
            elif left and not right:
                return left
            elif right and not left:
                return right

