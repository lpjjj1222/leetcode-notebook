# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#层序遍历 广度遍历
'''
class Solution:
    from collections import deque
    def minDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        if not root:
            return 0
        
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                #如果某个node左右孩子都没有的话直接跳出循环
                #因为找到了第一个叶子结点
                #if not node.right and not node.left:
                if not (node.right or node.left):
                    return (level+1)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
'''

#深度遍历 递归法 - 和广度一样，最小深度就是根节点到叶子结点的最短距离
class Solution:
    def minDepth(self,root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        right_depth = self.minDepth(root.right)
        left_depth = self.minDepth(root.left)
        if right_depth == 0:
            min_depth = left_depth + 1
        elif left_depth == 0:
            min_depth = right_depth + 1
        else:
            min_depth=min(right_depth,left_depth) + 1
        return min_depth

                
