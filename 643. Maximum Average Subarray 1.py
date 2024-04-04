class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w = sum(nums[:k])
        n = len(nums)
        res = w / k
        left , right = 0, k #包括left不包括right
        for right in range(k,len(nums)):
            w = w + nums[right] - nums[left]
            res = max(res,w/k)
            left += 1
        return res
        

            

        
