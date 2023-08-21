# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#递归array(递归法)
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return
        #在array中间的作为根节点，因为左边比它小右边比它大
        root_index = len(nums) // 2
        #这样的话，如果是nums奇数，就是中间，如果是偶数，就是中间两个数的右边那个
        #因为试验一下，nums偶数的时候不论是取中间两个数的左边还是右边，都可以，只是构造出来的树不一样
        root = TreeNode(nums[root_index])
        root.left = self.sortedArrayToBST(nums[:root_index])
        root.right = self.sortedArrayToBST(nums[root_index+1:])
        return root
'''

#递归index(递归法)
'''
class Solution:
    def sortedArrayToBST(self, nums:List[int]) -> Optional[TreeNode]:
        root = self.Traversal(0, len(nums), nums)
        return root

    def Traversal(self, left, right, nums):
        if right <= left:
            return None
        mid = left + (right-left) // 2
        root = TreeNode(nums[mid])
        root.left = self.Traversal(left, mid, nums)
        root.right = self.Traversal(mid+1, right, nums)
        return root
'''

#迭代法(deque)
class Solution:
    from collections import deque
    def sortedArrayToBST(self, nums:List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        root = TreeNode(0)

        nodeq = deque()
        leftq = deque()
        rightq = deque()
        
        nodeq.append(root)
        leftq.append(0)
        rightq.append(len(nums)-1)
        
        while nodeq:
            curNode = nodeq.popleft()
            left = leftq.popleft()
            right = rightq.popleft()
            mid = left + (right - left) // 2
            curNode.val = nums[mid]


            #处理左子树
            if left <= mid - 1:
                curNode.left = TreeNode(0)
                nodeq.append(curNode.left)
                leftq.append(left)
                rightq.append(mid-1)
                
            if mid+1 <= right:
                curNode.right = TreeNode(0)
                nodeq.append(curNode.right)
                leftq.append(mid+1)
                rightq.append(right)
        return root






        
        
