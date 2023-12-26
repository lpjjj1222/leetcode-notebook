class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        #两个集合相减-取差集
        nums1 = list(nums1_set-nums2_set)
        nums2 = list(nums2_set-nums1_set)
        return[nums1,nums2]


        
