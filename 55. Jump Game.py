#看代码随想录- -
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
           return True

        index, cover = 0 , 0 
        while index <= cover:
            cover = max(cover, index + nums[index])
            if cover >= len(nums) -1:
                return True
            index += 1
        return False
        
