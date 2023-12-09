class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #因为排好序了，用双指针
        left = 0
        right = len(numbers)-1

        while left < right:
            sumup = numbers[left]+numbers[right]
            if  sumup == target:
                return [left+1,right+1]
            elif sumup > target:
                right -= 1
            else:
                left += 1
        

        
