class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #背包容量是二维的，即0的个数和1的个数
        #一个str是一个物品，其0的个数和1的个数是其重量
        #本题要求容量为m,n的书包最多能装多少件物品，所以每个str value为1
        #dp数组的含义是，容量为i,j的书包最多能装的价值为dp[i][j]
        #m-0, n-1
        dp = [[0] * (m+1) for _ in range(n+1)]

        #初始化？
        #因为递推公式有+1,所以怎么都不会是000000，所以应该直接初始化为0就行


        #递推公式
        #背包倒序遍历，for循环先物品后背包
        for string in strs: #物品
          zeros = string.count('0')
          ones = string.count('1')
          for i in range(n,ones-1,-1): #背包容量
            for j in range(m,zeros-1,-1): #背包容量
              dp[i][j] = max(dp[i-ones][j-zeros] + 1, dp[i][j])
        print(dp)
        return dp[n][m]

        
