class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #如果Add是所有带加号的和，Minus是所有带减号的和
        #Add + Minus = Sum
        #Add - Minus = target
        #得到 2Add = Sum + target, Add = (Sum + target) / 2
        #如果无法整除，就搞不了，因为可选的都是整数
        sumup = sum(nums)

        if (sumup + target) % 2 != 0:
            return 0
        #如果各个数的绝对值之和<target的绝对值，搞不了
        if sumup < abs(target):
            return 0
        target_sum = int((sumup + target) / 2)

        #dp数组的含义：要想装满容量为j的书包，有dp[j]种方法
        #对于[*,#,%,^],要想装满总重量为5的书包：
        #如果已知有*，则组合方法有dp[j-*]
        #如果已知有#，则组合方法有dp[j-#]
        #如果已知有%，则组合方法有dp[j-%]
        #如果已知有^，则组合方法有dp[j-^]
        #dp[j]=所有加起来
        #所以递推公式是: dp[j] += dp[j-nums[i]]

        #题目转化为装满容量为target_sum的背包，有dp[j]种方法
        dp = [0] * (target_sum + 1)
        #一定要初始化否则全为1， 为什么dp[0] = 1呢？
        #因为例如上面，求dp[5]，已知有一个5，那么组合数就转化为dp[0],这个时候往前面的dp里加多少呢？加1，而非加0.因为直接丢一个5进去，也是一种方法。
        dp[0] = 1

        #一维数组：背包容量倒序遍历（确保dp[j-nums[i]]的dp[j]未被覆盖），for循环先物品后背包（否则一个书包只能放一个物品）
        for num in nums: #物品
            for j in range(target_sum, num-1,-1):
                dp[j] += dp[j-num]
        print(dp)
        return dp[target_sum]





        
