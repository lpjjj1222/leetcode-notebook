class Solution:
    def reverseStr(self, s: str, k: int) -> str:
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

            
            


        
        
    
    
    
    
    
    
 
    

            

        
