class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m-1, n-1
        p = len(nums1)-1
        for p in range(len(nums1)-1,-1,-1):
            if p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[p] = nums1[p1]
                    p1 -=1
                elif nums1[p1] <= nums2[p2]:
                    nums1[p] = nums2[p2]
                    p2 -=1
            elif p1 < 0:
                nums1[p] = nums2[p2]
                p2 -=1
            elif p2 < 0:
                nums1[p] = nums1[p1]
                p1 -=1
        


        