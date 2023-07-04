class Solution:
    #这题暴力算法很简单，但是KMP算法很难tmd
    #KMP算法 （看代码随想录视频）
    #haystack = 'sadbutsad'
    #needle = 'sad'
    #前缀：不包含最后一个字符，所有以第一个字符开头的字符串
    #后缀：不包含第一个字符，所有以最后一个字符结尾的字符串
    
    
    
    #寻找最长相等前后缀即寻找next数组
    #'aabaaf' 'baaba'
    #减1的版本，移动的指针分别是i和j+1
    def getNext(self, next, s):
        j = -1
        next[0] = j
        for i in range(1, len(s)):
            while j >= 0 and s[i] != s[j+1]:
                j = next[j]
            if s[i] == s[j+1]:
                j += 1
            next[i] = j
 
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        j = -1
        for i in range(len(haystack)):
            while j >= 0 and haystack[i] != needle[j+1]:
                j = next[j]
            if haystack[i] == needle[j+1]:
                j += 1
            if j == len(needle) - 1:
                return i - len(needle) + 1
        return -1
