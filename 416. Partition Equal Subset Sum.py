class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #0-1背包问题：因为一个元素只能被选中一次
        #sum(nums)/2就是满足条件的target书包容量
        #元素的值既是物品的重量也是物品的价值
        #当寻找到dp[target] == target，即容量为target的书包价值也为target时
        #得到满足条件的解

        #如果本来nums的和加起来等于一个奇数，而元素都是整数，奇数除以2之后有小数点，不可能实现
        if sum(nums) % 2 != 0:
            return False

        target = int(sum(nums) / 2)

        #创建一维数组并初始化
        dp = [0] * (target + 1)

        #递推公式
        #一维数组先遍历物品后遍历背包 背包倒序遍历
        for num in nums:
            for j in range(target, num-1, -1): 
                #j从target那么大遍历到哪里结束嘞
                #遍历到j=num的重量就行，因为容量比j的重量还要小的话，根本不可能放进去，就不用遍历了，滚动后的数组肯定还是取跟上一行一样的数
                dp[j] = max(dp[j-num]+num, dp[j])
        
        if dp[target] == target:
            return True
        else:
            return False
                

        
