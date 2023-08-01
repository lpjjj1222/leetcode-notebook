# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#我自己写的
'''
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result=[]
        if not root:
            return self.result
        
        self.Traversal(root,targetSum,[])
        return self.result

    def Traversal(self,root,targetSum,path):
        if not root:
            return
        path.append(root.val)
        targetSum -= root.val
        #如果遇到叶子结点，判断是否递减到0
        if not root.right and not root.left and targetSum ==0:
                self.result.append(path)
        
        targetSum_copy_for_righttree = targetSum
        left = self.Traversal(root.left, targetSum,path[:])
        right = self.Traversal(root.right, targetSum_copy_for_righttree,path[:])
'''

#代码随想录的递归精简版本

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        result = []
        self.traversal(root, targetSum, [], result)
        return result
    def traversal(self,node, count, path, result):
            if not node:
                return
            path.append(node.val)
            count -= node.val
            if not node.left and not node.right and count == 0:
                result.append(list(path))
                #注意！！！！！！！！！！！！！！！！！！
                #上面这个如果没有list（）包裹就会报错，因为list(path)相当于copy了一份path
                #不会让列表的可变性影响
                #打个比方
                
                #a = [1,2,3]
                #result=[]
                #result.append(a)
                #此时result是[[1,2,3]]
                #继续： a.append(4)
                #此时result是[[1,2,3,4]]

                #Q：但为什么我上面自己写的版本不需要list（path）呢
                #A：因为我在每一次递归的时候用的是path[:]递归，已经是复制了一份新的了
                   #不过，应该还是代码随想录这个占用的空间复杂度比较小，
                   #因为只有在遍历到符合要求的叶子节点的时候，才复制
            
            self.traversal(node.left, count, path, result)
            self.traversal(node.right, count, path, result)
            path.pop() #回溯
