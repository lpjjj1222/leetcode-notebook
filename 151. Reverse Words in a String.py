class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        s = [w for w in s if w != ""]

        left = 0
        right = len(s)-1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return " ".join(s)
            

        
        
