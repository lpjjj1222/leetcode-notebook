# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        q = deque()
        if not root:
            return 0
        q.append((root,0))

        while q:
            level_result = 0
            level_length = len(q)

            for _ in range(level_length):
                node,index = q.popleft()
                if _ == 0:
                    first_index = index

                if node.left:
                    q.append((node.left,index*2))
                if node.right:
                    q.append((node.right, index*2+1))
            level_result = index - first_index + 1
            max_width = max(max_width, level_result)
        return max_width




            

        
