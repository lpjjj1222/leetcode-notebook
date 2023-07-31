# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.result = []
        self.path = []
        if not root:
            return self.result
        self.traversal(root,self.path,self.result)
        return self.result

    def traversal(self,node,path,result):
        if node:
            self.path.append(node.val)
            if node.right==None and node.left==None:#到叶子结点
                strpath = "->".join(map(str,self.path))
                #map()函数是用来将一个函数应用于可迭代对象（例如列表、元组、集合等）的每个元素，并返回一个新的可迭代对象
                self.result.append(strpath)
            
            if node.left:#没到叶子结点
                self.traversal(node.left,self.path,self.result)
                self.path.pop() #回溯
            
            if node.right: #没到叶子结点
                self.traversal(node.right,self.path,self.result)
                self.path.pop() #回溯

    #看着Example 1过一遍：
    #首先path append 1. -> traversal(2,[1],result) 
    #对2来说， append2， 没有左孩子，所以 traversal(5,[1,2,],result)
    #对5来说，append5, 叶子结点了，所以 strpath = "1->2->5", result = ["1->2->5"]
    #5处理完了，回到2的if node.right的第二步，即path.pop 此时path变成[1,2]
    #2处理完了，回到1的if node.left的第二部，即path.pop 此时path变成[1]
    #接着1还没完，1还有if node.right， ->traversal(3,[1],result)
    #对3来说，append3, 到叶子结点，所以strpath = "1->3",result = ["1->3"]
    #3处理完了，回到1的if node.right的第二步，即path.pop，此时path变成[1]
    #处理完毕
'''


#递归回溯精简版（回溯隐形）

class Solution:
    def binaryTreePaths(self,root: Optional[TreeNode]) ->List[str]:
        self.result = []
        self.path = []
        if not root:
            return result
        self.Traversal(root,self.path,self.result)
        return self.result
    
    def Traversal(self,node,path,result):
        if node:
            path.append(node.val)
        #如果遇到叶子结点，就形成一条路径了
        if not node.left and not node.right:
            strpath="->".join(map(str,path))
            self.result.append(strpath)
        #如果不是叶子结点，继续向下遍历
        
        if node.left:
            self.Traversal(node.left,path[:],self.result)
        if node.right:
            self.Traversal(node.right,path[:],self.result)
        
        #注意上面这个path[:]!!!!!!!!!!!!!!!!!!!!!!!!!!
        #很重要，因为如果没有用[:]，就会是wrong answer
        #因为递归完左子树之后，如果没用[:]相当于截止到node的path已经改变了，增加了左子树的东西
        #这样遍历右子树的时候path的起始部分就包括了左子树的内容
        #但是如果用了[:]的话，path[:]就相当于复制了一份新的列表，就不会被列表的可变性影响


        
            

        
            
