class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        pointer_1 = 0
        nums.sort()

        for pointer_1 in range(len(nums)-3):
            if pointer_1 == 0 or nums[pointer_1] != nums[pointer_1-1]:
                for pointer_2 in range(pointer_1+1, len(nums)-2):
                    if pointer_2 - pointer_1 >1 and nums[pointer_2] == nums[pointer_2-1]:
                        continue
                    else:
                        self.twoSum(nums, pointer_1, pointer_2, result, target)
        return result
    
    def twoSum(self, nums: List[int], pointer_1:int, pointer_2:int, result: List[int], target:int):
        left = pointer_2 + 1
        right = len(nums)-1
        while left < right:
            sumup = nums[pointer_1] + nums[pointer_2] + nums[left] + nums[right]
            if sumup > target: #如果大了, right向左
                right -= 1
            elif sumup < target: #如果小了，left向右
                left += 1
            else: #如果刚好
                result.append([nums[pointer_1],nums[pointer_2],nums[left],nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            
            




            
        
