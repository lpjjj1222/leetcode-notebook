def solutions(nums,target):
    left = 0
    right = len(nums) - 1
    
   
    
    while left <= right:
        mid = (left + right) // 2 #用 // 就不用区分双数单数了 都可以得到中位数
        print('进入循环***************')
        print('mid=',mid)
        print('left=',left)
        print('right=',right)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:  #nums[mid] = 8 target = 2,  [2,4,6,8,10,12,14] - [2,4,6]
            print('mid<target')
            left = mid + 1
        else: #nums[mid] = 8 target = 12,  [2,4,6,8,10,12,14] - [10,12,14]
            print('mid>target')
            right = mid - 1 
            
        print('left=',left,'right=',right)
            
    return -1
