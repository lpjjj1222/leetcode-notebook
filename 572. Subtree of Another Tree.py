# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#我太屌了，跟着代码随想录写完100，101后自己做出来这个！
class Solution:
    from collections import deque
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
           
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                if node.val != subRoot.val:
                    q.append(node.left)
                    q.append(node.right)
                else:
                    if self.compare(node,subRoot) == False:
                        q.append(node.left)
                        q.append(node.right)
                        continue
                    else:
                        return True
        return False

    def compare(self, root,subRoot):
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        elif root and not subRoot:
            return False
        else:
            if root.val != subRoot.val:
                return False
            else:
                left=self.compare(root.left,subRoot.left)
                right=self.compare(root.right,subRoot.right)
                return left and right
