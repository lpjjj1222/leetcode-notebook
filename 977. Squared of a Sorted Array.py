class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #由于本来数组有序，且平方之后的最大值一定在数组的两端
        #要么最左要么最右
        #因此要想到用双指针

        res = [-1] * len(nums) #创建一个跟原始数组一样长度的list
        l = 0
        r = len(nums) - 1
        res_index = len(nums) - 1 #因为要从数组的最后添加元素而不是从最开始，因此不能用append，只能通过用index指定插入位置

        while l <=r :
            print('l',l)
            print('r',r)
            right = nums[r] * nums[r]
            left = nums[l] * nums[l]

            if right > left :
                res[res_index] = right
                r -= 1
            else:
                res[res_index] = left
                l += 1
                
            res_index -= 1
            
        return res
