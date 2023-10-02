#看代码随想录讲：只要把每个正利润加起来就行，因为没考察什么时候买入什么时候卖出
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        benefit_sum = 0
        prev_price = prices[0]

        for price in prices:
            if price > prev_price:
                benefit_sum += price - prev_price
            prev_price = price
        return benefit_sum
        
