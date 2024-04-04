class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        print(prefix)
        for i, p in enumerate(prefix):
            if p - nums[i] == prefix[-1] - p:
                return i
        return -1
            
        
