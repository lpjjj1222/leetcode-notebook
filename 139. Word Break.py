class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #wordDict里面的每个string都是一个物品模型，物品是s的子串，如果子串跟模型一样，就能放进书包
        #由于要求子串是否在wordDict里，应该把list wordDict转化为set,因为判断元素是否在list里的时间复杂度是O(N),set是O(1)
        wordDict = set(wordDict)
        #问题转化为：能否按照某个顺序把物品放进背包，把背包填满
        #由于wordDict里的string可以重复利用所以是完全背包问题
        #转化为排列数问题：for循环先背包后物品
        #dp数组的含义是：如果选物品能够将容量为j的背包填满，则dp[j] = True
        #递推公式：长度为j的string, 假设已经从前到后遍历到长度i，如果能够确定前面的字符串可以搞定，后面只剩s[i,j],且s[i,j]能够在wordDict找到，则整个长度为j的字符串都可以搞定。
        #因此，递推公式为dp[i] = True 且 dp[j-i]=True, dp[j] = True

        dp = [False] * (len(s)+1)
        #根据递推公式初始化，由于“且”，递推公式的开头dp[0]如果是False 后面就全部是False了，所以dp[0] = True
        dp[0] = True

        for j in range(1, len(s)+1):
          for i in range(j):  #物品是s[i,j]
            if dp[i]==True and s[i:j] in wordDict:
              dp[j] = True
        return dp[len(s)]


            




        

        




        

        
