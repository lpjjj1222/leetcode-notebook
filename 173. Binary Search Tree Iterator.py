# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#下面这种方法把节点存储在队列里，这样next()和hasNext()只需要O(1)时间复杂度，但是空间复杂度因为要把一整颗树存进去，所以是O(N)，即有多少个节点就存多少
#空间复杂度是O(N)因为每个节点都要遍历一次


'''
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.q = deque()
        def traversal(root):
            if not root:
                return 
            left = traversal(root.left)
            self.q.append(root.val)
            right = traversal(root.right)
        traversal(root)

        

    def next(self) -> int:
        if len(self.q)>0:
            return self.q.popleft()
        
    def hasNext(self) -> bool:
        if len(self.q) > 0:
            return True
        else:
            return False
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#follow up question希望O(h)memory即存储的空间是树的高度，要用下面这种方法
#先从root一直往左把所有节点放进去，栈顶是最小的元素（二叉搜索树），当找next的时候如果前面pop出来的有右子树
#则把右子树当作root一直往左放节点进去

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.just_pop = None
        self.left_traversal(root)
    def left_traversal(self,root):
        self.stack.append(root)
        if not root.left:
            return
        self.left_traversal(root.left)
    

    def next(self) -> int:
        if self.just_pop and self.just_pop.right:
            self.left_traversal(self.just_pop.right)
        self.just_pop = self.stack.pop()
        return self.just_pop.val
        
    def hasNext(self) -> bool:
        if len(self.stack) > 0 or self.just_pop.right:
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
        
