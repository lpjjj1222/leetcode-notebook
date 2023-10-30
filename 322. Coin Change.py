#这题初始化贼重要，如果没有想到正确的初始化值后面就会有贼多bug，我是看代码随想录的答案知道咋初始化的555
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Base case:如果amount = 0, 0个物品就可以装满，so返回0
        if amount == 0:
            return 0
        coins = sorted(coins)
        #dp数组的含义：在[0,i]物品里任选，装满容量为j的背包，最少使用的物品数为dp[i][j]

        #创建dp数组 这里用float('inf')初始化是因为后面要对比正上方的数和左边的数取最小值，那正上方就应该初始化为正无穷
        dp = [[float('inf')] * (amount+1) for _ in range (len(coins))]
        #初始化dp数组
        #初始化第0行：第0行就是用第0个物品装满不同容量的背包的数量嘛，那就能整除的整除，不能整除就还是正无穷
        for j in range(amount+1):
            if j % coins[0] == 0: #如果能整除
                dp[0][j] = int(j / coins[0])
        #初始化第0列：画二维数组的时候发现第0列全部初始化为0才对
        for i in range(len(coins)):
            dp[i][0] = 0

        #递推公式
        #分拿i和不拿i两种情况，取里面的最小值.
        #拿i就是dp[i][j] = dp[i][j-coins[i]]+1 是[i]instead of [i-1]是因为这是完全背包取了还能取
        #不拿i就是dp[i][j] = dp[i-1][j]
        #注意这题求的是最少用几个物品填满，而不是有几种方法填满。
        #如果是求几种方法填满，就要判断是组合数还是排列数，组合的话先物品，排列的话先背包
        #这题放钱币有没有顺序都无所谓，答案一样，所以先物品后背包，先背包后物品都行
        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                if j >= coins[i]: #如果书包容量允许
                #注意下面取最小值前的判断是否出现0
                    dp[i][j] = min(dp[i][j-coins[i]]+1,dp[i-1][j])
                else: #如果书包容量不允许，就只能不拿，就跟上一行一样
                    dp[i][j] = dp[i-1][j]
        result = dp[len(coins)-1][amount]
        if result == float('inf'):
            return -1
        return result


'''
#一维数组，根据二维自己写出来滴
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(len(coins)):
            for j in range(1,amount+1):
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j-coins[i]]+1)
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
'''


        
