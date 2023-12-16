class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:

        #STEP1:从后往前遍历正序递增的数放进栈里，这样栈顶就是最后面较小的数(的index)，如果符合要求，再看栈下一个更大的数...
        n = len(nums)
        stack = []
        for i in range(n-1, -1, -1):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        #STEP2: 从前往后遍历，每一个先对比栈顶的元素看是否比栈顶大，如果是，就有了符合要求的子数组
        #一定会找到比栈顶大的子数组，否则STEP1里就会把所有元素放进栈，STEP1是遇到比栈顶大的才停止入栈的
        r = 0 #用于记录目前最长的符合要求的长度
        m = float('-inf') #用于记录目前遍历到的最大数
        for i in range(n):
            #如果已经遍历到放入栈里的元素的index:
        
            while stack and i >= stack[-1]:
                stack.pop()

            #更新最大值
            if nums[i] > m:
                m = nums[i]

            
                while stack and m > nums[stack[-1]]:
                    r = max(r, stack[-1]-i+1)
                    stack.pop()
                    #栈顶变成大一点的值
        return r
        
            







        
