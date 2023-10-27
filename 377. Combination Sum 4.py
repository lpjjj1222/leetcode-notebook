#这道题不用看代码随想录，先看下面注释掉的二维数组 知道二维数组是怎么推出来的之后，看代码随想录的答案一维数组
#想这道题的时候nums[1,3,5],target=6地去画表格
'''
#二维数组 by myself
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        #Base case1： nums的最小值都大于target
        if min(nums) > target:
            return 0
        #Base case2: nums里有大于target的数，把这些数直接扔掉
        nums = [x for x in nums if x <= target]
        
        #完全背包问题 
        #但是同样的数字组合如果顺序不一样，会算不同的方法
        #dp数组的含义：dp[i][j]为从[0,i]的数里任选几个放到容量为j的书包里，使书包刚好装满的方法
        
        #创建dp数组
        dp = [[0] * (target+1) for _ in range(len(nums))]

        #初始化dp数组
        #由于递推公式设计[i-1]我们要初始化第一行
        #第一行的[0][0]必须是1（经验），其他第一行的数如果j能够被物品[0]整除，就1，否则0
        for j in range(target+1):
            if j == 0:
                dp[0][j] = 1
            elif j % nums[0] == 0: #如果能够被整除的话... 其实0%num[0]也=0，但是专门写出来是为了更容易记住
                dp[0][j] = 1
 
        #初始化第一列(经验) 当书包容量为0的时候，都初始化为1
        for i in range(len(nums)):
            dp[i][0] = 1
        
        #递推公式
        #这题可以理解为爬楼梯问题，爬楼梯问题是每次只能踏1步或者2步，那么如果要算踏到第5层有多少种方法，只需要算踏到第4层，第3层有多少种方法，然后把两个数加起来就是答案，因为跨到第三层之后只有一个选择，就是跨两层到第五层（如果跨一步，那就属于从第四层开始），跨到第四层后只有一个选择，就是跨1层到第五层
        #这题同理，target=4的方法可以理解为，target=4-1=3的方法+ target=4-2=2的方法+ target= 4-3=1的方法
        #所以放到二维数组中来看，就是要从前面的列里找数加起来，所以先遍历书包容量后遍历物品

        #例如，nums=[1,3,5],target=6, dp[5][6] = dp[5][6-5] + dp[5][6-3] + dp[5][6-1]
        for j in range(1,target+1):
            for i in range(1,len(nums)):
                if j >= nums[i]: #书包容量允许
                    for index in range(i+1): #index在0到i之间一个个取
                        dp[i][j] += dp[i][j-nums[index]]
                else: #书包容量不允许 这个物品不能放，那就跟上面一行情况一样，从上面复制下来
                    dp[i][j] = dp[i-1][j]

        return dp[len(nums)-1][target]
'''

#一维数组，by 代码随想录 递推公式本质上跟二维数组思路是一样的
#其实就是把二维数组的那么多行压缩成一行，每次找值向左找就行
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1) #后面从左往右推，推到最右边就是答案
        #每次往右推都要遍历各行，即各物品
        dp[0] = 1
        for j in range(1, target + 1):  # 遍历背包
            for i in range(len(nums)):  # 遍历物品
                if j - nums[i] >= 0:  #如果书包容量允许， 如果不允许，就不遍历这个物品i，也就不用更新
                    dp[j] += dp[j - nums[i]] #这个就是爬楼梯
        return dp[target]
