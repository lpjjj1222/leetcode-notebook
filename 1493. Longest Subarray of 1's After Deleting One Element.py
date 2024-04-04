class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        left = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
                while zeros > 1:
                    if nums[left] == 0:
                        zeros -= 1
                    left += 1
            res = max(res, right - left + 1)
        return res - 1

                

        
