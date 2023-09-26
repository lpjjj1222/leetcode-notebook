class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtracking([], 0, nums)
        self.result.append([])
        return self.result

    def backtracking(self, path, startIndex, nums):
        '''
        if startIndex == len(nums):
            return
        '''
        #其实这个终止条件可以完全不写，因为for循环里的条件限制了如果index+1 out of range，就不会取数了
        #例如：for i in range(5,3): print(i)是不会print任何东西的

        for index in range(startIndex, len(nums)):
            path.append(nums[index])
            self.result.append(list(path))
            self.backtracking(path, index+1, nums)
            path.pop()
        
