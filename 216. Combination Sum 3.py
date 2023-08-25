class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.result = []
        self.backtracking(k, n, 1, [])
        return self.result
        
    def backtracking(self, nums, targetsum, startindex, path):
        if sum(path) > targetsum:#剪枝1
            return
        if len(path) == nums:
            if sum(path) == targetsum:
                self.result.append(list(path))
            return

        #剪枝2
        #这里的剪枝的意思是：
        #比如说我的path还差3个数达到nums的预期，然后我遍历到7了，那就不用再遍历8和9
        #因为只剩下一种可能就是把 7 8 9都丢进去
        for i in range(startindex, 9-(nums-len(path))+2):
            path.append(i)
            self.backtracking(nums, targetsum,i+1,path)
            path.pop()
        
            




