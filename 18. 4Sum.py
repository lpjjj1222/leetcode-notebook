class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        #先排序
        nums = sorted(nums)
        #print(nums)


        
        for first_i in range(len(nums)-3):
            #first的for循环
            #print('-------------------first移动',nums[first_i])
            if first_i > 0 and nums[first_i] == nums[first_i-1]:
                #print('XXXXXXXXXXXXXXfirst_i跳过')
                continue
            
            for second_i in range(first_i+1,len(nums)-2):
                #second的for循环
                #print('********************second移动',nums[second_i])
                if second_i >first_i+1 and nums[second_i] == nums[second_i-1]:
                    #print('XXXXXXXXsecond_i跳过')
                    continue
                    
                else:
                    #重置left right指针
                    left_i = second_i+1
                    right_i = len(nums)-1

                    #左右双指针
                    while left_i < right_i:
                        #print('进入双指针循环')
                        first = nums[first_i]
                        second = nums[second_i]
                        left = nums[left_i]
                        right = nums[right_i]
                        
                        #print('first',first,'first_i',first_i)
                        #print('second',second,'second_i',second_i)
                        #print('left',left,'left_i',left_i)
                        #print('right',right,'right_i',right_i)

                        sumup = left+right+first+second
                        #print('&&&&&&&sumup&&&&&&&&&',sumup)
                        if sumup > target:#大了，右边向左
                            right_i -= 1
                        elif sumup < target:#小了，左边向右
                            left_i += 1
                        else: #等于target
                            ok_list = [left,right,second,first]
                            result.append(ok_list)

                            #判断会不会左右各走一步还是原来的相等的两个
                            while nums[right_i-1]== right and nums[left_i+1]==left:
                                #print('左右都还是原来的哦')
                                #确保还有距离各走一步
                                if right_i - left_i >2:
                                    #两边一起走
                                    right_i -= 1
                                    left_i += 1
                                #没有距离走了，即中间只夹着一个数了而且这个数和左右两边都相等
                                else:
                                    right_i = 0
                                    break
                                    
                            #不是相等的两个就左右任意走一个，走右边吧，回到原来的节奏    
                            while nums[right_i-1]==right and right_i - left_i >1:
                                right_i -= 1
                            
                            right_i-=1

        return result
                                    
