class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        n, m = len(str1), len(str2)

        def is_valid(k): #长度为k的string
            if n % k != 0 or m % k != 0:
                return False
            factor_1, factor_2 = n // k, m // k
            if factor_1 * str1[:k] == str1 and factor_2 * str1[:k] == str2:
                return str1[:k]
            return False
        
        for k in range(1,min(n,m)+1,1):
            if is_valid(k):
                res = is_valid(k)
        return res


                
            
                          

