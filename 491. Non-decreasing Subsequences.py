#这道题的递增子序列要遵循原序列的先后顺序，即如果原序列里a在b前面，在子序列里不能a在b后面

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtracking([], 0, nums, 0, [])
        return self.result
    
    def backtracking(self, path, startIndex, nums, level, used):
        for index in range(startIndex, len(nums)):
            
            if len(path) == 0 or (len(path) > 0 and nums[index] >= path[-1]): #判断是否比前面的大或相等
                if len(used)-1 < level:
                    used.append([])
                if nums[index] in used[level]:#如果已经用过了，就跳过
                    continue
                else: #如果没用过，就加到path且used里也要记录
                    path.append(nums[index])
                    used[level].append(nums[index])
            else:#如果比前面的小
                continue

            if len(path) >= 2:
                self.result.append(list(path))
            used.append([])
            self.backtracking(path, index+1, nums, level+1, used)
            path.pop()
            used.pop() #注意回溯的过程要把used也pop，不然的话 以4767为例子画树
            #会发现得到[4,7,7]后，used是[[4],[7],[7]]嘛
            #到[4,6], used是[[4],[7,6],[7]] used第三层的7应该在上面搞完之后pop掉，如果没pop的话
            #接下来第三层就不能把7放进来，得不到[4,6,7]了
            


        
