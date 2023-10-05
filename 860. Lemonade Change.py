class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                five -= 1
                ten += 1
            else:
                #局部最优：收到20找零，有两种找零方法 一个是10+5， 另一个是5+5+5
                #优先用第一种方法找零，因为5更万能，可以给10给20找零，应该尽可能留多点
                twenty += 1
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five >= 0 and ten >= 0 and twenty >= 0:
                continue
            else:
                return False
        return True
        
