#字典
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        num_dict = dict(collections.Counter(nums))
        for num, frequency in num_dict.items():
            if frequency > len(nums)/3:
                result.append(num)
        return result
'''

#
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #设两个候选，两个计数器。因为数组里最多有两个数符合 频率大于三分之一，因为第三个数肯定小于三分之一
        #如果遍历到的数是其中一个候选，则该候选计数器+1，另一个候选计数器不变。
        #如果遍历到的数不是候选的任意一个，则两个计数器都-1
        result = []
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
          
        #遍历投票完后，剩下的候选人未必都能满足频率大于三分之一，例如[3,2,3],2的次数1次并没有大于1次
        if nums.count(candidate1) > len(nums)/3:
            result.append(candidate1)
        if nums.count(candidate2) > len(nums)/3:
            result.append(candidate2)
        return result
  

            

                    


        
