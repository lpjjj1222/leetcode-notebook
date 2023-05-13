class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        for n in nums1:
            if n in set(nums2):
                result.add(n)
        return result
