class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #先排序后双指针
        #第三指针从0开始遍历， left在第三指针邻右， right在最左
        #跳过第三指针用过的数值
        result = []
        pointer = 0
        nums.sort()

        while pointer < len(nums)-2 and nums[pointer] <= 0:
            if pointer == 0 or nums[pointer] != nums[pointer-1]:
                self.twoSum(pointer, nums, result)
            pointer += 1
        return result

    def twoSum(self, pointer: int, nums: List[int], result:List[int]) -> List[List[int]]:
        left, right = pointer+1, len(nums)-1
        while left < right:
            sumup = nums[pointer] + nums[left] + nums[right]
            if sumup > 0:#如果大了，right往左
                prev_right = right
                right -= 1
            elif sumup < 0: #如果小了，left往右
                left += 1
            else: #如果刚好
                result.append([nums[pointer], nums[left],nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left]==nums[left-1]:
                    left += 1




        


        
