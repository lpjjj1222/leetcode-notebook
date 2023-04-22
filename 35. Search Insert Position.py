def solutions(nums,target):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target: #[2,3,4,5,6] mid = 4 target = 5 则[5,6]
            left = mid + 1
        else: #[2,3,4,5,6] mid = 4 target = 3 则[2,3]
            right = mid - 1
            
    if nums[left] < target: #大多数时候比如说example 1和example 2，出循环的时候都是
    #right = left 跳出循环，in this case,用right或者left都可以
    #However, 当出现例如[1,3,] target = 0 时， right在循环中会被赋值mid - 1
    #这样的话right会成为一个负数， 而left在循环中只会+1，所以用left代替right 做判断可以避免这种情况
        return left + 1
    else:
        return left
