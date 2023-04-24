def solutions(matrix,target):
    #先二分法找每一行的第一个数
    #上指针up是在上面的行的第一个数 
    #下指针down是在下面的行的第一个数
    #start表示的是target在matrix的第几行  
    
    up = 0
    down = len(matrix) - 1
    
    
    while up < down and up + 1 != down:
        
        mid = (up + down) // 2
        if matrix[mid][0] > target:
            down = mid

        elif matrix[mid][0] < target:
            up = mid
        else:
            return True
            
           
    if target > matrix[down][0]:
        start = down
    elif target < matrix[down][0]:
        start = up
    else:
        return True
    
    
#上面的语句执行完就能确定start,start是用来确定target在matrix的第几行

    if target in matrix[start]:
        return True
    else:
        return False
    
