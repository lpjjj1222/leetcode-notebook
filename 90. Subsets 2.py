#这个是自己做出来的去重方法，跟组合总和2，即leetcode40的去重方法是一样的。
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.last_pop = None
        self.backtracking([], 0, nums)
        self.result.append([])
        return self.result

    def backtracking(self, path, startIndex, nums):
        for index in range(startIndex, len(nums)):
            if nums[index] == self.last_pop:
                continue
            path.append(nums[index])
            self.result.append(list(path))
            self.backtracking(path, index+1, nums)
            self.last_pop = path.pop()
        
