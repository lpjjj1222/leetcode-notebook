# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #在102层序遍历的基础上，将每一层的最右边，也就是二维数组每一行的最后一个数放到结果列表里即可
        q = deque()
        result = []

        if root:
            q.append(root)
        else:
            return

        while q:
            size = len(q)
            for _ in range(size):
                print(_)
                node = q.popleft()
                if _ == (size - 1):#即遍历到一层的最后一个，即最右边一个的时候
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result


 

        
