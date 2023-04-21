def solutions (nums,target):
    list_for_index = []
    length = len(nums)
    #第一个指针在nums的中位数
    if length % 2 == 0: #双数个 0 1 2 3 4 5
        
        index = int((length / 2) - 1)
    elif length % 2 != 0: #单数个 0 1 2 3 4 
        index = int((length - 1) / 2)
    now = nums[index]
    print('length of nums:',length)
    print('original index:',index)
    print('第一个指针now是：',now)
    print('index = ',index)
    print('now this index list:',list_for_index)
    left = nums
        
    
    #对比now和target
    while index not in list_for_index:
        if len(left) == 1:
            print('缩小到只剩一个的范围了')
            if left[0] == target:
                return index
            else:
                return -1

        
        list_for_index.append(index)
        now = nums[index]
        print('now指针是',now)
        if now == target:
            print('指针就是target')
            return index
        
        else: 
            print('指针不是target')
            #确定下一个循环 猜数的范围
            if now < target:  #  #eg.[2,3,4,5,6] target = 5 now = 4 [4,5,6] 未来的now 5
                range_length = len(left[left.index(now):])
                step = 1
                left = left[left.index(now):]
                print('now',now,' < target',target)
                print('left = ', left)
            elif now > target: #[nums[0]:now]的中位数 #eg.[2,3,4,5,6] target = 2 now = 4 [2,3,4] 未来的now 3
                range_length = len(left[0:left.index(now)]) 
                step = -1
                left = left[0:left.index(now)]
                print('now',now, '> target',target)
                print('left = ', left)
                
            if len(left) == 0: #例如[2,5],target = 0，指针是2，然后由于 now 2 > target 0
                #则left只剩[]
                print('猜数范围...没有范围了')
                return -1

            #确定下一个循环 猜的数（新范围的中位数）
            print('range_length=',range_length)

            if range_length % 2 == 0: #双数个 0 1 2 3 4 5
                diff = range_length / 2
            elif range_length % 2 != 0: #单数个 0 1 2 3 4 
                diff = (range_length - 1) / 2
                
            if diff == 0: #即当range_length =1 时 即猜数的范围只剩1个了
                if left[0] == target:
                    return nums.index(left[0])
                else:
                    return -1

            print('diff=',diff)
    
            
            index += int(diff * step)
            print('***************next_index:************',index)
            print('让我们判断一下进不进下一个循环')
            print('index = ',index)
            print('now ths index list:',list_for_index)
                
        
    if nums[0] == target:
        return index
    else:
        return -1
        
