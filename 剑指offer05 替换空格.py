def solutions(s):
    #因为数组是连续存储的
    #所以一般扩充数组的题目都是采用以下步骤
    #step1:扩容数组到需要的大小
    #step2:从后往前一步步插入元素
    #（不从前往后是因为如果从前面插入，后面的元素就要因为前面插入了元素而移动）
    
    #数空格个数
    count_space = 0
    s = list(s)
    s_m = list(s)
    for letter in s:
        if letter == ' ':
            count_space += 1
            
    #扩容数组        
    need_to_add = count_space * 2
    
    for _ in range (need_to_add):
        s_m.append('')
        
        
    #从前往后一步步插入元素    
    step = 1 #%20 #0 2 %
    
    for letter in reversed(s):
        if letter != ' ':
            s_m[-step] = letter
            step += 1
        else:
            s_m[-step] = '0'
            s_m[-(step+1)] = '2'
            s_m[-(step+2)] = '%'
            step +=3
    
    #将list转换回string
    s_m = ''.join(letter for letter in s_m)
    return s_m
    
