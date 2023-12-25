class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxleft = maxright = 0
        left_bound = right_bound = 0
        water = 0
        
        while left < right:
            if height[left] > maxleft:
                left_bound = left
                maxleft = height[left]
            if height[right] > maxright:
                right_bound = right
                maxright = height[right]
            water = max(min(maxleft,maxright) * (right_bound-left_bound),water)
            #移动左右指针时，移动板子高度低的那个，因为移动高的板子并不会增加水的体积
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1      
        return water
            



