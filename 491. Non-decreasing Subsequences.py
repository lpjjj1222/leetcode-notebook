#这道题的递增子序列要遵循原序列的先后顺序，即如果原序列里a在b前面，在子序列里不能a在b后面
#代码随想录用used，但是跟前面的那种，即组合总和2和子集2 （leetcode90,40) 不一样

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtracking([], 0, nums,[])
        return self.result
    
    def backtracking(self, path, startIndex, nums, used):

        used = []

        for index in range(startIndex, len(nums)):
            if nums[index] in used or (path and nums[index] < path[-1]):
                continue
            else:
                path.append(nums[index])
                used.append(nums[index])

            if len(path) >= 2:
                self.result.append(list(path))

            
            self.backtracking(path, index+1, nums, used)

            path.pop()

            


        
