#这道题看到代码随想录的单调有平坡解释完有什么要考虑的特殊情况就行了
#不用跟着他说的解决特殊情况的方法解决
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        result = 1 
        prediff = 0
        curdiff = 0
        
        for i in range(0, len(nums)-1):
            curdiff = nums[i+1] - nums[i]
            if prediff * curdiff <=0 and curdiff != 0: #curdiff != 0 是为了让平坡的时候不算摆动
                result += 1
                prediff = curdiff #只有出现摆动的时候，pre才会跟着cur
        return result
            
       
