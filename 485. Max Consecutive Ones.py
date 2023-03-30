
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcons = 0
        curcons = 0

        for i in range(len(nums)):
            cur = nums[i]
            if cur == 1:
                curcons +=1
            else:
                maxcons = max(maxcons,curcons)
                curcons = 0 
        return max(maxcons,curcons)

