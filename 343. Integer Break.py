class Solution:
    def integerBreak(self, n: int) -> int:
        #dp数组的意义：拆分数字i之后各个组成元素的最大乘积是dp[i]
        #当i拆成两个数，一个数是j,另一个是i-j，乘积就是j * (i-j)
        #当i拆成两个数以上，一个数是j, 乘积就是j * dp[i-j]
        #如果要求dp[4] 就要遍历j=1,j=2,j=3的情况，分别求每种情况的乘积，然后找最大值

        #初始化dp
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1 # 2只能拆成1 * 1
        # dp[0] 和dp[1]都没有意义，因为都拆不了

        for i in range(3, n+1): 
            #eg.要求dp[5],就要得到dp[4],dp[3],dp[2] 因为会涉及1*dp[4],2*dp[3]等计算
            for j in range(1,i):
                dp[i] = max(j * dp[i-j], j * (i-j), dp[i])
        
        return dp[n]

        

        
