# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#递归法
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #两个都不存在
            return True
        elif p and not q: #一个存在一个不存在
            return False
        elif not p and q: #一个存在一个不存在
            return False
        else:#两个都存在 比较值是否相等 只有完全相等后才需要向下递归
            if p.val != q.val:
                return False
            else:
                left = self.isSameTree(p.left,q.left)
                right= self.isSameTree(p.right,q.right)
                return left and right
    
    #P和q是1的时候，都存在且值相等，所以需要向下递归
    #left = self.isSameTree(2,2) 得到True
    #right = self.isSameTree(3,3,) 得到True
    #return True
'''

#队列法 两两放入 两两取出
class Solution:
    from collections import deque
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue = deque([p,q])

        while queue:
            nodep = queue.popleft()
            nodeq = queue.popleft()
            if not nodep and not nodeq:
                continue 
                #注意这里不是return True因为如果是[1，N，N]和[1,N,2]，
                #那么在遍历到第二个的时候直接return True
                #跳出while queue:循环最终结果就是True,就错了！
            elif not nodep and nodeq:
                return False
            elif nodep and not nodeq:
                return False
            else:
                if nodep.val != nodeq.val:
                    return False
                else:
                    queue.append(nodep.left)
                    queue.append(nodeq.left)
                    queue.append(nodep.right)
                    queue.append(nodeq.right)
        return True


                



        
        
        

