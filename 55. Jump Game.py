class Solution:
    def canJump(self, nums: List[int]) -> bool:
        terminal = nums[0]
        i = 0
        while i <= terminal:
            #更新目前能到达的最远的地方
            terminal = max(terminal, nums[i] + i)
            if terminal >= len(nums)-1:
                return True
            i += 1
        return False
            

        
        
