class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        mapping_12 = {}
        res = 0
        for n in nums1:
            for nn in nums2:
                sumup = n + nn
                if sumup not in mapping_12.keys():
                    mapping_12[sumup] = 1
                else:
                    mapping_12[sumup] += 1

        for nnn in nums3:
            for nnnn in nums4:
                if (0-nnn-nnnn) in mapping_12.keys():
                    res += mapping_12[0-nnn-nnnn]
        
        return res
                    
