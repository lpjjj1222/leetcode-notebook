#看代码随想录 提到 排列用used数组后一下子就做出来啦
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        used = [False] * len(nums)
        self.backtracking([], nums, used)
        return self.result
    
    def backtracking(self,path, nums, used):
        if len(path) == len(nums):
            self.result.append(list(path))
            return
        
        for index in range(0,len(nums)):
            if used[index] == True:
                continue
            else:
                path.append(nums[index])
                used[index] = True

            self.backtracking(path, nums, used)

            path.pop()
            used[index] = False

    
