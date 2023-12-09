#双指针+集合
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        word_set = set()
        
        for right in range(len(s)):
            if s[right] not in word_set:
                word_set.add(s[right])
                maxLength = max(maxLength, right-left+1)
            else:
                #如果右边的已经在前面出现，就把左边界往右推,推到不重复为止
                while s[right] in word_set:
                    word_set.remove(s[left])
                    left += 1
                maxLength = max(maxLength, right-left+1)
                word_set.add(s[right])
        return maxLength
'''

#双指针+字典
class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        maxLength = 0
        left = 0
        word_dict = {}
        #字典key是letter, value是该letter最后出现的index位置

        for right in range(len(s)):
            if s[right] not in  word_dict:
                word_dict[s[right]]= right
                maxLength = max(maxLength, right-left+1)
            else:
                #左指针移到最后出现该letter的位置的后一个（这就保证了不会再重复该letter)
                #但如果是abba,right = 3时，left之前在2,由于a重复了，b要不要移到第一个a的后面呢？
                #不！left只往右推！
                if word_dict[s[right]] >= left:
                    left = word_dict[s[right]] + 1
                #更新最后出现的位置
                word_dict[s[right]] = right
                maxLength = max(maxLength, right-left+1)
        return maxLength





                


        
        
