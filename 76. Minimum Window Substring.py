class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_length = float('inf')
        res = ""
        #滑动窗口 先找到t里的所有字母 然后开始收缩窗口
        #用required和formed两个变量记录满足了要求的字符种类
        dic = Counter(t) 
        required = len(dic)  #t里需要有多少种字符种类
        l , r = 0, 0
        formed = 0 #window里已经满足的字符种类数

        dics = defaultdict(int)

        ans = (float('inf'), None, None) #window长度，left, right


        while r < len(s):
            letter = s[r]
            dics[letter] += 1
            if letter in dic and dic[letter] == dics[letter]:
                formed += 1
            
            #如果条件已经全部满足，则推左边界缩小窗口。缩小至不满足后，推右边界扩张窗口
            while l <= r and formed == required:
                letter = s[l]
                if r-l+1 < ans[0]:
                    ans = (r-l+1,l,r)
                dics[letter] -= 1
                if letter in dic and dic[letter] > dics[letter]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
        
                
