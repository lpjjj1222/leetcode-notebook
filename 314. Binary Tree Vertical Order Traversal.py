# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #这题看Editorial
        if not root:
            return []
        q = deque()
        q.append((root, 0)) #queue里放(node, column index)
        col_dict = defaultdict(list) #key: column index, value: node
        while q:
            level_size = len(q)
            for _ in range(level_size):
                node, index = q.popleft()
                col_dict[index].append(node.val)
                if node.left:
                    q.append((node.left, index-1))
                if node.right:
                    q.append((node.right, index+1))
        res = [col_dict[x] for x in sorted(col_dict.keys())]
        return res
            

        
        