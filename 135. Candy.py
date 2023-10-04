#先看右边比左边大的情况（前一个比后一个大，从左边开始遍历）
#然后看左边比右边大的情况（前一个比后一个大，从右边开始遍历）
#然后两个结果取最大值就是最终给的糖果数
#不过其实可以在第二次遍历的时候就直接取最大值
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_l_to_r = [1] * len(ratings)
        candy_result = [1] * len(ratings)
        #前一个比后一个大，从左边开始遍历(右边>左边)
        for i in range(len(ratings)):
            if i > 0:
                if ratings[i] > ratings[i-1]:
                    candy_l_to_r[i] = candy_l_to_r[i-1] + 1
        
        #前一个比后一个大， 从右边开始遍历（左边>右边）
        for i in range(len(ratings)-1, -1, -1):
            if i == len(ratings) - 1:
                candy_result[i] = max(1, candy_l_to_r[i])
            if i < len(ratings) - 1:
                if ratings[i] > ratings[i+1]:
                    candy_result[i] = candy_result[i+1] + 1
                candy_result[i] = max(candy_l_to_r[i], candy_result[i] )

        return sum(candy_result)


            
        
