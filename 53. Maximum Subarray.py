#关键点就是 前面的和如果是负数，在加下一个数之前，要把前面的和抛弃掉，不然会被拖累
#另外一点就是，为何让大于0的和加负数？因为这个负数后面可能要很大的正数可以把整体的和提升
#这样的话我们就要引入temporary_max来keep track of 目前最大的和
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        temporary_max = float('-inf')

        for i in nums:
            total += i
            temporary_max = max(total,temporary_max)
            if total < 0: #前面的和是负数肯定会拖累后面的数，还不如重置
                total = 0
        return temporary_max
        
