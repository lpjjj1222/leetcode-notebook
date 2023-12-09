class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        #当有一个字典，且key不存在时希望值为0时就用collections.defaultdict
        #特别是用字典计数的时候，要初始值为0，一个个+1时

        num_dict = collections.defaultdict(int)
        count = 0

        for i in nums1:
            for j in nums2:
                num_dict[i+j] += 1 #记录该nums1+nums2出现的次数
        
        for n in nums3:
            for m in nums4:
                count += num_dict.get(-(n+m), 0)
        
        return count


        
        
