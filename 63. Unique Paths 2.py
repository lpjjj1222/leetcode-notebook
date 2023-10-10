class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #创建dp数组 这里不可以把默认值都弄成1，因为如果障碍在第一列或者第一行，后面的格子是过不去的
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        #处理特殊情况:起点终点有障碍物
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        elif m == 1 and n == 1: #特殊情况，只有一行一列，且无障碍物
            return 1

        #dp = [[0] * n] * m <-这种创建dp方式不可取！！因为都有一行变的时候，别的行也会一起发生改变，他们会共享引用！！！
        dp = [[0] * n for _ in range(m)]


        for i in range(1,m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for j in range(1,n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break
        #递推公式
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


        
