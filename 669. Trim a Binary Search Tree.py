# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#我自己写出来，但是看着代码随想录优化的（递归法）
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        #需要遍历一整棵树
        #注意到如果要删除某个节点，该节点不可能有左右子树而左右子树都保留
        #（因为要删除证明已经不在范围内，左右子树要么还要大，要么还要小
        #①如果某个节点因为太大要被删除，那么其右子树也要走，所以直接返回左子树，哦不，左子树要是还是太大..
        #②如果某个节点因为太小要被删除，那么其左子树也要走，所以直接返回右子树,哦不，右子树要是还是太小..
        #叶子结点要被删除的情况已经包含在①和②了，因为如果是叶子结点，直接返回左右子树，就是直接返回None
        if not root:
            return

        if root.val > high:#如果大了
            return self.trimBST(root.left,low,high)
        elif root.val < low:#如果小了
            return self.trimBST(root.right,low,high)
        root.right = self.trimBST(root.right,low,high)
        root.left = self.trimBST(root.left,low,high)
        return root

#迭代法 (代码随想录)
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return
        #处理头结点，让root移动到区间内
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
        
        #因为最后要返回的是root,所以迭代法要把root赋值给cur
        cur = root

        #处理左孩子太小的情况
        while cur:
            while cur.left and cur.left.val < low:
                cur.left = cur.left.right
            cur = cur.left
        #弄两个while循环，外面的那个while cur是用来继续往下走的，里面的While是用来判断左子树符不符合要求

        #遍历完左子树可以回到前面找好的根节点然后去根节点的右节点遍历右子树
        cur = root

        #处理右孩子太大的情况
        while cur:
            while cur.right and cur.right.val > high:
                cur.right = cur.right.left
            cur = cur.right
        
        return root
        
        







            


