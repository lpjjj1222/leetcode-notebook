def test_1_wei_bag_problem(weight, value, bagweight):
    #一维数组一定要先遍历物品再遍历背包
    #因为一维数组是滚动数组，结合上一行的数据更新到下一行
    #所以得从上往下
    #背包的遍历顺序一定是倒序，看代码随想录的视频或者自己举例子就知道
    #如果正序遍历的话，会把同一个物品放进背包两次
    
    
    #创建和初始化数组
    dp = [0] * (bagweight+1)
    #j=0的时候，即背包容量为0的时候，背包里的价值肯定只能为0
    #其他书包容量的时候，初始化为0是因为后面要从上一行的数值本身以及新数值取最大值
    #所以如果初始值太大，会not make sense
    
    for i in range(len(weight)):
        for j in range(bagweight, -1, -1):
            if weight[i] <= j: #如果书包容量允许，可以选放i物品或者不放
                #不放的话就还是dp[j]，放的话就是dp[j-weight[i]] + value[i]
                dp[j] = max(dp[j], (dp[j-weight[i]] + value[i]))
            else:
                #如果书包容量不允许，已经不能放i物品了
                dp[j] = dp[j]
    return dp[bagweight]

#为什么遍历背包容量的时候要倒序遍历？
#因为根据二维数组时的递推公式，dp[i][j]需要根据dp[i-1]和dp[i-1][j-weight[i]]决定
#其实就是上一行正上方和左上方
#如果从左遍历到右，左边的数组先更新了，右边数组更新要涉及自己本身值和左边值。
#左边的那个值就是已经遍历过的了
#但是如果从右边往左遍历，设计本身值和左边值的时候，这个左边值是没遍历过的，才符合逻辑

if __name__ == "__main__":
    weight = [1,3,4]
    value = [15,20,30]
    bagweight = 4
    result = test_1_wei_bag_problem(weight, value, bagweight)
    print(result)
    
    
    
    
