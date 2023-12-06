class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #完全背包，正序，for循环无所谓
        #书包容量amount,weight是coin的值,装满背包有dp[j]方法
        #多少种方法的递推公式：dp[j] += dp[j-coins[i]]

        dp = [0] * (amount+1)
        dp[0] = 1
        
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j-coin]
        return dp[amount]


        
