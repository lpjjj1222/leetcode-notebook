# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#看代码随想录的思路自己写的复杂代码，请不要看
'''
class Solution:
    def __init__(self):
        self.parent = None

    def Traversal(self, root, key):
        if not root:
            return 
        if root.val == key:
            if root.left and not root.right:
                root = root.left
            elif root.right and not root.left:
                root = root.right
            elif not root.right and not root.left:
                root = None
            else:
                left = root.left
                right = root.right
                #把右子树先接上
                root = right
                #然后把左子树接到接好的右子树左下角
                #cur是用来探究从哪里插入的，应该从接好的右子树的左下角接入
                cur = right.left
                if not cur:
                    right.left = left
                else:
                    while cur.left:
                        cur = cur.left
                    cur.left = left
            return (1,root)
            

        if root.right and root.right.val == key:
            self.parent = root
        elif root.left and root.left.val == key:
            self.parent = root
        else:
            self.Traversal(root.left,key)
            self.Traversal(root.right,key)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #①：找不到要删除的节点
        #②：发现要删除的是叶子节点 ->直接删
        #③：要删除的节点左子节点非空，右子节点空
        #④：要删除的节点右子节点非空，左子节点空
        #⑤：要删除的节点左右子节点都非空

        traversal = self.Traversal(root,key) #找到符合要求的parent
        if traversal:
            return traversal[1]
        if not self.parent:
            return root

        if self.parent.right and self.parent.right.val == key:
            kid = self.parent.right
            if not kid.right and not kid.left:#②
                self.parent.right = None
            elif kid.right and not kid.left:#④
                self.parent.right = kid.right
            elif kid.left and not kid.right:#③
                self.parent.right = kid.left
            else:
                #把右子树先接上
                self.parent.right = kid.right
                #然后把左子树接到接好的右子树左下角
                #cur是用来探究从哪里插入的，应该从接好的右子树的左下角接入
                cur = self.parent.right.left
                if not cur:
                    self.parent.right.left = kid.left
                else:
                    while cur.left:
                        cur = cur.left
                    cur.left = kid.left

        
        elif self.parent.left and self.parent.left.val == key:
            kid = self.parent.left
            if not kid.right and not kid.left:#②
                self.parent.left = None
            elif kid.right and not kid.left:#④
                self.parent.left = kid.right
            elif kid.left and not kid.right:#③
                self.parent.left = kid.left
            else:
                #把右子树先接上
                self.parent.left = kid.right
                #然后把左子树接到接好的右子树左下角
                #cur是用来探究从哪里插入的，应该从接好的右子树的左下角接入
                cur = self.parent.left.left
                if not cur:
                    self.parent.left.left = kid.left
                else:
                    while cur.left:
                        cur = cur.left
                    cur.left = kid.left
        
        return root
'''

#代码随想录的迭代法
'''
class Solution:
    def deleteNode(self, root:Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #遍历整棵树，找到目标节点
        if not root:
            return root
        cur = root
        pre = None
        while cur:
            if cur.val == key:
                break
            pre = cur
            if key > cur.val:
                cur = cur.right
            elif key < cur.val:
                cur = cur.left
        #以上找到了目标节点，如果cur==None,那就是没找到
        #如果pre==None说明根节点值等于val，一进while循环就break
        if not cur:
            return root
        if not pre:
            return self.deleteoneNode(cur) #因为知道删除的是根节点，所以答案最后返回根节点就行了

        if pre.left and pre.left.val == key: #要知道pre的左节点还是右节点是目标节点
            pre.left = self.deleteoneNode(cur)
        elif pre.right and pre.right.val == key:
            pre.right = self.deleteoneNode(cur)
        return root
    
    def deleteoneNode(self, target):
        #删除目标节点，将目标节点左子树接到右子树的左下角
        if not target:
            return target
        if not target.right:
            return target.left
        else:
            bottom_left = target.right
            while bottom_left.left:
                bottom_left = bottom_left.left
            bottom_left.left = target.left
            return target.right
'''

#代码随想录的递归法1（容易理解的递归）
class Solution:
    def deleteNode(self, root:Optional[TreeNode],key:int) ->Optional[TreeNode]:
        if not root:
            return 
        if root.val == key:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
                
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        return root
            

        


    





            
