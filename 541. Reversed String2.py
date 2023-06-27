class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #总体关键思路：
        #range(start, end ,step) 表示的是始末点和步长 
        #在这一题Start和end设为s的始末，step设为2k
        #for循环，就可以找到每次要替换部分的起始字母
        
        
        if len(s)<2:
            return s
        
        
        
        #结果
        concatenate = ''
        
        #把s化成list
        s = list(s)
        
        #自定义替换function
        def reverse(string):
            left_i = 0
            right_i = len(string) - 1
            while left_i < right_i:
                string[left_i],string[right_i] = string[right_i],string[left_i]
                left_i += 1
                right_i -= 1
            return string
        
        for rev_start in range(0, len(s)-1, 2*k):
            reverse_part = reverse(s[rev_start:rev_start + k])
            back_part = s[rev_start + k: rev_start + 2*k]

            reverse_part = ''.join(letter for letter in reverse_part)
            back_part = ''.join(letter for letter in back_part)
            concatenate = concatenate+reverse_part
            #print('还没加后面部分：',concatenate)
            #print('后面部分：',back_part)
            if back_part:
                concatenate = concatenate + back_part

        remain_length = len(s) - len(concatenate)
        #print('remain_length:',remain_length)
        if remain_length >0:
            remain = s[-remain_length:]
            remain = ''.join(letter for letter in remain)
            concatenate = concatenate + remain
                

                
        return concatenate
    
        
    














        '''
        #我的解法，切割成长度为2k的小串
        list_s = []
        list_m = []
        
        #分割字符串 每个长度2k
        while s:
            string = s[:2*k]
            s = s[2*k:]
            list_s.append(string)
        #print('分割完',list_s)
        
        
        #对每个小串 swap using 双指针
        for string in list_s:
            string = list(string)
            left_i = 0
            #对长度不满k的小串，
            if len(string)<k:
                right_i = len(string)-1
            else:
                right_i = k-1 #确保右指针从第k个开始向左走
            
            while left_i < right_i:
                string[left_i], string[right_i] = string[right_i], string[left_i]
                left_i += 1
                right_i -= 1
            
            #print('swap完',string)
            
            #将swap完的小串放回一个新列表，因为swap的时候转成了list，所以要把list连成字符串再放进新列表里
            result = ''.join(str(letter) for letter in string)
            list_m.append(result)
            
        #print(list_m)
        
        result = ''.join(str(split_string) for split_string in list_m)
        return result 
        '''
            
            


        
        
    
    
    
    
    
    
 
    

            

        
