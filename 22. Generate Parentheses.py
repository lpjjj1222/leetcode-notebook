#DFS
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(string,left,right):#string是目前的结果，left是还能增加多少左括号，right还能增加多少右括号
            if len(string) == 2 * n:
                res.append(string)
                return #用于表示结束当前递归并返回到函数被调用的地方
            if left > 0:
                helper(string+'(',left-1,right)
            if right > 0 and left < right: 
                #这个left<right说明左括号比右括号用多了一个，即string里的左括号是多过右的才可以在最后放入右括号
                helper(string+')',left, right-1)
        helper('',n,n)
        return res
        
    
        
