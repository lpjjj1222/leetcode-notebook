class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sdic = dict()
        tdic = dict()
        ss = []
        tt = []

        i = 0 #跟踪新出现的letter
        for letter in s:
            if letter in sdic: #如果已经有初始index
                ss.append(sdic[letter])
            else:
                ss.append(i)
                sdic[letter] = i
                i += 1
        
        i = 0
        for letter in t:
            if letter in tdic:
                tt.append(tdic[letter])
            else:
                tt.append(i)
                tdic[letter] = i
                i += 1
        return tt == ss
                


        
