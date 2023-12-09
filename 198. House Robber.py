class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp数组的含义：考虑下标为i以下的房屋（包括i),最多可以偷到的财产金额dp[i]
        #考虑到第0-i间时，如果第i间偷，则dp[i] = dp[i-2] + nums[i]因为第i-1间房肯定不能偷
        #如果第i间不偷，则dp[i] = dp[i-1] 

        #edge cases:
        if len(nums)==0:return 0
        if len(nums)==1:return nums[0]
        if len(nums)==2:return max(nums)
        
        dp = [0] * len(nums)

        #初始化？由于nums[i] > 0,所以初始化为0没问题?但i不能从0开始遍历，因为i-2,i-1咋办？
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        

        #递推公式
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
        
