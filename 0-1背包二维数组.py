def test_2_wei_bag_problem1(weight, value, bagweight):
    #明确dp数组含义，dp[i][j]表示从序号为[0,i]的物品中任选放进容量为j的书包达到的最大价值
    dp = [[0] * (bagweight+1) for _ in range(len(weight))]
    
    #初始化第一行第一列
    #第一列是背包容量为0的时候 所以价值都应该初始化为0
    #第一行是只能放物品0的时候，所以如果背包容量允许，价值就是物品0的价值，容量不允许，就是0

    for j in range (bagweight + 1):
        if j >= weight[0]:
            dp[0][j] = weight[0]
        else:
            dp[0][j] = 0
    #0-1背包问题先遍历物品或者先遍历背包都可以
    #这里先遍历背包吧！
    for j in range(1,bagweight+1):
        for i in range(1,len(weight)):
            if weight[i] <= j:#容量能放得下这个物品 就可以选择放不放进去
                #那遍历到这里的最大价值就是以下两个情况的最大价值
                #①：这个物品放进去之后书包的最大价值为dp[i-1][j-weight[i]] + value[i]
                #因为接下来要从[0,i-1]物品里任选放进容量为j-weight[i]书包里，然后加上这个物品的价值
                #②：这个物品不放进去书包的最大价值为dp[i-1][j]
                #因为接下来要从[0,i-1]物品里任选放进容量为j的书包里
                dp[i][j] = max(dp[i-1][j-weight[i]] + value[i], dp[i-1][j])
            else:#书包容量不允许了，那就只能不放了
                dp[i][j] = dp[i-1][j]
    
    return dp[len(weight)-1][bagweight]


if __name__ == "__main__":

    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4

    result = test_2_wei_bag_problem1(weight, value, bagweight)
    print(result)

            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
