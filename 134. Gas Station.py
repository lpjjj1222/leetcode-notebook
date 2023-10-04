#看代码随想录（要看到质疑的点，并且消除质疑的方法）
#总的来说就是，currentsum 累加前面的和，如果和小于零，说明前面的任何一个点都不能作为起始点，要从后面一个点开始作为起点判断

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        startIndex = 0 #这里的start不是表示遍历的起点而是车出发的起点
        curSum = 0
        totalSum = 0 #totalSum是能跑完一圈的最基本条件，如果所有的和加起来<0, 根本不可能跑完全部
        #curSum遇到负数要归零重新计算，totalSum一直累加
        

        for index in range(len(gas)):
            thisStop = gas[index] - cost[index]
            curSum += thisStop
            totalSum += thisStop
            if curSum < 0:
                startIndex = index + 1
                curSum = 0

        if totalSum < 0:
            return -1
        else:
            return startIndex


        
        
