#看代码随想录看完模拟过程 然后自己举例子写出来这个
#局部最优：跳到的格子是未来可以覆盖范围最远的格子
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        index, cover, step = 0, nums[0] , 1
        while index <= cover:

            if cover >= len(nums)-1: #覆盖最后一个数
                return step
            if cover <= len(nums)-1: #还没覆盖到最后一个数
                step += 1

            max_next_cover = cover
            for next_index in range(index+1, cover+1):
                if next_index+nums[next_index] > max_next_cover:
                    index = next_index
                    max_next_cover = next_index + nums[next_index]
            cover = max_next_cover
        

            

        
