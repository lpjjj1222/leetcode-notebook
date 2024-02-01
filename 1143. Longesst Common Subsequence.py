class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_1 = len(text1)
        len_2 = len(text2)

        if len_2 == 0:
            return 0

        dp = [[0] * (len_1+1) for i in range(len_2+1)]

        for i , c in enumerate(text2):
            for j , d in enumerate(text1):
                dp[i+1][j+1] = dp[i][j]+1 if c == d else max(dp[i+1][j],dp[i][j+1])
        return dp[-1][-1]



        
        
