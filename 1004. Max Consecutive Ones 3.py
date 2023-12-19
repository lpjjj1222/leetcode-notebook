#双指针+滑动窗口,右指针用于扩大窗口，左指针用于缩小窗口
#一点点增大窗口，当窗口内0的个数超过k的时候缩小窗口
#由于记录的是最大的窗口长度，所以仅仅在增大窗口的时候更新窗口长度
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        right=left=window_size=count_zero=0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                count_zero += 1
                while count_zero > k:
                    left+=1
                    if nums[left-1] == 0:
                        count_zero -= 1
            window_size = max(window_size,right-left+1)
        return window_size
            

        
