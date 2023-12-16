'''
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        max_num = float('-inf')
        count = 0
        
        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
            if i > 0:
                nums[i] = max_num + num + nums[i-1]
            else:
                nums[i] = 2 * nums[i]
        return nums
'''

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n
        dp = [0] * n

        arr[0] = 2 * nums[0]
        dp[0] = 2 * nums[0]

        for i in range(1,n):
            arr[i] = nums[i] + max(nums[i], arr[i-1]-nums[i-1])
            dp[i] = dp[i-1] + arr[i]
        return dp




        
