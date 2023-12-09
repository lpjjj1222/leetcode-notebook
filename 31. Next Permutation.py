class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #找pivot_point 并定位
        pivot_index = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                pivot_point = nums[i-1]
                pivot_index = i-1
                break
        if pivot_index == -1:
            return nums.sort()
        else:
            print(pivot_index)

        
        #遍历pivot_point右边的数，找到能够大于pivot_point的最小值
        pivot_right_valid_min = float('inf')
        for right_i in range(pivot_index+1, len(nums)):
            if nums[right_i] > pivot_point:
                if nums[right_i] < pivot_right_valid_min:
                    pivot_right_valid_min = nums[right_i]
                    valid_min_i = right_i

        
        #用这个大于pivot_point的最小值跟pivot_point换
        nums[pivot_index], nums[valid_min_i] = pivot_right_valid_min, pivot_point

        #pivot_point右边的数字从小到大排列
        nums[pivot_index+1:] = sorted(nums[pivot_index+1:])
        
        return nums


        


        
    
            

        
