class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        result = []
        for i, num in enumerate(nums):
            if not num_dict or (target-num) not in num_dict:#如果字典空或者字典里找不到匹配的值
                num_dict[num] = i#将当前值放进字典里
            else:
                result.append(i)
                result.append(nums.index(target-num))
                break
        return result
            

            
        
