'''
#二维数组
class Solution:
    def numSquares(self, n: int) -> int:
        #定义dp数组的含义：填满容量为n的书包最少需要dp件物品

        #确定遍历的物品个数
        import math
        p_num = int(math.sqrt(n))
    
        #初始化dp数组,由于后面是求min值，所以初始化为无穷大
        dp = [[float('inf')] * (n+1) for _ in range(p_num+1)]
        #第0行的物品重量是0，所以不管它 直接从第1行开始遍历
        #第1行初始化：第一个物品也就是1的重量，因此
        for j in range(n+1):
            dp[1][j] = j
        #第0列初始化：书包容量为0的时候，都是0
        for i in range(p_num+1):
            dp[i][0] = 0

        #由于这个是完全背包且求的是多少件物品而不是多少种填满的方法所以不用想是排列数还是组合数
        #所以先遍历哪个都行,我们这儿先遍历背包后遍历物品吧
        #遍历到第i个物品，如果拿的话，就是dp[i][j-i*i]+1
        #如果不拿的话，就是dp[i-1][j]
        for j in range(1,n+1):
            for i in range(1,p_num+1):
                #如果书包容量允许：
                if j >= i*i:
                    dp[i][j] = min(dp[i][j-i*i]+1,dp[i-1][j])
                #如果书包容量不允许：
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[p_num][n]
'''

#一维数组
class Solution:
    def numSquares(self, n: int) -> int:
        import math
        p_num = int(math.sqrt(n))
        dp = [float('inf')] * (n+1)
        #初始化，当书包容量为0的时候用0个物品放满
        dp[0] = 0

        for j in range(1,n+1):
            for i in range(1,p_num+1):
                if j >= i*i:
                    dp[j] = min(dp[j],dp[j-i*i]+1)
        return dp[n]






        
