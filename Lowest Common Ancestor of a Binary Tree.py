# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #这道题感觉看代码随想录的视频会清晰很多
        #这题从下往上走，回溯，用后序，左右中就是天然的回溯

        #遇到p或者q就返回p或者q
        #情况1：遍历到某个节点，左子树和右子树都有返回值
        #情况2:遍历到某个节点，该节点是p或q，该节点的子树有另一个值
        #情况2会直接考虑到，因为遇到p或者q就返回p或者q，就不会继续遍历子树，直接返回这个公共祖先了

        #终止条件：遇到p或者q就返回p或者q，遇到None返回None
        if not root:
            return
        if root == p or root == q:
            return root
        
        #左
        left = self.lowestCommonAncestor(root.left,p,q)
        #右
        right = self.lowestCommonAncestor(root.right,p,q)

        #中
        if left and right:
            return root
        elif right and not left:
            return right
        elif not right and left:
            return left
        else:
            return

