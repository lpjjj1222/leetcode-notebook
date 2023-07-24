# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#递归法，左子树-左右中，右子树-右左中
'''
#注意只有都存在且值相等的情况需要继续往下递归
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        else:
            right_tree = root.right
            left_tree = root.left
            return self.judging(right_tree, left_tree)

    def judging(self, right_node,left_node):
        #左右节点有一个为空，另一个不为空 不对称
        if not right_node and left_node: return False
        elif not left_node and right_node: return False
        #左右两个节点都为空 对称
        elif not left_node and not right_node: return True
        #左右两个节点都存在，比较数值是否相等,这有这种情况，才需要往下做递归
        elif left_node and right_node:
            if left_node.val != right_node.val:
                return False
            else:
                outside = self.judging(right_node.right,left_node.left)
                inside = self.judging(right_node.left, left_node.right)
                return outside and inside
'''

#使用队列的迭代法
#成对成对的拿进去取出来
class Solution:
    from collections import deque
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root.right, root.left])
        while q:
            right_node = q.popleft()
            left_node = q.popleft()
            #左右节点有一个为空，另一个不为空 不对称
            if not right_node and left_node: return False
            elif not left_node and right_node: return False
            #左右两个节点都为空 对称
            elif not left_node and not right_node: continue
            #左右两个节点都存在，比较数值是否相等,这有这种情况，才需要往下做递归
            elif left_node and right_node:
                if left_node.val != right_node.val:
                    return False
                else:
                    q.append(right_node.right) #右树外侧
                    q.append(left_node.left) #左树外侧
                    q.append(right_node.left)  #右树内侧
                    q.append(left_node.right)  #左树内侧
        return True

            




        
        

        

        
        
    
        
            


  


            
