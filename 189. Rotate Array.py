class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        def reverse(start,end):
            while start < end:
                nums[start],nums[end] = nums[end], nums[start]
                start , end = start + 1, end - 1
        reverse(0,n-1) #整个翻转
        reverse(0,k-1) #翻转前一半
        reverse(k,n-1) #翻转后一半


        