# Time Complexity - O(N)
# Space Complexity - O(1)
# https://leetcode.com/problems/missing-ranges/
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        n = len(nums)
        if not nums:
            return [[lower,upper]]
        
        if nums[0] > lower:
            res.append([lower,nums[0]-1])

        for i in range(n-1): #从第一个数遍历到倒数第二个数
            if nums[i+1] - nums[i] != 1: #如果不是连续的数
                res.append([nums[i]+1,nums[i+1]-1])

        if nums[n-1] < upper:
            res.append([nums[n-1]+1,upper]) 

        return res

                


