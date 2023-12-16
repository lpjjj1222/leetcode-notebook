'''
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res= []
        for i,num in enumerate(nums):
            if num == target:
                res.append(i)
        return res
'''
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        start = count = 0
        for num in nums:
            start += num < target
            count += num == target
        return list(range(start,start+count))


        

        
