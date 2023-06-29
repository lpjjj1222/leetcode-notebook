def solutions(nums,val):
    #用快慢双指针不占用额外空间，直接in-place修改
    
    #slow_i用于指示新数组的下标，一步步前进
    #fast_i 去看是否符合新数组元素的要求，即不是val的元素
    #fast_i如果检测到符合要求的，就把符合要求的元素在slow_i指示的位置填上去
    #如果不符合，就不填，fast_i继续往下走
    
    slow_i, fast_i = 0, 0
    size = len(nums)
    
    while fast_i < size:
        #print('*********')
        #print('fast_i',fast_i,'fast',nums[fast_i])
        #print('slow_i',slow_i,'slow',nums[slow_i])
        
        if nums[fast_i] != val:
            #print('符合要求')
            nums[slow_i] = nums[fast_i]
            slow_i += 1
        fast_i += 1
        #print('改完：',nums)
    

 
    return slow_i


        

        
    
    
