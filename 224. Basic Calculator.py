class Solution:
    def calculate(self, s: str) -> int:
        #用一个计数器变量记录现在正在evaluate的总和 res
        #用一个变量记录现在是加号还是减号 sign +1默认值
        #用一个变量记录现在的数字，num  num = num * 10 + c
        #遇到(，将res 和 sign 压入栈
        #遇到), 将栈顶出栈，和res运算
        res = 0
        sign = 1
        num = 0
        stack = []
        s = list(s)
        s = [c for c in s if c != " "]

        for i, c in enumerate(s):
            if c == "(":
                stack.append((res, sign))
                res = 0
                sign = 1
                num = 0
            elif c == ")":
                popNum, popSign = stack.pop()
                res = popNum + res*popSign
                num = 0
            elif c == "+":
                sign = 1
                num = 0
            elif c == "-":
                sign = -1
                num = 0
            else:
                num = num * 10 + int(c)
                if i == len(s)-1 or (i < len(s)-1 and not s[i+1].isdigit()):
                    res += num * sign
        return res


        

        
