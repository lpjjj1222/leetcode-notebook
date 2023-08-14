# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #看代码随想录文字解释
        #关键点1:BST是有序树（左中右，中序时），所以如果一个节点左右子树分别有一个p一个q，那么一定满足p<root<q or q<root<p
        #关键点2:从上至下遍历时，遇到的第一个满足关键点1的节点，就是最近公共祖先，再往下找，就不是公共祖先了（可以随便画画） ****

        if not root:
            return 
        if (p.val <root.val and q.val>root.val) or (p.val>root.val and q.val<root.val):
            return root
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        return left or right


'''
#因为利用二叉搜索树的性质按照大小指示往左下还是右下走 不需要走到叶子结点之后再走回头路，所以不需要考虑root为None 的情况
#代码随想录精简版
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:#p<root<q 或者 q<root<p 或者 root is None
            return root
'''


#因为利用二叉搜索树的性质按照大小指示往左下还是右下走 不需要走到叶子结点之后再走回头路，所以不需要考虑root为None 的情况
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root
        return None
        



