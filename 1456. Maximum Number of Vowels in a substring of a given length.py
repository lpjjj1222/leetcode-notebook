class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        res = 0
        cur_vow = 0
        
        for i,n in enumerate(s):
            if i >= k: #先判断是否是初始窗口之外的数
                if s[i - k] in vowels:
                    cur_vow -= 1
                
            if n in vowels:
                cur_vow += 1
                
            res = max(cur_vow,res)
        return res
