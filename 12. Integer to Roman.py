class Solution:
    def intToRoman(self, num: int) -> str:
        dic = dict({1:'I',4:'IV', 5:'V',9:'IX', 10:'X',40:'XL', 50:'L', 90:'XC', 100:'C',400:'CD', 500:'D', 900:'CM',1000:'M'})
        res = ""
        divisors = [1000,900,500,400,100,90,50,40,10,9,5,4]
        for divisor in divisors:
            n = num // divisor
            num = num % divisor
            if n > 0:
                res += dic[divisor] * n
        if num != 0:
            res += "I" * num
            
        return res
        
