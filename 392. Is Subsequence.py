class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_s = 0
        index_t = 0
        if not s:
            return True
        while index_t < len(t) and index_s < len(s):
            if t[index_t] == s[index_s]:
                index_s+=1
                index_t+=1
            else:
                index_t+=1
        return index_s == len(s)
        
