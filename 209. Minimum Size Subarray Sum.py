def solutions(nums,s):
    window_start = 0
    min_size = float('inf') 
    summation = 0
    #这一步是初始化最小窗口长度为无穷大，这样的话，
    #第一个得到的窗口长度肯定小于这个无穷大，在做min()比较之后就可以被更新

    for window_end, number in enumerate(nums):  #enumerate(list)返回的是index,number
        summation += number

        while summation >= s:
            min_size = min(min_size,window_end - window_start + 1) #更新目前满足条件的最小窗口长度
            summation -= nums[window_start]  #满足条件之后把窗口的最左边拿掉，看是否还满足，如满足，进入While循环那最小窗口长度又可以少1了！
            #如果不满足，就向右滑动，for循环会给window_end + 1
            window_start += 1
            
    if min_size == float('inf'):
        return 0
    else:
        return min_size
        
    
        
    
    
    
