class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        intervals.sort(key = lambda x: x[1])
        intervals.sort(key = lambda x: x[0])


        right_end = intervals[0][1] #将right_end初始化为第一个区间的右边界
        left_end = intervals[0][0] #将left_end初始化为第一个区间的左边界
        for index in range(len(intervals)):
            if index > 0:
                #如果之前的right_end大于等于当前左边界，则重叠
                if right_end >= intervals[index][0]:
                    right_end = max(right_end,intervals[index][1])
                #如果遇到一个区间，跟上一个区间没有重叠了，那么就可以把上一个区间的结果添加到result
                #并且更新left_end为当前区间的左边界，right_end为当前区间的右边界
                else:
                    result.append([left_end,right_end])
                    left_end = intervals[index][0]
                    right_end = intervals[index][1]
        result.append([left_end,right_end])
        return result
        
