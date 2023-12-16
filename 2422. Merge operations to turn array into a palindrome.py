class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        res = 0
        while left < right:
            if nums[right] == nums[left]:
                left += 1
                right -= 1
            elif nums[right] <= nums[left]:
                res += 1
                right -= 1
                nums[right] += nums[right+1] #*******关键
            elif nums[left] <= nums[right]:
                res += 1
                left += 1
                nums[left] += nums[left-1]
        return res
