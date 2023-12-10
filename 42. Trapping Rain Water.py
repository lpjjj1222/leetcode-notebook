#暴力算法time limit exceeded：遍历每个height, 找到height左边的最大值，和右边的最大值，这两个最大值取小的那个，用当前height减去这个较小值就是该柱子上方装水量，把每个累积起来就行。
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        
        result = 0
        for i in range(1,len(height)-1):
            left_max, right_max = 0, 0
            for left_i in range(0, i):
                left_max = max(left_max, height[left_i])
            for right_i in range(i+1, len(height)):
                right_max = max(right_max, height[right_i])
            add_water = max(min(right_max, left_max) - height[i],0) #不能为负数，比如左边最大值如果是0的话
            result += add_water
        return result
'''
#动态规划
#先从左向右遍历，一边遍历一边得到每个位置其左边的最大值,得到一个list
#从右向左遍历，一边遍历一边得到每个位置其右边的最大值,得到第二个list
#两个list相同位置取最小值，像暴力解法一样算就行了。
#这是n + n + n所以时间复杂度是O(N)
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        for h in range(len(height)):
            if not left_max:
                left_max.append(0)
                max_h = height[h]
                print("max_h=",max_h)
            else:
                left_max.append(max_h)
                max_h = max(max_h,height[h])
        print(left_max)
        
        right_max = []
        for h in range(len(height)-1, -1, -1):
            if not right_max:
                right_max.insert(0, 0)
                max_h = height[h]
            else:
                right_max.insert(0,max_h)
                max_h = max(max_h,height[h])
        print(right_max)

        result = 0
        for i in range(len(height)):
            add_water = max(min(right_max[i], left_max[i])- height[i],0) #防止让它为负数
            result += add_water
        return result
'''

#双指针
#左指针在最左，右指针在最右，如果左指针数大，则左指针向右移一格，添加雨水，然后更新left_max
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0

        left_max, right_max = 0, 0

        while left < right:
            if height[left] < height[right]:
                add_water = max(left_max - height[left],0)
                result += add_water
                left_max = max(left_max, height[left])
                left += 1
            else:
                add_water = max(right_max - height[right], 0)
                result += add_water
                right_max = max(right_max, height[right])
                right -= 1
        return result
        
        




        

        
