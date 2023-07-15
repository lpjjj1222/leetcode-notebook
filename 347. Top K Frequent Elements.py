class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#用哈希法，用字典做一个频率表，key是元素，value是频率，对字典根据值进行排序，返回前k个
        def frequency_hash(nums):
            dic = dict()

            for i in range(len(nums)):
                if nums[i] not in dic:
                    dic[nums[i]]= 1
                else:
                    dic[nums[i]]+= 1
            #对字典根据值进行排序
            sorted_dic = sorted(dic.items(),key = lambda x:x[1],reverse=True)
            return sorted_dic

        result = []
        frequency = frequency_hash(nums)
        for i in range(k):
            result.append(frequency[i][0])
        return result


        
