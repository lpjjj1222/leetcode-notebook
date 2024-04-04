class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        vow = ['a','e','i','o','u']
        left, right = 0 , 0
        s = list(s)
        count = 0
        for right in range(len(s)):
            if right >= k:
                # 左边界收缩
                if s[left] in vow:
                    count -= 1
                left += 1
            # 右边界扩张
            if s[right] in  vow:
                count += 1
            res = max(res,count)
        return res

            


        
