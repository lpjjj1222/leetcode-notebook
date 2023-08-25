#本题直接先看代码随想录视频讲解

#回溯法模板
'''
def backtracking(参数):
    if (终止条件):
        存放结果
        return
    for 选择本层集合中的元素，本节点子节点个数就是集合大小：
        处理节点
        backtracking(参数)
        回溯，撤销结果
'''

#回溯法（未优化）
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.backtracking(n, k , 1, [])
        return self.result
    
    def backtracking(self, n, k, startindex, path):
        if len(path) == k:
            self.result.append(list(path))
            return
        for nn in range(startindex,n+1):
            path.append(nn)
            self.backtracking(n, k, nn + 1, path)
            path.pop()
'''

#回溯法（优化）
#能够优化的地方在：如果n=4 k=4 那for循环的时候，遍历过1就不需要再遍历2 3 4 了
#所以要判断，如果for循环中挑选剩下的节点已经不足以满足我们要求的组合个数，就不往下遍历了
# k - len(path)是剩下的path需要填充的个数
# n - nn + 1是进入for循环后，还剩几个元素选择
#要求： n - nn + 1 >= k - len(path)  即 nn <= n - k + len(path) + 1
#这样的话，放在for循环range的右边就要再加1， 因为range(1,5) 输出的是1,2,3,4
#所以range右边写的是 n-k+len(path)+2


class Solution:
    def combine(self, n:int, k:int) -> List[List[int]]:
        self.result = []
        self.backtracking(n,k,1,[])
        return self.result
    
    def backtracking(self, n, k, startindex, path):
        if len(path) == k:
            self.result.append(list(path))
            return
        for nn in range(startindex,n-k+len(path)+2):
            path.append(nn)
            self.backtracking(n, k ,nn+1,path)
            path.pop()

        

