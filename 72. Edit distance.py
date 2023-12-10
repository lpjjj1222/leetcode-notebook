class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #其实不一定只对word1操作，因为处理word2其实就是word1的逆向操作是一样的。
        #这里刚好利用了这一点，本来word1有增删替，这里把Word1的增看作word2的减
        #所以一共三种操作：word1减   word2减   word1替   
        #dp数组的含义： 长度为i以i-1结尾的字符串word1,长度为j以j-1结尾的字符串word2，弄成相同的样子，需要的最少操作次数为dp[i][j]

        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        print(dp)

        #初始化:从递推公式看出dp由左边，上边，左上边的数推出来的，所以要初始化第一行第一列
        for i in range(len(word1)+1):#当word1长度为0时，word2有多长就删多少个
            print(i)
            dp[i][0]  = i
        for j in range(len(word2)+1):
            dp[0][j] = j

        #递推公式
        #长度为i的word1和j的word2 先对比结尾的word1[i-1]和word2[j-1]，从结尾往前对比
        #word1减： dp[i-1][j] + 1
        #word2减： dp[i][j-1] + 1
        #word1替： dp[i-1][j-1] + 1
        for i in range(1, len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[len(word1)][len(word2)]

        
