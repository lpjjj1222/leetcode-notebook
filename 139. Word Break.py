#这题二维数组真搞不出来....只能看代码随想录咯
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #s是书包，wordDict里的每个字符串是物品，用字符串把s一部分一部分消掉，意味着用物品将书包填满
        #定义dp数组：dp[j] = True表示长度为j的字符串，可以被成功拆分
        #递推公式：i < j ,如果dp[i]=True,即前i个字符串可以被成功拆分，且s[i,j]是出现在wordDict里的单词，则dp[j] = True
        #初始化dp数组：dp[0] = True,不然如果长度为0就是false,后面全都得是False，非0下标的dp值为False，因为还不知道能否成功拆分
        #遍历顺序：由于递推公式是从左往右凑单词，物品是需要考虑顺序进背包的，因此排列数对应先背包，后物品
        dp = [False] * (len(s)+1)
        dp[0] = True

        for j in range(1,len(dp)): #书包
            for i in range(j): #物品:因为dp[i]为前面的string，s[i:j]为剩下的String
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    break #目前遍历的容量为j的书包就搞定了，break之后继续j++遍历

        return dp[len(s)]
                

        

        

        
