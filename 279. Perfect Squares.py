class Solution:
    def numSquares(self, n: int) -> int:
        #完全背包，装满容量为n的书包，最少需要的物品个数,非排列组合，for循环无所谓
        #装满容量为j的书包最少需要的物品个数为dp[j]
        #递推公式:dp[j] = min(dp[j],dp[j-num]+1)
        #根据递推公式，需要将非0下标初始化为无穷大，而dp[0] = 0,因为填满容量为0的书包最少需要0个物品
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        # 遍历物品的时候只需要遍历，1到 n ** (0.5)向下取整，因为比如n=16, 只需要遍历到4的平方就行了，n=17的话，也只需要遍历到4的平方 notice: int(3.5) = 3

        for num in range(1, int(n ** 0.5)+1):
            for j in range(num * num, n+1):
                dp[j] = min(dp[j], dp[j-num*num]+1)
        return dp[n]
        






        
