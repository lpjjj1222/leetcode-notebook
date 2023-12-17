# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.counter = 0
        def dfs(node):
            #对于某一个node,以这个node作为根节点，有若干个叶子，返回一个列表，列表里是该node到这些叶子的距离
            if not node:
                return []
            if not node.left and not node.right:
                return [0]
            left = dfs(node.left)
            right = dfs(node.right)

            for l in left:
                for r in right:
                    if l + r + 2 <= distance:
                        self.counter += 1
            return [x+1 for x in left+right if x+1 < distance]
        dfs(root)
        return self.counter


             
             

        
