class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        index = -1 #遍历word的index 从-1开始是因为如果一开始abbr是字母，会给index先加1再判断，如果abbr是数字，直接计算数字，加index。例如一开始数字是2，那么-1+2=1,匹配长度为2之后到达index为1的位置
        endOfIndex = len(word) - 1
        count = 0
        for i, char in enumerate(abbr):
            if char.isdigit():
                #排除leading zeros的情况
                if count == 0 and char == '0':
                    return False
                count = count * 10 + int(char)
                if (i == len(abbr) - 1) or ((i+1 in range(len(abbr))) and (not abbr[i+1].isdigit())):
                #如果后面没了或者后面不是数字,就开始匹配长度为count的word
                    #匹配前面数字决定的长度
                    index += count
                    #将count归回0
                    count = 0
                    #看走完那么长之后会不会超出界限
                    if index > endOfIndex:
                        return False
            else:
                index += 1
                if index > endOfIndex:
                    return False
                elif word[index] != char:
                    return False
        return index == endOfIndex







            
        