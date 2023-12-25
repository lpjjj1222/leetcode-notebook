class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        index = 0
        window = 0
        for index in range(k):
            window += nums[index]
        res = window

        index += 1
        while index < len(nums):
            window = window+nums[index]-nums[index-k]
            res = max(res,window)
            index+=1
        return max(res,window) / k #nums = [5], k=1的情况，res 在return的时候还是-inf

            

        
