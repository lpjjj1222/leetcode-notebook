class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #dp数组的意义，dp[i][j]意思是从初始位置到[i][j]这个点有dp[i][j]条路径

        #创建dp数组
        #将默认值设置为1，是因为第0行和第0列的格子对应的dp值都是1，只有一条路
        dp = [[1] * n] * m
        #初始化dp数组

        #递推公式
        for i in range(1,m):
            for j in range(1,n):
                if i > 0 and j > 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i == 0 or j == 0:
                    continue #因为就是初始值1f
        return dp[m-1][n-1]
        

        

