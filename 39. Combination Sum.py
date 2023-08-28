'''
if (终止条件):
    存放结果
    return
for 选择本层集合中的元素 节点的孩子数量就是元素个数:
    处理节点
    backtracking(递归,path,startIndex...)
    撤销结果 （回溯）
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.backtracking(candidates, target, 0, [], 0 )
        return self.result


    def backtracking(self, candidates, target, nowsum, path, startIndex):
        if nowsum >= target:
            if nowsum == target:
                    self.result.append(list(path))
            return
        
        for index in range(startIndex, len(candidates)):
            path.append(candidates[index])
            nowsum = sum(path)
            self.backtracking(candidates, target, nowsum, path, index)
            path.pop()
            nowsum = sum(path)  #其实这里的


'''
#剪枝： 将candidates由从小到大排序之后
#如果已经知道接下来for循环遍历到的元素加进去之后会大于Target，那就让这个for循环Break掉，不要再继续遍历这个数以及后面的数了
class Solution:
    def combinationSum(self, candidates: List[int], target: int)-> List[List[int]]:
        self.result = []
        candidates.sort()
        self.backtracking(candidates, target, 0, [], 0)
        return self.result
    
    def backtracking(self, candidates, target, nowsum, path, startIndex):
        if nowsum == target:
            self.result.append(list(path))
            return
        
        for index in range(startIndex, len(candidates)):
            if nowsum + candidates[index] > target:
                break
            path.append(candidates[index])
            nowsum = sum(path)
            self.backtracking(candidates, target, nowsum, path, index)
            path.pop()
            nowsum = sum(path)
'''
            





