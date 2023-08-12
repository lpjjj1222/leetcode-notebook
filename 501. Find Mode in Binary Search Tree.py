# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#没有利用二叉搜索树的性质，遍历了一次二叉树，用字典记录频率，且最后要遍历一次字典（递归法）
'''
class Solution:
    from collections import defaultdict

    def searchBST(self, cur, freq_map):
        if not cur:
            return
        freq_map[cur.val] += 1
        self.searchBST(cur.left, freq_map)
        self.searchBST(cur.right, freq_map)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        result = []
        #defaultdict(int)创造一个字典，如果字典里没有某个key却被访问，那么返回值0（因为int）
        freq_map = defaultdict(int)
        self.searchBST(root, freq_map)
        max_freq = max(freq_map.values())
        for node, freq in freq_map.items():
            if freq == max_freq:
                result.append(node)
        return result
'''

#利用双指针，利用二叉搜索树单调递增的性质（中序遍历时），不用引入统计频率的字典(递归法)
'''
class Solution:
    def __init__(self):
        self.result = []
        self.max_freq = 1
        self.pre = None
        self.count = 1
        #count初始化为1是因为pre和cur相等才+1

    def searchBST(self, cur):
        if not cur:
            return
    
        self.searchBST(cur.left) #左

        if self.pre:
            if cur.val == self.pre.val:
                self.count += 1
            else:
                self.count = 1
        self.pre = cur

        if self.count > self.max_freq:
            self.result = [cur.val] #清空之前result里面的值并加入当前的node
            self.max_freq = self.count

        elif self.count == self.max_freq:
            self.result.append(cur.val)

        self.searchBST(cur.right) #右
        
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.searchBST(root)
        return self.result
'''

#（迭代法）用栈代替上面一种写法的递归
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        pre = None
        count = 1
        max_count = 1
        result = []

        while cur or len(stack) >0:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre:
                    if pre.val == cur.val:
                        count += 1
                    else:
                        count = 1
                if count == max_count:
                    result.append(cur.val)
                if count > max_count:
                    result = [cur.val]
                    max_count = count
                pre = cur
                cur = cur.right
        return result








        
        
        
