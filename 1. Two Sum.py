class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping={}
        res=[]
        
        #把遍历过的数放在字典里
        #要找的话直接in

        for i,n in enumerate(nums):
            if (target-n) in mapping.keys():
                res.append(i)
                res.append(mapping[target-n])
                return res
            else:
                mapping[n] = i
