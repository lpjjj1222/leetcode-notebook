class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0] * (2*k+1) for _ in range(len(prices))]
        result = 0

        #初始化第一天
        for n in range(2*k+1):
            if n % 2 == 0:
                dp[0][n] = 0
            else:
                dp[0][n] = -prices[0]

        for i in range(1,len(prices)):
            for j in range(2*k+1):
                if j == 0:
                    dp[i][j] = 0
                elif j % 2 == 0: #j是偶数，即不持股的状态
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+prices[i])
                else: #j是奇数，即持股的状态
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]-prices[i])
                if i == len(prices)-1: #最后一天的时候，开始记录不同状态下最大的现金
                    result = max(result, dp[i][j])
        return result
        
                
        
