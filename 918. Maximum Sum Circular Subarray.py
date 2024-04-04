
        #题目限制，即使子序列跨越了末尾去到开头，也不能重复考虑原有数组的数
        #1:最大和出现在非环形子数组（不跨越末尾开头) - 同leetcode53
        #2:最大和出现在环形子数组（跨越末尾开头）-找非环形子数组的最小和，然后用总的和减去最小和
        #edge case:如果nums全是负数，那么答案只能是某一个单独的值，因为再加入其他的负数只能变得更小，所以不用考虑是否跨越末尾开头
        
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #edge case: all below zero

        # non-circular maximum
        total_max = 0
        total_min = 0
        nc_max = float('-inf')
        nc_min = float('inf')
        sumup = 0
        all_below_zero = True
        max_num = float('-inf')
        for n in nums:
            if n >= 0:
                all_below_zero = False
            max_num = max(max_num,n)
            sumup += n
            total_max = max(total_max + n, n)
            total_min = min(total_min + n, n)
            nc_max = max(nc_max, total_max)
            nc_min = min(nc_min, total_min)
        # circular maximum = sum - non-circular minimum
        c_max = sumup - nc_min
        if all_below_zero:
            return max_num
        return max(c_max, nc_max)

        

        

        
