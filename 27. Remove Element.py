class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #fast遍历element
        #slow写数
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] == val:
                continue
            else:
                nums[slow] = nums[fast]
                slow += 1
        return slow

        
