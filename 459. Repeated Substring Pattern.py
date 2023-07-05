def solutions(s):
    def getNext(next, s):
        j = -1
        next[0] = j
        for i in range(1, len(s)):
            while j >= 0 and s[i] != s[j+1]:
                j = next[j]
            if s[i] == s[j+1]:
                j += 1
            next[i] = j
        #print(next)
        

    next = [0] * len(s)
        
    getNext(next,s)
    
    if next[len(s)-1] >= 0:#有最长相等字符串 （减1版本，所以才是大于等于）
        length_of_longest = next[len(s)-1] + 1
        minimal_repeated_string = len(s) - length_of_longest
    else:
        return False
    
    if len(s)%minimal_repeated_string ==0:
        return True
    else:
        return False


    
    
