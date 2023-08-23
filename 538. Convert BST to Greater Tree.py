# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#递归法
#注意pre放在哪里
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #中序：左中右 从小到大
        #把中序反过来，就是递增（右中左）
        self.pre = 0
        self.Traversal(root)
        return root
    def Traversal(self, cur):
        if not cur:
            return
        #右 
        cur.right = self.Traversal(cur.right)
        #中
        cur.val += self.pre
        #如果没有pre，cur值不变
        self.pre = cur.val
        #左
        cur.left = self.Traversal(cur.left)
        return cur
#迭代法
#注意pre放在哪里
#用stack
class Solution:
    def __init__(self):
        self.pre = 0
    def Traversal(self, root):
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur.val += self.pre
                self.pre = cur.val
                cur = cur.left
    
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.Traversal(root)
        return root
        



        
        

            
        
        

