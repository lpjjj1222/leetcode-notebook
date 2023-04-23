class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #这道题要想到用二分法
        #因为看例子，如果一个列表里不止一个peak
        #只需要返回其中一个peak的index就行了
        #所以从中间开始往两边找会比较简单
        #因为是比较左右两边跟中间的那个数
        
        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        

        while mid > left and mid < right:
            if max(nums[mid],nums[mid-1],nums[mid+1]) == nums[mid]:
                return mid
            elif nums[mid-1] > nums[mid]:
                mid = mid - 1 
            else:
                mid = mid + 1
                
        if mid == left:
            if nums[mid + 1] < nums[mid]:
                return mid
            else:
                return (mid + 1)
        if mid == right:
            if nums[mid - 1] < nums[mid]:
                return mid
            else:
                reutrn (mid - 1)
