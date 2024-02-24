class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        res = []
        start = 0
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i] == nums[i+1]-1:
                continue
            else:
                if i == start:
                    res.append(str(nums[i]))
                    start = i+1
                else:
                    res.append("->".join([str(nums[start]),str(nums[i])]))
                    start = i+1
        return res

            
        
