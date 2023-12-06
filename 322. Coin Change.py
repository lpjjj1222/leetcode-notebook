class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #完全背包  用最少的物品装满背包, amount为背包容量
        #装满容量为j的背包，所需要的最少物品数量为dp[j]
        #遍历到物品coin的时候可以选择放或者不放，如果放则为 dp[j-coin] + 1,这个+1是物品数+1,如果不放就还是dp[j]
        #递推公式：dp[j] = min(dp[j],dp[j-coin]+1)

        #根据递归公式初始化数组，由于递推公式是min(),所以初始值应该为最大值
        #除了dp[0],因为填满容量为0的书包肯定最少只需要0个物品
        #所以把非0下标的dp初始化为最大值
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

  
        #for循环应该谁在外层都可以？因为不是求排列组合数
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j],dp[j-coin]+1)
        #如果dp值为无穷大，说明未曾被更新过，所以没办法把东西放进书包里
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]



        
