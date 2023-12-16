from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(n: TreeNode, val: int, path: List[str]) -> bool:
            #STEP1：递归分别找start和destination,看从root分别到这两个点需要什么路径（注意靠下方的节点对path的增加先发生所以其实实际路径应该是返回过来的）
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path += "L"
            elif n.right and find(n.right, val, path):
                path += "R"
            return path
        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)

        #STEP2：把共同路径删掉，例如当start和destination都在同一颗子树时，要把从root到这颗子树根节点的路径去掉才能找到lowest common ancestor
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))



      
