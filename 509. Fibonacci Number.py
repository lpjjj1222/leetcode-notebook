class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        #创建dp table
        dp = [0] * (n+1)

        #初始化dp
        dp[0] = 0
        dp[1] = 1

        #遍历顺序：从前往后，
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        #返回答案
        return dp[n]


 


