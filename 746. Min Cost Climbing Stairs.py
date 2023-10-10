class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #dp数组的意义：到达i台阶的最小花费就是dp[i]

        top_index  = len(cost)

        #生成dp数组
        dp = [0] * (top_index + 1)

        #初始化dp数组 (因为我们可以从0开始也可以从1开始，且只有跳的时候才需要花费)
        dp[0] = 0
        dp[1] = 0

        #递推公式 (前一个台阶+花费  & 后一个台阶+花费 里面选最小的)
        for i in range(2,top_index+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[top_index] 

        
