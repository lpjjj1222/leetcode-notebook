#这个是自己做出来的去重方法，跟组合总和2，即leetcode40的去重方法是一样的。
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        self.last_pop = None
        self.backtracking([], 0, nums,0)
        self.result.append([])
        return self.result

    def backtracking(self, path, startIndex, nums,level):
        for index in range(startIndex, len(nums)):
            if nums[index] == self.last_pop:
                continue
            path.append(nums[index])
            self.result.append(list(path))
            self.backtracking(path, index+1, nums)
            self.last_pop = path.pop()
'''

#代码随想录里用的是used数组

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        used = [False] * len(nums)
        self.backtracking([],0,nums,used)
        self.result.append([])
        return self.result

    def backtracking(self, path, startIndex, nums, used):
        for index in range(startIndex, len(nums)):
            if index > 0 and nums[index] == nums[index-1] and used[index-1] == False:
                continue
            else:
                path.append(nums[index])
                used[index] = True

            self.result.append(list(path))

            self.backtracking(path, index+1, nums, used)

            path.pop()
            used[index] = False
            


            
        
