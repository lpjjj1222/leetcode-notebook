class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = 0
        vowels = set(['a','e','i','o','u'])
        for index in range(k):
            if s[index] in vowels:
                window += 1
        res = window
        
        index += 1
        while index < len(s):
            if s[index] in vowels:
                window += 1
            if s[index-k] in vowels:
                window -= 1
            res = max(res,window)
            index += 1
        return res
            


        
