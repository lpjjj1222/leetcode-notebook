class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #长度小的尽量先遍历
        strs = sorted(strs, key = lambda x: len(x))
        
        #明确dp数组的含义：由于背包容量是二维的，所以定义滚动二维数组或者三维数组instead of 滚动一维数组和二维数组。
        #dp[i][j]指的是将物品放到容量为i，j的背包中，能放的最大物品数
        #对滚动一维数组，dp[j] = max(dp[j],dp[j-weight[i]+value[i]]),先遍历物品后遍历背包，背包倒序遍历，因为每个物品只能选一次
        #因此对于滚动二维数组，dp[i][j] = max(dp[i][j], dp[i-x][j-y]+1)，其中x是遍历到的物品的0的个数，y是1的个数
        
        #创建并初始化dp数组
        dp = [[0] * (n+1) for _ in range(m+1)]
        #dp[0][0]肯定是0，非0下标的dp数组由于之后要放进max()里比较，也初始化为0

        for str in strs:
            for i in range(m,-1,-1):
                for j in range(n,-1,-1):
                    x = str.count('0')
                    y = str.count('1')
                    if x <= i and y <= j:#如果书包容量允许
                        dp[i][j] = max(dp[i][j],dp[i-x][j-y] + 1)
                    #如果书包容量不允许，则不变
        return dp[m][n]

                    
              
            
        
