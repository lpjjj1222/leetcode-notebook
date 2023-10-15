#代码随想录的思路：只要尽可能把石头分成重量相等的两堆，碰撞之后剩下的就可以最小
#例如，总和为23， 就找一个容量为11的书包，剩下的重量为12。
#书包尽可能往11装，如果装不到只装下10，那另一堆石头的重量就是23-10 = 13
#相撞之后就是3
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2 
        #创建初始化dp数组
        dp = [0] * (target + 1)

        #递推公式
        #先遍历物品后遍历书包，书包倒序遍历
        for stone in stones:
            for j in range(target, stone-1, -1):
                dp[j] = max(dp[j], dp[j-stone] + stone)
        
        #第一堆物品的重量：dp[target]， 第二堆物品的重量:sum-dp[target]
        #由于target算的时候是向下取整，所以第一堆物品的重量和一定小于第二堆
        #所以碰撞后剩下的重量为第二堆-第一堆
        return sum(stones)-dp[target]-dp[target]
        



        
