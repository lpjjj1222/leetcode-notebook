class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp数组的含义
        #dp[i][j] 从[0,i]种面额中任选几张放到容量为j的书包里，使书包刚好装满
        

        #创建dp数组
        dp = [[0] * (amount+1) for _ in range(len(coins))]
        #初始化dp数组 初始化第一行 why要初始化第一行，因为递推公式设计[i-1]
        #当书包容量能够整除面额的时候为1，其他时候为0，（书包容量为0的时候得是1，确实很奇怪but没办法就是这样画二维数组就知道这个得保持1）
        for j in range(amount+1):
            if j % coins[0] == 0:
                dp[0][j] = 1
        #初始化第一列 当书包容量为0的时候得保持1 确实很奇怪but没办法就是这样画二维数组就知道这个得保持1
        for i in range(len(coins)):
            dp[i][0] = 1
        #为什么要这样初始化，画一个二维表格就知道了


        for j in range(1,amount+1):
            if j == coins[0]:
                dp[0][j] = 1
            

        #先遍历物品后遍历书包，书包正序遍历
        #遍历到物品i时，如果拿该物品，就是dp[i][j-coins[i]] 这里跟0-1背包的二维数组不一样，二维数组这里是dp[i-1][j-coins[i]],这里不用-1是因为，即使确定我们拿了一个i物品，剩下的也不是从[0,i-1]物品任选，而是从[0,i]物品任选，因为没有规定一个物品只能拿一次
        #如果不拿该物品，就跟遍历到上一个物品一样，dp[i-1][j]
        for i in range(1,len(coins)):
            for j in range(amount+1):
                #如果书包容量不够装了，就只有不拿该物品的可能
                if j < coins[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-coins[i]] + dp[i-1][j]
        return dp[len(coins)-1][amount]

        
