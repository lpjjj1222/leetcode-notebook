class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #先把区间按照左边界进行排序，如果左边界一样，则右边界靠左，即跨度小的，排在前面
        #因此先按照右边界排，再按照左边界排
        intervals.sort(key = lambda x:x[1])
        intervals.sort(key = lambda x:x[0])
        count = 0 #需要删除的区间数
        for index in range(len(intervals)):
            if index > 0:
                #如果上一个左边界大于当前的右边界，则重叠
                if intervals[index-1][1] > intervals[index][0]:
                    count += 1
                    #将当前区间删除之后，就把这个区间的右边界更新为上一个和当前区间右边界的最小值
                    #画图就知道，已知i和i-1区间重叠，画两种情况，一种是i-1右区间大，一种是i右区间大
                    #如果遍历到i+1区间时，左边界如果大于i-1,i右区间的最小值，则只需要去掉i-1和i里，右区间最大的那个区间
                    #如果遍历到i+1区间时，左边界如果小于i-1,i右区间的最小值，则这个i+1区间也要去掉
                    intervals[index][1] = min(intervals[index-1][1],intervals[index][1])
        return count
        

                    
        
