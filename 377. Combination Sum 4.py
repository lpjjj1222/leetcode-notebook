class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #完全背包： target书包容量， nums[i]物品的重量， 求装满书包有几种方法（排列问题顺序matters）
        #凑成和为j的排列个数为:dp[j]
        dp = [0] * (target+1)

        dp[0] = 1

        #排列问题for循环先背包后物品
        for j in range(target+1):
            for num in nums:
                if j >= num:
                    dp[j] += dp[j-num]
        return dp[target] 
        

        
