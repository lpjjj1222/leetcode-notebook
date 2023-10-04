#step1:如果k还有的话，把负数都取反变成正数 （优先取反绝对值大的）
#step2:如果k还有的话，如果是奇数，就用所有k取反绝对值最小的正数（损失最小），偶数的话直接就是当前的结果

#因此我们应该按照绝对值对nums进行排序
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key = lambda x: abs(x), reverse= True)
        index = 0
        print(nums)
        #step 1:
        while index < len(nums) and k > 0:
            print(nums[index])
            if nums[index] <0:
                nums[index] = nums[index] * (-1)
                k -= 1
            index += 1
                
        #step 2:
        if k <= 0:
            return sum(nums)
        else:
            if k % 2 == 1:
                nums[-1] = nums[-1] * (-1)
                return sum(nums)
            else:
                return sum(nums)
        
        


        
        
