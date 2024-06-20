class Solution:
    def romanToInt(self, s: str) -> int:
        dic = dict({'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000})
        res = 0
        stk = list(s)
        prev = 0
        while stk:
            num = dic[stk.pop()]
            if num < prev:
                res -= num
            else:
                res += num
            prev = num
        return res
        