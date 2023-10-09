class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        #dp[i]是指到达i层有几种方法实现

        #初始化dp数组
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        #递推公式：求到达第三层有几种方法直接用到达第一层的方法数+到达第二层方法数
        #因为第三层要么从第一层跨上来，要么从第二层跨上来
        #因此，第i层有几种方法直接用到达第i-1层的方法数+到达第i-2层方法数
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
       
        
