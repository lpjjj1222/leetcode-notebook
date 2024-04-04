class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #0代表不持股
        #1代表持股
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], 0 - prices[i])
        return dp[len(prices)-1][0]
        