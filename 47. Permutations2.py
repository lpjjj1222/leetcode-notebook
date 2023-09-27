#这个的去重和组合问题的去重一毛一样
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        nums.sort()
        used = [False] * len(nums)
        self.backtracking(nums, [], used)
        return self.result

    def backtracking(self, nums, path, used):
        if len(path) == len(nums):
            self.result.append(list(path))
            return
        
        for index in range(0,len(nums)):
            if used[index] == True:
                continue
            elif index > 0 and nums[index] == nums[index-1] and used[index-1] == False:
                continue
            else:
                path.append(nums[index])
                used[index] = True

            self.backtracking(nums,path, used)
            path.pop()
            used[index] = False
        
