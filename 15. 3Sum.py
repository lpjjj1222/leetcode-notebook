def solutions(nums):
        #先将数组进行排列
        #第三个指针从最左边开始，找另外两个指针能否让和+第三个指针=0
        #转变成双指针题目
        #left 和 right安排在第三个指针右边，left从最左开始，right从最右开始
        #根据三指针之和大于还是小于0，决定移动left还是right
        #如果大于0，说明大了，则right向左，如果小于0，说明小了，则left向右
        
    result = []
    
        #排序
    nums = sorted(nums)
    
        #移动指针
    for i3 in range(len(nums)-2):
        if i3 >0 and nums[i3] == nums[i3-1]:
            continue

        left_start = i3+1
        right_start = len(nums)-1
        while left_start < right_start:

            third = nums[i3]

            left = nums[left_start]

            right = nums[right_start]

            if third + left + right > 0:
                right_start -= 1
            elif third + left + right <0:
                left_start += 1
            else:
                triple = [third,left,right]
                result.append(triple)
                #如果已经找到left + right匹配，则两个指针同时向中间移动一格，然后继续原来的判断
                #判断左指针是否还能右移或者右指针是否还能左移
                if left_start + 1 < (len(nums)-2) and (right_start -1) > 1:
                    left_start += 1
                    right_start -= 1
                    while nums[left_start]==left and nums[right_start]==right:
                        if left_start<right_start: 
                            left_start += 1
                            right_start -= 1
                        else:
                            break
                #如果不能，直接出While循环
                else:
                    break
        
                        
    
    return result

    
            

            
    
