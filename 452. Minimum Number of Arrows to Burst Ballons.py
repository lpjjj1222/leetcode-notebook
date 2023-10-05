#要看代码随想录
#最先按照左边界排列气球
#如果当前气球的左边界大于上一个气球的右边界，则没有重合，如果小于，则有重合
#那如果第一个和第二个有重合，如何确认第三个气球会不会跟前两个气球一起射穿呢？
#那就要取上两个气球的最小右边界，把第二个气球的边界更新成这个值
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0]) #按照左边界排列气球
        arrows = 1
        for index in range(1, len(points)):
            if points[index][0] <= points[index-1][1]:
                 #当前左边界小于上一个右边界的话
                 points[index][1] = min(points[index][1],points[index-1][1])
                 #将当前右边界更新为当前右边界和上一个右边界的较小值
                 #且当前气球不浪费arrow，直接continue
                 continue
            else:
                #当前气球和上一个气球没有重叠
                arrows += 1
        return arrows





        
        
