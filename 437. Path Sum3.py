# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#这题要看会员的editorial!!!!
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(root,cur_sum):
            nonlocal count
            #nonlocal用于在嵌套函数内部，对外部的不可变对象进行修改
            if not root:
                return
            cur_sum += root.val
            if cur_sum == targetSum:
                count += 1
            count += h[cur_sum-targetSum]
            h[cur_sum] += 1
            
            left = dfs(root.left, cur_sum)
            right = dfs(root.right, cur_sum)
            h[cur_sum] -= 1  #回溯，遍历完后遍历上面的node的时候下面的key和value就不适用了

        count = 0
        k = targetSum
        h = defaultdict(int)
        dfs(root,0)

        return count


                
