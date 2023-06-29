def solutions(s,k):
    #这题也可以跟151一样用局部反转+整体反转解决
    
    #'ab cdefg' - 'cdefgab'
    #'ba' 'gfedc'局部反转
    #'cdefgab'整体反转
    
    #拆开两部分
    front = s[:k]
    back = s[k:]
    
    #局部反转
    r_front = list(reversed(front))
    b_front = list(reversed(back))
    
    #合并
    combine = r_front + b_front
    result = list(reversed(combine))
    result = ''.join(letter for letter in result)
    
    return result


    '''
    其实这题本来可以很简单，只是代码随想录要求不占用额外空间才加大了难度
    直接:
    return s[k:] + s[:k]
    就行了
    '''
