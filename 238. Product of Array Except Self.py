class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_all = 1
        zeros = 0
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                product_all *= n
        if zeros > 1:
            return [0] * len(nums)
        if zeros == 1:
            for i,num in enumerate(nums):
                if num != 0:
                    nums[i] = 0
                else:
                    nums[i] = product_all
        else: #一个0都没有
            for i,num in enumerate(nums):
                nums[i] = product_all // num
        return nums
            
        
