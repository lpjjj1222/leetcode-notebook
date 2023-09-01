'''
if 终止条件：
    记录结果
    return

for 选择这层的元素，节点的孩子个数就是该层的元素个数:
    处理节点
    self.backtracking(startindex, path...)
    撤销结果（回溯）

'''

#这题是我自己做出来的哦！难点在于，以case2举例子，1 2 2 2 5，target = 5
#可能会得到多个重复的组合122
#因为 1 2 2 得到之后要回溯pop一个2出来，接着把第三个2放进来，又符合，又加入了，这就重复了
#所以如果接下来要放进去的数和回溯pop出来的结果相等，那就直接continue
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return
        self.result = []
        self.lastpop = None
        candidates.sort()
        self.backtracking([],0,candidates,target)
        return self.result


    
    def backtracking(self, path, startIndex, candidates, target):
        if sum(path) == target and path not in self.result:
            self.result.append(list(path))
            return
        
        for index in range(startIndex, len(candidates)):
            if sum(path) + candidates[index] > target:
                break
            if self.lastpop == candidates[index]:
                continue
            path.append(candidates[index])
            self.backtracking(path, index+1, candidates, target)
            self.lastpop = path.pop()




        
