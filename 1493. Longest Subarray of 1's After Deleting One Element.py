class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = window_size = zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                left += 1
                if nums[left-1] == 0:
                    zeros -= 1
            window_size = max(window_size,right - left + 1)
        return window_size-1
        
