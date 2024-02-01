class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 5 for _ in range(len(prices))]
        #因为prices的长度可以为1，所以可以同一天多次交易操作
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0

        for i in range(1,len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][0]-prices[i],dp[i-1][1])
            dp[i][2] = max(dp[i-1][1]+prices[i],dp[i-1][2])
            dp[i][3] = max(dp[i-1][2]-prices[i],dp[i-1][3])
            dp[i][4] = max(dp[i-1][3]+prices[i],dp[i-1][4])
        return max(dp[len(prices)-1][4], dp[len(prices)-1][2],dp[len(prices)-1][0])
        
