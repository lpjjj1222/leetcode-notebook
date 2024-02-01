class Solution:
    def numTilings(self, n: int) -> int:
        #dp[n]代表2 * n的格子的铺砖的方法数
        dp = [[0] * 2 for i in range(n+1)]
        dp[0][0] = 1
        dp[0][1] = 1
        dp[1][0] = 1
        dp[1][1] = 0

        for i in range(2,n+1):
            dp[i][0] = dp[i-1][0] + dp[i-2][0] + 2*(dp[i-1][1])
            dp[i][1] = dp[i-2][0] + dp[i-1][1]   
        return (dp[n][0]) % (10**9+7)     
