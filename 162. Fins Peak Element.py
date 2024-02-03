class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #先看中间，如果这个数比右边邻居小，则右边必存在峰值
        #如果这个数比左边邻居小，则左边必存在峰值
        #如果这个数既不比右边小也不比左边小，则该数为峰值
        left = 0
        right = len(nums)-1
        res = 0
        if len(nums)==1:
            return 0
        while left <= right:
            mid = left + (right - left) // 2
            if mid == 0:
                if nums[0] > nums[1]:
                    res = 0
                    break
                else:
                    res = 1
                    break
            elif mid == len(nums)-1:
                if nums[mid] > nums[mid-1]:
                    res = mid
                    break
                else:
                    res = mid-1
                    break
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            elif nums[mid] < nums[mid-1]:
                right = mid - 1
            else:
                res =mid
                break
        return res
        

        
